sc-audit v{cur_ver} applies migrations since v{prev_ver}. Tag the previous HEAD as:

```sh
git tag -a sc-audit-v{prev_prefix} {data_commit} -m "sc-audit schema {rev_before}"
git push --tags
```
