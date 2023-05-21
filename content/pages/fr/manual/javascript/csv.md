title: Fonctions CSV (csv-parse)
hash: 5f9a447b8f22c3e45034906ed86a761bc4a16baf6749487111bc851ad0b7c621
locale: fr
language: French

La fonction synchrone `parse()` de la bibliothèque `csv-parse` est disponible. Ceci vous permet d'analyser du texte au format CSV, par exemple à partir d'un fichier CSV dans le file pool, en un objet.

__Exemple :__

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Pour un aperçu, consultez :

- <https://csv.js.org/parse/api/sync/#sync-api>