# sc-data
Stellarcarbon public data

## Development

This repo follows a template for git commit messages:
`<data-dir> schema <current alembic revision>`

Before committing data with a new (incompatible) schema, first tag the current HEAD with the
version prefix of the last compatible package version, e.g.:

```sh
git tag -a sc-audit-v0.9 -m "sc-audit schema 04d168a1598f"
git push --tags
```

Then, commit the data with applied revision normally. It does not need to be tagged until
it becomes the latest compatible version.

```sh
git add sc-audit/*.ndjson
git commit -m "sc-audit schema 77ea86674a18"
git push
```

