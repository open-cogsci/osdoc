title: EyeLink
hash: 37419c41f2ba79dc8903d36fe35edc800de2791247978b58d7a4c3ee07121ff1
locale: es
language: Spanish

[TOC]

## Acerca de EyeLink

Los rastreadores oculares EyeLink, producidos por SR Research, se encuentran entre los rastreadores oculares más utilizados en la investigación psicológica. SR Research proporciona enlaces de Python para comunicarse con EyeLink (llamados PyLink), que son utilizados por PyGaze y por su propio plugin EyeLink. 


## Instalación de PyLink

La biblioteca de Python para la integración de EyeLink está disponible en PyPI como `sr-research-pylink`. Cuenta con compatibilidad total con Windows, macOS y Linux en Python 2.7 a 3.14, por lo que puede instalarse en las instalaciones más recientes de OpenSesame.

Puede instalarla directamente desde la terminal:

```
pip install sr-research-pylink
```

**Importante:** *No* intente instalar `pylink` ejecutando `pip install pylink`. ¡Si lo hace, instalará un paquete completamente distinto y no relacionado!

Puede encontrar más información sobre `sr-research-pylink` en el foro de SR Research (se requiere registro gratuito):

- <https://www.sr-research.com/support/> 
- <https://www.sr-research.com/support/thread-48.html>
	
## PyGaze

Después de instalar PyLink siguiendo las instrucciones anteriores, puede utilizar EyeLink con PyGaze. Consulte:

- %link:pygaze%

## Plugin EyeLink de SR Research

SR Research también proporciona su propio conjunto de plugins EyeLink para OpenSesame. Este plugin ofrece integración adicional con EyeLink que no está disponible a través de PyGaze, como un disparador de mirada, transferencia de EDF cuando una tarea se cancela y compatibilidad total durante la transferencia de cámara para modelos EyeLink recientes. Para instalar su plugin, ejecute:

```
pip install opensesame-plugin-eyelink
```

Para obtener más información, visite:

- <https://www.sr-research.com/support/thread-52.html>

## Opcional: EyeLink Developers Kit

Aunque ya no es necesario para ejecutar PyLink en OpenSesame, EyeLink Developers Kit (a veces llamado EyeLink Display Software) proporciona herramientas útiles adicionales, como el convertidor `edf2asc`, documentación y archivos de instalación offline de `sr-research-pylink` (.whl).

Si necesita estas utilidades, puede encontrar los instaladores para Windows, macOS y los repositorios de Ubuntu en el sitio de soporte de SR Research:

- <https://www.sr-research.com/support/forum-9.html>