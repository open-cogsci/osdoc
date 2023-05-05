title: advanced_delay
hash: 05d5215072bc5c76e2fd177cc099d6281a44d87cde42c43e79a945b2ac83b98f
locale: es
language: Spanish

El complemento `advanced_delay` retrasa el experimento durante una duración promedio preespecificada más un margen aleatorio.

- *Duración* es la duración promedio del retraso en milisegundos.
- *Variación* es el tamaño de la variación en el retraso en milisegundos.
- *Modo de variación* es cómo se calcula la variación:
	- *Desviación estándar* tomará la variación de una distribución gaussiana con la variación como desviación estándar.
	- *Uniforme* tomará la variación en duración de una distribución uniforme.