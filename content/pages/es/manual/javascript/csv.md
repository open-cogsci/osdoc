title: Funciones CSV (csv-parse)
hash: 5f9a447b8f22c3e45034906ed86a761bc4a16baf6749487111bc851ad0b7c621
locale: es
language: Spanish

La función síncrona `parse()` de la biblioteca `csv-parse` está disponible. Esto te permite analizar texto con formato CSV, por ejemplo, de un archivo CSV en el grupo de archivos, en un Objeto.

__Ejemplo:__

```js
const condiciones = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const ensayo of condiciones) {
    console.log(ensayo.distractor)
}
```

Para obtener una descripción general, consulta:

- <https://csv.js.org/parse/api/sync/#sync-api>