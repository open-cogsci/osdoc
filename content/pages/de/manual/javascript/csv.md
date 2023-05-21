title: CSV-Funktionen (csv-parse)
hash: 5f9a447b8f22c3e45034906ed86a761bc4a16baf6749487111bc851ad0b7c621
locale: de
language: German

Die synchrone `parse()` Funktion aus der `csv-parse` Bibliothek ist verfügbar. Dadurch können Sie CSV-formatierten Text, zum Beispiel aus einer CSV-Datei im Datei-Pool, in ein Objekt umwandeln.

__Beispiel:__

```js
const Bedingungen = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const Versuch of Bedingungen) {
    console.log(Versuch.distractor)
}
```

Für einen Überblick, siehe:

- <https://csv.js.org/parse/api/sync/#sync-api>