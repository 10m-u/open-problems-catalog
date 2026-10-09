# Tools

`fetch_sources.py` downloads the documents listed in `data/sources.json` into `fetched/`, which git ignores. If
`pdftotext` (poppler) is installed, it also writes a `.txt` next to each PDF. The documents are for your own
reading: most are under copyright and must not be redistributed.

```sh
python3 tools/fetch_sources.py                 # everything (several thousand documents; slow)
python3 tools/fetch_sources.py --question 3188 # only the sources of one problem
python3 tools/fetch_sources.py --limit 20      # a sample
```

The script waits two seconds between requests. Some hosts (publishers, ProQuest) refuse automated downloads; those
are reported and skipped.
