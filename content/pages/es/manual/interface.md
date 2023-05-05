title: Usando la interfaz
hash: 76f98fb7d0797037375f61ab159fef066c3fe407e469e0f97494e76d38e6177e
locale: es
language: Spanish

OpenSesame tiene una potente interfaz gráfica que consta de varios componentes (%FigInterface).

%--
figure:
 id: FigInterface
 source: interface.png
 caption: La interfaz de usuario de OpenSesame.
--%


[TOC]

## Barras de herramientas y barra de menú

### La barra de menú

La barra de menú (%FigMenubar) se muestra en la parte superior de la ventana o, en algunos sistemas operativos, está integrada en el borde alrededor de la ventana. La barra de menú contiene funcionalidades generales, como guardar y abrir experimentos, ejecutar experimentos, etc.

%--
figure:
 id: FigMenubar
 source: menubar.png
 caption: La barra de menú.
--%

### La barra de herramientas principal

La barra de herramientas principal (%FigMainToolbar) se muestra (por defecto) en la parte superior de la ventana, justo debajo de la barra de menú. La barra de herramientas principal contiene una selección de las funciones más relevantes de la barra de menú.

%--
figure:
 id: FigMainToolbar
 source: main-toolbar.png
 caption: La barra de herramientas principal.
--%

### La barra de herramientas de ítems

La barra de herramientas de ítems (%FigItemToolbar) se muestra (por defecto) en el lado izquierdo de la ventana. La barra de herramientas de ítems contiene todos los ítems, es decir, todos los bloques de construcción de un experimento. Puede agregar ítems a su experimento arrastrándolos desde la barra de herramientas de ítems al área de descripción general.

%--
figure:
 id: FigItemToolbar
 source: item-toolbar.png
 caption: La barra de herramientas de ítems.
--%

## El área de pestañas

El área de pestañas es la parte central de la ventana (%FigTabArea). El área de pestañas es donde se muestran los controles de ítems, la documentación, mensajes importantes, etc. El área de pestañas puede contener múltiples pestañas y funciona como un navegador web con pestañas.

%--
figure:
 id: FigTabArea
 source: tab-area.png
 caption: El área de pestañas.
--%

## El área de descripción general

El área de descripción general (%FigOverviewArea) se muestra (por defecto) en el lado izquierdo de la ventana, a la derecha de la barra de herramientas de ítems. El área de descripción general muestra la estructura de su experimento como un árbol. Puede reordenar los ítems de su experimento arrastrándolos desde una posición a otra en el área de descripción general.

- Acceso rápido para ocultar/mostrar: `Ctrl+\`

%--
figure:
 id: FigOverviewArea
 source: overview-area.png
 caption: El área de descripción general.
--%

## El repositorio de archivos

El repositorio de archivos (%FigFilePool) se muestra (por defecto) en el lado derecho de la ventana. Proporciona una descripción general de todos los archivos que están incluidos en el experimento.

- Acceso rápido para ocultar/mostrar: `Ctrl+P`

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: El repositorio de archivos.
--%

## La ventana de depuración

La ventana de depuración (%FigDebugWindow) se muestra (por defecto) en la parte inferior de la ventana. Proporciona un [intérprete IPython](https://ipython.org/) y se utiliza como salida estándar mientras se ejecuta un experimento. Es decir, si usa la función `print()` de Python, el resultado se imprimirá en la ventana de depuración.

- Acceso rápido para ocultar/mostrar: `Ctrl+D`

%--
figure:
 id: FigDebugWindow
 source: debug-window.png
 caption: La ventana de depuración.
--%

## El inspector de variables

El inspector de variables (%FigVariableInspector) se muestra (por defecto) en el lado derecho de la ventana. Proporciona una lista de todas las variables que se detectan en su experimento. Cuando ejecuta un experimento, el inspector de variables también proporciona una descripción general en tiempo real de las variables y sus valores.

- Acceso rápido para ocultar/mostrar: `Ctrl+I`

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: El inspector de variables.
--%

## Atajos de teclado

Los atajos de teclado que se enumeran a continuación son valores predeterminados. Muchos de ellos se pueden cambiar a través de *Menú → Herramientas → Preferencias*.

### Atajos generales

Los siguientes atajos de teclado están disponibles en todas partes:

- Cambiador rápido: `Ctrl+Espacio`
- Paleta de comandos: `Ctrl+Shift+P`
- Nuevo experimento: `Ctrl+N`
- Abrir experimento: `Ctrl+O`
- Guardar experimento: `Ctrl+S`
- Guardar experimento como: `Ctrl+Shift+S`
- Deshacer: `Ctrl+Alt+Z`
- Rehacer: `Ctrl+Alt+Shift+Z`
- Ejecutar experimento a pantalla completa: `Ctrl+R`
- Ejecutar experimento en ventana: `Ctrl+W`
- Ejecución rápida del experimento: `Ctrl+Shift+W`
- Probar experimento en navegador: `Alt+Ctrl+W`
- Mostrar/ocultar área de resumen: `Ctrl+\`
- Mostrar/ocultar ventana de depuración: `Ctrl+D`
- Mostrar/ocultar conjunto de archivos: `Ctrl+P`
- Mostrar/ocultar inspector de variables: `Ctrl+I`
- Enfocar área de resumen: `Ctrl+1`
- Enfocar área de pestañas: `Ctrl+2`
- Enfocar ventana de depuración: `Ctrl+3`
- Enfocar conjunto de archivos: `Ctrl+4`
- Enfocar inspector de variables: `Ctrl+5`

### Atajos de editor

Los siguientes atajos de teclado están disponibles en los componentes del editor, como el INLINE_SCRIPT:

- (Des)comentar línea(s) seleccionada(s): `Ctrl+/`
- Buscar texto: `Ctrl+F`
- Reemplazar texto: `Ctrl+H`
- Ocultar diálogo de búsqueda/ reemplazo: `Escape`
- Duplicar línea: `Ctrl+Shift+D`
- Deshacer: `Ctrl+Z`
- Rehacer: `Ctrl+Shift+Z`
- Copiar: `Ctrl+C`
- Cortar: `Ctrl+X`
- Pegar: `Ctrl+V`

### Atajos del área de pestañas

Los siguientes atajos de teclado están disponibles en el área de pestañas:

- Pestaña siguiente: `Ctrl+Tab`
- Pestaña anterior: `Ctrl+Shift+Tab`
- Cerrar otras pestañas: `Ctrl+T`
- Cerrar todas las pestañas: `Ctrl+Alt+T`
- Cerrar pestaña actual: `Alt+T`

### Atajos del área de resumen y secuencia

Los siguientes atajos de teclado están disponibles en el área de resumen y en el elemento SEQUENCE:

- Menú contextual: `+`
- Copiar elemento (sin vincular): `Ctrl+C`
- Copiar elemento (vinculado): `Ctrl+Shift+C`
- Pegar elemento: `Ctrl+V`
- Eliminar elemento: `Del`
- Eliminar elemento permanentemente: `Shift+Del`
- Cambiar nombre: `F2`
- Cambiar declaración de ejecución si corresponde (si es aplicable): `F3`