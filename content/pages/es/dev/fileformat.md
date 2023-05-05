title: Formato de archivo (.osexp)
hash: 310dc6efe4055dac4dd14eda896adcf8c98e4a4f1950bb613ed0c1fd461c5ebc
locale: es
language: Spanish

[TOC]

## El formato .osexp

Los experimentos de OpenSesame se guardan en formato `.osexp`. Lo que es un archivo `.osexp` depende de si hay archivos incluidos en el experimento, es decir, si el grupo de archivos está vacío o no.

## Si el grupo de archivos está vacío

Si el grupo de archivos está vacío, el experimento se guarda como un archivo de texto sin formato. Este archivo está codificado en utf-8 y usa finales de línea al estilo Unix. Puedes editar y ver este archivo en la mayoría de los editores de texto.

La sintaxis de OpenSesame-script se describe aquí:

- %link:opensesame-script%

## Si el grupo de archivos no está vacío

Si hay archivos en el grupo de archivos, el experimento se guarda como un archivo `.tar.gz`, que es un formato de archivo similar a `.zip`. Dentro de este archivo, encontrarás lo siguiente:

- `script.opensesame` es el script experimental, en el mismo formato que se describe arriba
- `pool/` es una carpeta que contiene todos los archivos en el grupo de archivos. Cualquier carácter no ASCII en los nombres de archivo es reemplazado por cadenas `U+XXXX`.

## ¿Qué pasó con los formatos .opensesame y .opensesame.tar.gz?

Todavía puedes abrir el formato `.opensesame` y `.opensesame.tar.gz`, que se usaba para OpenSesame <= 2.9.X. Sin embargo, ya no puedes guardar experimentos en este formato.