# sc-data

This repo contains the public data from [sc-audit](https://github.com/stellarcarbon/sc-audit),
serialized as one NDJSON file per database table.

Feel free to use this data for your own project. Its main purpose is to enable bootstrapping
for new sc-audit installations. It speeds up the initial data load considerably, compared to
loading all historical data from scratch. It also helps making our historical data freely accessible,
since getting a full history from the original data sources can be complicated and/or costly
to set up.

The data is kept up to date by running `sc-audit catch-up` daily in a GitHub workflow.
You can check whether the dump job has run succesfully in the [Actions tab](https://github.com/stellarcarbon/sc-data/actions).

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
