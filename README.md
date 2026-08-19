# unitsize

Human readable byte sizes, both directions. No dependencies.

```python
>>> from unitsize import human_size, parse_size
>>> human_size(2500)
'2.4 KB'
>>> human_size(5_000_000)
'4.8 MB'
>>> parse_size("2.4 KB")
2458
```

## Install

```bash
pip install -e ".[test]"
```

## Tests

```bash
pytest
```

## Contributing

Small, focused pull requests are welcome. A behaviour change needs a test that
fails without it. Please keep the commit subject in the imperative mood and
under 72 characters.
