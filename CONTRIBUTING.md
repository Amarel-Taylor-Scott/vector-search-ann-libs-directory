# Contributing

This is a curated directory of public **ANN / vector-search libraries**. Listings
are pointers to upstream repos (name, org, category, license) — no third-party
code is vendored.

## Add or update an entry

1. Edit [`data.py`](data.py) — add a `Tool(...)` with the correct category, the
   `open_source` flag, the EXACT license, a short note, and the GitHub link. Omit
   anything you can't verify.
2. Run `python main.py generate` to refresh `README.md`.
3. Run `pytest -q`.
4. Open a PR linking the project.

## Quality bar

- Keep the focus on **embeddable ANN libraries** (HNSW/trees/quantization) — not
  vector *databases* or *embedding models*.
- Record the EXACT license; categorize accurately.
- `python main.py generate` must leave `README.md` unchanged in CI.
