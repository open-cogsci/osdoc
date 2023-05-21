title: CSV 函数 (csv-parse)
hash: 5f9a447b8f22c3e45034906ed86a761bc4a16baf6749487111bc851ad0b7c621
locale: zh
language: Chinese

`csv-parse`库中的同步`parse()`函数可用。这允许您将CSV格式的文本（例如从文件池中的CSV文件）解析成对象。

__示例：__

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

概述请参见：

- <https://csv.js.org/parse/api/sync/#sync-api>