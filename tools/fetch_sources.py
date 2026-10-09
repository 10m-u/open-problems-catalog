#!/usr/bin/env python3
"""Download the cited source documents for local reading (see tools/README.md)."""
import argparse
import json
import shutil
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = 'open-problems-catalog-fetch/1.0'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--question', type=int, action='append', help='only sources of these problem numbers')
    ap.add_argument('--limit', type=int)
    ap.add_argument('--out', default=str(ROOT / 'fetched'))
    a = ap.parse_args()
    docs = json.loads((ROOT / 'data' / 'sources.json').read_text())
    if a.question:
        docs = [d for d in docs if set(d['questions']) & set(a.question)]
    docs = docs[:a.limit] if a.limit else docs
    out = Path(a.out)
    out.mkdir(exist_ok=True)
    have_pdftotext = shutil.which('pdftotext') is not None
    for d in docs:
        dest = out / (d['document_id'] + '.pdf')
        if dest.exists():
            continue
        for url in [u for u in d['urls'] if u]:
            u = url.replace('arxiv.org/abs/', 'arxiv.org/pdf/').replace('arxiv.org/html/', 'arxiv.org/pdf/')
            try:
                req = urllib.request.Request(u, headers={'User-Agent': UA})
                with urllib.request.urlopen(req, timeout=90) as r:
                    body = r.read()
                if not body.startswith(b'%PDF'):
                    continue
                dest.write_bytes(body)
                (out / (d['document_id'] + '.json')).write_text(json.dumps(d, indent=1, ensure_ascii=False))
                if have_pdftotext:
                    subprocess.run(['pdftotext', '-layout', str(dest), str(dest.with_suffix('.txt'))], check=False)
                print('ok  ', d['document_id'], d['title'])
                break
            except Exception as e:
                print('fail', d['document_id'], u, type(e).__name__)
            finally:
                time.sleep(2)


if __name__ == '__main__':
    main()
