title: Traducir
hash: 6c70867370aa97b006209d57e083504cd28b4f73a9eb715aae26ff5532faaf08
locale: es
language: Spanish

Si desea proporcionar una traducción, se recomienda enviar primero una consulta a <s.mathot@cogsci.nl> o publicar un mensaje en el [foro](https://forum.cogsci.nl/) para asegurarse de que su idioma ya no está siendo trabajado.

¡Se necesita muy poca habilidad técnica para contribuir con una traducción!

[TOC]

## Iniciando OpenSesame en un idioma específico

Por defecto, OpenSesame utiliza la configuración regional predeterminada de su sistema operativo si hay una traducción disponible y recurre al inglés si no hay una traducción disponible. Para iniciar OpenSesame con un idioma específico, puede cambiar la opción de idioma en Menú → Herramientas → Preferencias.

## Cómo traducir

### Traduciendo pestañas Markdown

#### Cómo traducir pestañas Markdown

Las pestañas Markdown son las pestañas tipo sitio web que presentan texto y opciones básicas. Un ejemplo de una pestaña Markdown es la pestaña Comenzar que se ve al iniciar OpenSesame.

Para traducir una pestaña Markdown, primero ubique el archivo `.md` sin traducir (en inglés). En el caso de la pestaña Comenzar, esto es:

- `opensesame_extensions\get_started\get_started.md`

A continuación, copie este archivo original a `[original folder]\locale\[your locale code]\get_started.md`. Entonces, si está trabajando en una traducción francesa (`fr_FR`), copiaría el `get_started.md` original en (creando subcarpetas si aún no existen):

- `opensesame_extensions\get_started\locale\fr_FR\get_started.md`

Finalmente, simplemente abra el archivo `get_started.md` a traducir en un editor de texto y tradúzcalo.

#### Lista de pestañas Markdown que deben ser traducidas

En el [código fuente de OpenSesame](https://github.com/smathot/opensesame):

- `opensesame_extensions/update_checker/failed.md`
- `opensesame_extensions/update_checker/update-available.md`
- `opensesame_extensions/update_checker/up-to-date.md`
- `opensesame_extensions/toolbar_menu/system-information.md`
- `opensesame_extensions/help/offline_help.md`
- `opensesame_extensions/bug_report/failure.md`
- `opensesame_extensions/bug_report/report.md`
- `opensesame_extensions/bug_report/success.md`
- `opensesame_extensions/after_experiment/finished.md`
- `opensesame_extensions/system_information/system-information.md`
- `opensesame_extensions/get_started/get_started.md`
- `opensesame_extensions/opensesame_3_notifications/new-user.md`
- `opensesame_extensions/opensesame_3_notifications/old-experiment.md`
- `opensesame_extensions/opensesame_3_notifications/new-experiment.md`
- `opensesame_plugins/notepad/notepad.md`
- `opensesame_plugins/port_reader/port_reader.md`
- `opensesame_plugins/repeat_cycle/repeat_cycle.md`
- `opensesame_plugins/quest_staircase_init/quest_staircase_init.md`
- `opensesame_plugins/parallel/parallel.md`
- `opensesame_plugins/advanced_delay/advanced_delay.md`
- `opensesame_plugins/joystick/joystick.md`
- `opensesame_plugins/reset_feedback/reset_feedback.md`
- `opensesame_plugins/fixation_dot/fixation_dot.md`
- `opensesame_plugins/touch_response/touch_response.md`
- `opensesame_plugins/external_script/external_script.md`
- `opensesame_plugins/quest_staircase_next/quest_staircase_next.md`
- `opensesame_plugins/video_player/video_player.md`
- `opensesame_resources/help/missing.md`
- `opensesame_resources/help/new_item_warning.md`

En el [código fuente de Rapunzel](https://github.com/smathot/rapunzel):

- `opensesame_extensions/RapunzelWelcome/rapunzel_welcome.md`

### Traduciendo el código fuente y la interfaz de usuario

#### Paso 1: Descargar translatables.ts

Si está comenzando una traducción desde cero, debe comenzar con `translatables.ts`, que contiene todas las cadenas que se deben traducir. OpenSesame y Rapunzel tienen su propia versión de este archivo, ambas deben ser traducidas.

En el [código fuente de OpenSesame](https://github.com/smathot/OpenSesame/), este archivo se puede encontrar en:

- `opensesame_resources/ts/translatables.ts`

En el [código fuente de Rapunzel](https://github.com/smathot/rapunzel/), este archivo se puede encontrar en:

- `opensesame_extensions/RapunzelLocale/translatables.ts`

Puede descargar o clonar el código fuente y abrir directamente estos archivos. O puede verlos a través de GitHub. En este último caso, en la parte superior derecha del archivo, verá un enlace 'Raw'. Haga clic derecho en este enlace y seleccione 'Guardar archivo como' (o algo similar, según su navegador) para guardar el archivo en su disco.

#### Paso 2: Instalar Qt Linguist

Qt Linguist es una herramienta gráfica que le ayudará en el proceso de traducción. Es fácil de usar y le permite simplemente seleccionar una cadena de texto (en inglés) e ingresar una traducción.

__Windows__

Puede descargar una versión independiente de Qt Linguist desde aquí:

- <https://github.com/thurask/Qt-Linguist/releases>


__Mac OS__

Puede descargar una versión independiente de Qt Linguist desde aquí:
- <https://github.com/lelegard/qtlinguist-installers/releases>

__Linux__

En Linux, Qt Linguist generalmente está disponible en los repositorios. Por ejemplo, en Ubuntu se puede instalar con:

	sudo apt-get install qttools5-dev-tools


#### Paso 3: Abrir translatables.ts en Qt Linguist

Ahora inicie Qt Linguist y abra `translatables.ts`. Primero se le pedirá que ingrese un idioma fuente y de destino. Deje la fuente tal como está: 'POSIX/ Cualquier país'. El idioma de destino debe establecerse en el idioma en el que traducirá OpenSesame. Deje la opción País/Región en 'Cualquier país'. Puede cambiar estas configuraciones más tarde a través de Menú → Editar → Configuración del archivo de traducción.

¡Ahora puedes empezar a traducir! A la izquierda verá una lista de 'contextos'. Estos indican en qué contexto se muestra el texto, lo cual es útil. Para traducir, simplemente haga clic en la primera cadena de texto fuente en el primer contexto, ingrese una traducción adecuada y presione `Ctrl+Enter` para avanzar a la siguiente cadena.

Algunas cadenas contendrán etiquetas HTML, como esta:

	Size<br /><i>in pixels</i>

En este caso, solo cambie el texto y deje las etiquetas HTML tal como están. Entonces, para una traducción al español, esto se convertiría en:

	Tamaño<br /><i>en píxeles</i>

Además, algunas cadenas contienen comodines, como esta:

	Tell me more about the %s item

Estos `%s` (y `%d`, `%f`, `{}`, etc.) comodines son espacios en blanco que se llenan automáticamente en OpenSesame. Respete estos (¡eliminar un comodín hará que el programa se bloquee!) e intente crear una traducción adecuada a su alrededor. Entonces, para una traducción al español, esto se convertiría en:

	Dime más sobre el elemento %s

#### Paso 4: Compilar su traducción al formato `.qm` y probarla

OpenSesame no utiliza el archivo `.ts` directamente, sino que requiere un archivo en formato `.qm`. Puede crear este archivo fácilmente desde Qt Linguist seleccionando 'Archivo → Liberar como'. Cree un archivo `.qm` con el mismo nombre (excepto por la extensión) que el archivo original.

Para OpenSesame, este archivo debe guardarse en (cambie `fr_FR` por la configuración regional apropiada):

- `opensesame_resources/locale/fr_FR.qm`

Para Rapunzel, este archivo debe guardarse en (cambie `fr_FR` por la configuración regional apropiada):

- `opensesame_extensions/RapunzelLocale/fr_FR.qm`

## Guardar y enviar sus traducciones

### Enviar por correo electrónico

Una vez que esté satisfecho con sus traducciones, envíe el archivo `.ts` traducido y todos los archivos `md` traducidos a <s.mathot@cogsci.nl>.

### Enviar a través de GitHub

También puede enviar (y actualizar) su traducción a través de GitHub. En primer lugar, agregue su traducción a su bifurcación de OpenSesame, como `opensesame_resources/ts/ll_RR.ts`, donde `ll` corresponde al idioma y `RR` a la región. Por ejemplo, `en_US` es inglés de EE. UU., `fr_FR` es francés y `zh_CN` es chino. Puede encontrar una lista de regiones e idiomas válidos [aquí](http://www.iana.org/assignments/language-subtag-registry).

De manera similar, agregue todos los archivos `.md` traducidos a su bifurcación de OpenSesame.

Finalmente, envíe una solicitud de extracción para que su traducción se incluya en OpenSesame.

## Actualizar una traducción existente

El proceso para actualizar una traducción existente es similar al descrito anteriormente para crear una nueva traducción. La diferencia crucial es que no comienzas con `resources/ts/translatables.ts`, sino con un archivo de traducción no vacío, como `resources/ts/fr_FR.ts`.