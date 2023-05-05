title: Integración con el Open Science Framework
hash: b86c05caa254209c5f4d161cd5c5a9daffef60ec5e5d5fca41a7aec00643d1f7
locale: es
language: Spanish

[TOC]

## Acerca de

La extensión OpenScienceFramework conecta OpenSesame con el [Open Science Framework](https://osf.io) (OSF), que es una plataforma web para compartir, conectar y optimizar flujos de trabajo científicos. Para usar esta extensión, [necesitas una cuenta de OSF](https://osf.io/login/?sign_up=True).

Con la extensión OpenScienceFramework, puedes:

- Guardar automáticamente tu experimento en el OSF
- Subir automáticamente datos al OSF
- Abrir experimentos desde el OSF
- Compartir tu experimento y datos con otros investigadores, dándoles acceso a través del OSF

## Iniciar sesión en el OSF

Para iniciar sesión en el OSF:

- Crea una cuenta en <https://osf.io>. (No puedes crear una cuenta desde dentro de OpenSesame).
- En OpenSesame, haz clic en el botón de inicio de sesión en la barra de herramientas principal e ingresa tus datos.
- Una vez que hayas iniciado sesión, puedes abrir el Explorador de OSF haciendo clic en tu nombre donde solía estar el botón de inicio de sesión y seleccionando *Mostrar explorador*. El explorador mostrará una vista general de todos tus proyectos de OSF y de todos los repositorios/servicios en la nube que estén vinculados a tus proyectos.

## Vincular un experimento con el OSF

Si vinculas un experimento con el OSF, cada vez que guardes el experimento en OpenSesame, también se subirá una nueva versión al OSF.

Para vincular un experimento:

- Guarda el experimento en tu computadora.
- Abre el explorador de OSF y selecciona una carpeta o repositorio donde te gustaría que se almacenara tu experimento en el OSF. Haz clic con el botón derecho en esta carpeta y selecciona *Sincronizar experimento en esta carpeta*. El nodo de OSF al que está vinculado el experimento se mostrará en la parte superior del explorador.
- Luego, el experimento se sube a la ubicación seleccionada.
- Si marcas *Siempre subir experimento al guardar*, se guardará automáticamente una nueva versión en el OSF en cada guardado; si no habilitas esta opción, se te preguntará cada vez si deseas hacerlo o no.

Para desvincular un experimento:

- Abre el explorador de OSF y haz clic en el botón *Desvincular* junto al enlace *Experimento vinculado a*.

## Vincular datos con el OSF

Si vinculas datos con el OSF, cada vez que se recopilen datos (normalmente después de cada sesión experimental), estos datos también se subirán al OSF.

Para vincular datos al OSF:

- Guarda el experimento en tu computadora.
- Abre el explorador de OSF, haz clic con el botón derecho en la carpeta a la que deseas que se suban los datos y selecciona *Sincronizar datos en esta carpeta*. El nodo de OSF al que están vinculados los datos se mostrará en la parte superior del explorador.
- Si marcas *Siempre subir datos recopilados*, los archivos de datos se guardarán automáticamente en el OSF después de haber sido recopilados; si no habilitas esta opción, se te preguntará cada vez si deseas hacerlo o no.

Para desvincular datos del OSF:

- Abre el explorador de OSF y haz clic en el botón *Desvincular* junto al enlace *Datos almacenados en*.

## Abrir un experimento almacenado en el OSF

Para abrir un experimento desde el OSF:

- Abre el explorador de OSF y encuentra el experimento.
- Haz clic con el botón derecho en el experimento y selecciona *Abrir experimento*.
- Guarda el experimento en tu computadora.

## Manejo de versiones no coincidentes

Si abres un experimento en tu computadora que está vinculado al OSF, pero difiere de la versión en el OSF, se te preguntará qué quieres hacer:

- Usar la versión de tu computadora; o
- Usar la versión del OSF. Si eliges usar la versión del OSF, se descargará y sobrescribirá el experimento en tu computadora.

## Instalación de la extensión OpenScienceFramework

La extensión OpenScienceFramework se instala de manera predeterminada en el paquete de Windows de OpenSesame. Si la extensión no está instalada, puedes instalarla de la siguiente manera:

Desde PyPi:

~~~
pip install opensesame-extension-osf
~~~

En un entorno Anaconda

~~~
conda install -c cogsci opensesame-extension-osf
~~~

El código fuente de la extensión está disponible en GitHub:

- <https://github.com/dschreij/opensesame-extension-osf>

Y para el módulo `python-qosf`, que es utilizado por la extensión:

- <https://github.com/dschreij/python-qosf>