title: OpenSesameRun (sin GUI)
hash: 435d6b0358c5bdd011dbe66206d56d78258410aadf1b385e46d7c8fedd2aecb2
locale: es
language: Spanish

## Acerca de

`opensesamerun` es una herramienta simple que te permite ejecutar experimentos de OpenSesame con una GUI mínima, o directamente, especificando todas las opciones necesarias a través de la línea de comandos. Una GUI mínima aparecerá automáticamente si no se han especificado todas las opciones de la línea de comandos, especialmente el archivo de experimento, el número de sujeto y el archivo de registro.

~~~
Uso: opensesamerun [experimento] [opciones]

Opciones:
  --version             mostrar el número de versión del programa y salir
  -h, --help            mostrar este mensaje de ayuda y salir

  Opciones de sujeto y archivo de registro:
    -s SUJETO, --subject=SUJETO
                        Número de sujeto
    -l ARCHIVO_REGISTRO, --logfile=ARCHIVO_REGISTRO
                        Archivo de registro

  Opciones de pantalla:
    -f, --fullscreen    Ejecutar en pantalla completa
    -c, --custom_resolution
                        No utilizar la resolución de pantalla especificada en
                        el archivo de experimento
    -w ANCHO, --width=ANCHO
                        Ancho de pantalla
    -e ALTO, --height=ALTO
                        Alto de pantalla

  Opciones varias:
    -d, --debug         Imprimir muchos mensajes de depuración en la salida
                        estándar
    --stack             Imprimir información de pila

  Opciones varias:
    --pylink            Cargar PyLink antes de PyGame (necesario para usar 
                        los complementos de Eyelink en modo no simulado)
~~~

## Ejemplo

Supongamos que quieres ejecutar el experimento de ejemplo de dirección de la mirada, para el sujeto # 1, y guardar el archivo de registro en tu carpeta Documentos (este ejemplo asume Linux, pero funciona de manera análoga en otras plataformas):

~~~
opensesamerun /usr/share/opensesame/examples/gaze_cuing.opensesame.tar.gz -s 1 -l /home/sebastiaan/Documents/sujeto1.tsv -f 
~~~


## Alternativa `libopensesame`

También puedes iniciar experimentos sin utilizar la GUI a través del módulo de Python `libopensesame`:

- %link:manual/python/nogui%