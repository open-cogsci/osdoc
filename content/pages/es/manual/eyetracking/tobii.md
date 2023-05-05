title: Tobii
hash: 91075c11d390d9162057a382ddc27a006029b42c7c7c79882ad81ff5e90f4430
locale: es
language: Spanish

PyGaze ofrece soporte *experimental* para los rastreadores de mirada Tobii. El paquete `tobii-research` se puede instalar a través de `pip`, pero al momento de escribir este artículo requiere una versión específica de Python, y *qué* versión de Python requiere varía de una versión a otra. Por lo tanto, el primer paso es averiguar qué versión de Python necesitas. Puedes hacerlo visitando `tobii-research` en PyPi y haciendo clic en 'Descargar archivos':

- <https://pypi.org/project/tobii-research/#files>

Desde los nombres de los archivos, puedes saber qué versión de Python necesitas; por ejemplo, el `cp310` en el nombre
`tobii_research-1.10.2-cp310-cp310-win_amd64.whl` significa que necesitas Python 3.10 (`cp` significa C-Python).

A continuación, instala OpenSesame en un entorno Python de la versión correcta (por lo que Python 3.10 para la versión 1.10.2 de `tobii-research` como se muestra arriba). Esto se hace más fácilmente usando Anaconda, como se describe [aquí](%url:download%). Finalmente, instala el paquete `tobii-research` en este entorno Python.

```
!pip install tobii-research
```


Para obtener más información, consulte:

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>