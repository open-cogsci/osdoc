title: advanced_delay
hash: 54879490fe7472c89ac95be6dc21911ffcdddabbe58ec3de0baf4b660ad5dc89
locale: es
language: Spanish

El complemento `advanced_delay` retrasa el experimento por una duración promedio preespecificada más un margen aleatorio.

- *Duration* es la duración promedio del retraso en milisegundos.
- *Jitter* es el tamaño de la variación en el retraso en milisegundos.
- *Jitter mode* es cómo se define el jitter:
  - *Standard deviation* tomará valores de una distribución Gaussiana con Jitter como la desviación estándar.
  - *Uniform* tomará valores de una distribución Uniforme centrada en Duration, con Jitter como el ancho.