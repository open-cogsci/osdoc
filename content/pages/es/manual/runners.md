title: Corredores
hash: 06242415e6cca1b1434321f7ba96e925abe4ccd2fd31cac48ab7ff6b64f73876
locale: es
language: Spanish

[TOC]

## Acerca de los ejecutores

Hay varias maneras técnicamente diferentes en las que puedes ejecutar tu experimento. Cada una de estas corresponde a un *ejecutor*. Puedes seleccionar un ejecutor en Menú → Herramientas → Preferencias → Ejecutor.

A menos que tengas una razón para no hacerlo, deberías usar el ejecutor *multiproceso*. Sin embargo, si OpenSesame a veces se bloquea, puedes probar si seleccionar un ejecutor diferente resuelve esto.

## Ejecutores disponibles

### Multiproceso

El ejecutor *multiproceso* ejecuta tu experimento en un proceso diferente. La ventaja de este enfoque es que tu experimento puede bloquearse sin derribar la interfaz de usuario con él. Otra ventaja del ejecutor *multiproceso* es que permite que el inspector de variables muestre tus variables experimentales mientras se ejecuta el experimento.

### En proceso

El ejecutor *en proceso* ejecuta el experimento en el mismo proceso que la interfaz de usuario. La ventaja de este enfoque es su simplicidad. La desventaja es que la interfaz de usuario puede bloquearse si el experimento se bloquea y viceversa.

### Externo

El ejecutor *externo* ejecuta el experimento iniciando opensesamerun como una aplicación separada. La ventaja de este enfoque es que tu experimento puede bloquearse sin derribar la interfaz de usuario con él.