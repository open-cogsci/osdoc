title: Tobii
hash: a383da57d44200882bf0aa52f84f681e06fecc7982e5a785150b5372d2d75259
locale: es
language: Spanish

PyGaze ofrece soporte *experimental* para los rastreadores de mirada Tobii.

`tobii-research` es la biblioteca Python para soporte Tobii. A partir de julio de 2023, `tobii-research` requiere Python 3.10, mientras que OpenSesame utiliza por defecto Python 3.11. Por lo tanto, hasta que `tobii-research` se actualice para Python 3.11, la manera más fácil de instalar OpenSesame con soporte Tobii es construyendo un entorno Python 3.10 a través de Anaconda.

Esto suena complicado, pero realmente no lo es. Para hacerlo, primero lee el procedimiento general para instalar OpenSesame a través de Anaconda como se describe en la página de Descargas:

- %link:download%

A continuación, una vez que entiendas el procedimiento general, comienza creando un entorno Python 3.10, continúa con las instrucciones de la página de Descargas, y luego instala `tobii-research`:

```
# Comienza creando un entorno Python 3.10
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# Ahora sigue las instrucciones de la página de descargas
# ...
# Luego instala soporte Tobii
pip install tobii-research
# ¡Y ahora lanza OpenSesame!
opensesame
```

Para más información, consulta:

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>