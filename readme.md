# csv2md

A CLI tool that converts a CSV file into a Markdown table. Made in Python 3 using the csv library.

## Example

The csv-file *test.csv* has following content.

```
test.csv
--------------------
Fruit,Shape,Color
Apple,Round,Red
Banana,Curved,Yellow
```

By issuing the following command a markdown table will be created.

```
python3 csv2md.py test.csv -o test.md
```

```markdown
test.md
--------------------
|Fruit |Shape |Color |
|------|------|------|
|Apple |Round |Red   |
|Banana|Curved|Yellow|
```