#!/usr/bin/env python3
"""Dependency-free document, relative-link and release guard checks."""
import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = [ROOT / 'index.html', ROOT / 'privacy/index.html', ROOT / 'terms/index.html']

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.headings = set(), [], 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'Duplicate ID'
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.headings += 1
        if tag in ('a', 'link', 'script', 'img'):
            ref = attrs.get('href', attrs.get('src', ''))
            self.refs.append((tag, ref))

parser = argparse.ArgumentParser()
parser.add_argument('--release', action='store_true')
args = parser.parse_args()
pages = {path: Page(path.read_text()) for path in PUBLIC}
for path, page in pages.items():
    text = path.read_text()
    assert page.headings == 1, f'{path}: expected one h1'
    assert 'lang="en"' in text and 'name="viewport"' in text
    assert 'Content-Security-Policy' in text and 'href="#main"' in text
    if args.release:
        assert 'data-status="approved-local-app"' in text, f'{path.name}: explicit approval of the local-application legal website is required'
        assert not re.search(r'data-status="draft"|not yet effective|Drafts? for review|Review in progress|Effective date pending', text, re.I), f'{path.name}: unresolved approval labels'
        # Known, disclosed verification tasks remain in the approved local-app notice.
        # This release approves the legal website only, never bank-data processing.
        assert not re.search(r'TODO', re.sub(r'TODO L[1-3]\b', '', text)), f'{path.name}: unexpected TODO'
        if path.parent.name == 'privacy':
            assert 'The app has been implemented locally and its API registration has been checked.' in text
            for task in range(1, 4):
                assert f'TODO L{task} — ' in text, f'Missing disclosed verification task L{task}'
    for tag, ref in page.refs:
        target = urlsplit(ref)
        if target.scheme:
            assert target.scheme in ('https', 'mailto'), f'Unexpected URL: {ref}'
            assert tag == 'a', f'External runtime resource: {ref}'
            continue
        assert not ref.startswith('/'), f'Non-relative project URL: {ref}'
        dest = (path.parent / unquote(target.path)).resolve() if target.path else path
        if dest.is_dir():
            dest /= 'index.html'
        assert dest.is_relative_to(ROOT), f'Link escapes site: {ref}'
        assert dest.exists(), f'Broken link: {ref}'
        if target.fragment:
            assert dest in pages and unquote(target.fragment) in pages[dest].ids, f'Broken fragment: {ref}'

allowed = {p.relative_to(ROOT).as_posix() for p in PUBLIC} | {'assets/style.css', 'assets/theme.js'}
for folder in ('assets', 'privacy', 'terms'):
    for path in (ROOT / folder).rglob('*'):
        assert not path.is_symlink(), f'Symlink in public directory: {path.name}'
        if path.is_file():
            assert path.relative_to(ROOT).as_posix() in allowed, f'Unexpected public file: {path.name}'
for rel in allowed:
    text = (ROOT / rel).read_text()
    assert not re.search(r'-----BEGIN [A-Z ]*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.', text), f'Possible credential in {rel}'
    if rel.endswith('.js'):
        assert not re.search(r'localStorage|sessionStorage|document\.cookie|\bfetch\s*\(|XMLHttpRequest|sendBeacon|WebSocket', text), f'Unexpected storage/network API in {rel}'
print('PASS: 3 pages; local links and fragments; single h1; viewport, language, skip link, CSP; public file allowlist; common credential and tracking patterns.')
if not args.release:
    print('Run with --release to enforce the approved local-application publication scope.')
