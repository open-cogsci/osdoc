title: Respuesta táctil
hash: 1efac24d50a608e8694fed56d169d03f62defefdc30636bfc4f9ca23bb702995
locale: es
language: Spanish

El complemento `touch_response` te permite trabajar con respuestas táctiles (o clics de ratón) de una manera fácil, dividiendo la pantalla en filas y columnas. Cada respuesta está codificada por un solo número, que corresponde a la posición contando de izquierda a derecha y de arriba a abajo. Por ejemplo, si has especificado 2 columnas y 3 filas, la pantalla se divide en las siguientes regiones de respuesta:

```bash
1	2
3	4
5	6
```

De manera similar, si has especificado 4 columnas y 1 fila, la pantalla se divide horizontalmente en las siguientes regiones de respuesta:

```bash
1	2	3	4
```