title: CSV functions (csv-parse)

The synchronous `parse()` function from the `csv-parse` library is available. This allows you to parse CSV-formatted text, for example from a CSV file in the file pool, into an Object.

__Example:__

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

For an overview, see:

- <https://csv.js.org/parse/api/sync/#sync-api>
