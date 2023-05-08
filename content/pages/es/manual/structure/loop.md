title: Bucles y variables independientes
hash: f52d2b6f370a4abedc40605527622cea0ff9e57163ef51e6d8d4e39ff35789ec
locale: es
language: Spanish

El ítem LOOP tiene dos funciones importantes:

- Ejecuta otro ítem múltiples veces.
- Es donde generalmente se definen sus variables independientes; es decir, las variables que manipula en su experimento.

[TOC]

## El ítem a ejecutar

Un LOOP siempre está conectado a un único otro ítem: el ítem a ejecutar. Selecciona el ítem a ejecutar en el cuadro etiquetado como "Run". En la mayoría de los casos, el ítem a ejecutar es una SECUENCIA, que ejecuta múltiples ítems secuencialmente.

Dos estructuras SECUENCIA-LOOP comunes son:

- Si una SECUENCIA corresponde a un solo ensayo (por convención llamado *trial_sequence*), entonces un LOOP que está conectado a esta secuencia corresponde a múltiples ensayos o un bloque (por convención llamado *block_loop*).
- Si una SECUENCIA corresponde a un bloque de ensayos seguido de una visualización de retroalimentación (por convención llamada *block_sequence*), entonces un LOOP que está conectado a esta secuencia corresponde a múltiples bloques o una sesión experimental completa (por convención llamada *experimental_loop*).

## Definición de variables independientes

La tabla de LOOP es una forma potente pero simple de definir variables independientes. Cada columna en la tabla corresponde a una variable; cada fila corresponde a un ciclo, es decir, un nivel de la variable. Por ejemplo, un LOOP simple con una variable (`animal`) que tiene dos ciclos ("gato" y "perro") se ve así:

animal |
------ |
gato    |
perro   |

El LOOP tiene algunas opciones importantes:

*Repetir* indica cuántas veces se debe ejecutar cada ciclo. En el ejemplo anterior, se establece un repeat en 2, lo que significa que se llama *trial_sequence* dos veces mientras la variable `animal` tiene el valor "gato" y dos veces mientras `animal` tiene el valor "perro" (cuatro veces en total).

*Orden* indica si los ciclos se deben ejecutar secuencialmente o en orden aleatorio. La aleatorización es completa, en el sentido de que la lista completa de número-de-ciclos × repeticiones ensayos es aleatoria.

## Leer variables independientes desde archivo

Si desea leer variables independientes desde archivo, en lugar de ingresarlas en la tabla LOOP, puede hacerlo de la siguiente manera:

- Establezca *Fuente* en *archivo*.
- Seleccione un archivo de Excel (`.xlsx`) o CSV (`.csv`) en la entrada *Archivo*.

El archivo fuente sigue las mismas convenciones que la tabla LOOP; es decir, cada columna corresponde a una variable y cada fila corresponde a un ciclo.

Se espera que los archivos CSV estén en el siguiente formato:

- texto-claro
- separado por comas
- entrecomillado doble (las comillas dobles literales se escapan con barras invertidas)
- codificado en UTF-8

## Interrumpir LOOP

Si desea interrumpir el LOOP antes de que se hayan ejecutado todos los ciclos, puede especificar una expresión de interrupción. Esta expresión de interrupción sigue la misma sintaxis que otras expresiones condicionales, como se describe en:

- %link:manual/variables%

Por ejemplo, la siguiente declaración de interrupción rompería el LOOP tan pronto como se dé una respuesta correcta:

```python
correct == 1
```

La opción *evaluar en primer ciclo* indica si la declaración de interrupción debe evaluarse antes del primer ciclo, en cuyo caso es posible que no se ejecute ningún ciclo, o solo antes del segundo ciclo, en cuyo caso siempre se ejecuta al menos un ciclo. En algunos casos, la declaración de interrupción se referirá a una variable que solo se define después del primer ciclo; en ese caso, debe deshabilitar la opción 'Evaluar en primer ciclo' para evitar un error de 'Variable no existe'.

## Generación de un diseño factorial completo

Al hacer clic en *Diseño factorial completo*, se abre un asistente que le permite generar fácilmente un diseño factorial completo, es decir, un diseño en el que se produce cada combinación de factores.

## Pseudorandomización

Puedes agregar restricciones para la pseudorandomización al script del ítem LOOP. Esto baraja las filas, incluso si el orden está establecido en secuencial. (Actualmente, esto no es posible a través de la GUI.)

Ejemplo: asegúrese de que las repeticiones de la misma palabra (dada por la variable `word`) estén separadas por al menos 4 ciclos:

```python
constrain word mindist=4
```

Ejemplo: Asegúrese de que no se repita la misma palabra:

```python
constrain word maxrep=1
```

Los comandos `constrain` deben venir *después* de los comandos `setcycle`.

## Operaciones avanzadas de bucle

Los comandos para operaciones avanzadas de bucle deben venir *después* de los comandos `constrain` y `setcycle`.

### fullfactorial

La instrucción `fullfactorial` trata la tabla de bucle como la entrada para un diseño factorial completo. Por ejemplo, la siguiente tabla de bucle:

cue   | duration
----- | --------
left  | 0
right | 100
      | 200

Resultaría en:

cue   | duration
----- | --------
left  | 0
left  | 100
left  | 200
right | 0
right | 100
right | 200

### shuffle

`shuffle` sin argumento aleatoriza toda la tabla. Cuando se especifica el nombre de una columna (`shuffle cue`), solo se aleatoriza esa columna.

### shuffle_horiz

`shuffle_horiz` mezcla todas las columnas horizontalmente. Cuando se especifican varias columnas, solo esas columnas se mezclan horizontalmente.

Por ejemplo, cuando se aplica `shuffle_horiz word1 word2` a la siguiente tabla:

word1 | word2 | word3
----- | ----- | -----
cat   | dog   | bunny
cat   | dog   | bunny
cat   | dog   | bunny

El resultado podría ser (es decir, los valores se intercambian aleatoriamente entre `word1` y `word2`, pero no `word3`):

word1 | word2 | word3
----- | ----- | -----
dog   | cat   | bunny
dog   | cat   | bunny
cat   | dog   | bunny

### slice

`slice [from] [to]` selecciona una porción del bucle. Requiere un índice de inicio y un índice de final, donde 0 es la primera fila y los valores negativos se cuentan hacia atrás desde el final. (Al igual que el corte de listas en Python, en otras palabras.)

Por ejemplo, cuando se aplica `slice 1 -1` a la siguiente tabla:

word  |
----- |
cat   |
dog   |
bunny |
horse |

El resultado sería:

word  |
----- |
dog   |
bunny |

### sort

`sort [column]` ordena una sola columna, sin cambiar ninguna de las otras columnas.

### sortby

`sortby [column]` ordena toda la tabla por una sola columna.

### reverse

`reverse` invierte el orden de toda la tabla. Si se especifica el nombre de una columna (p. Ej., `reverse word`), solo se invierte esa columna, sin cambiar ninguna de las otras columnas.

### roll

`roll [value]` mueve toda la tabla hacia adelante (para valores positivos) o hacia atrás (para valores negativos). Si se especifica el nombre de una columna (p. Ej., `roll 1 word`), solo se mueve esa columna, sin cambiar ninguna de las otras columnas.

Por ejemplo, si se aplica `roll 1` a la siguiente tabla:

word  |
----- |
cat   |
dog   |
bunny |
horse |

El resultado sería:

word  |
----- |
horse |
cat   |
dog   |
bunny |

### weight

`weight [column]` repite cada fila según un valor de ponderación especificado en una columna.

Por ejemplo, si se aplica `weight w` a la siguiente tabla:

word  | w
----- | -
cat   | 0
dog   | 0
bunny | 2
horse | 1

El resultado sería:

word  | w
----- | -
bunny | 2
bunny | 2
horse | 1

## Vista previa del bucle

Si ha especificado restricciones o ha utilizado operaciones avanzadas de bucle, entonces es una buena idea verificar que el resultado sea el esperado. Para hacerlo, puede generar una vista previa de la tabla de bucle tal como estará (o podría ser, en caso de aleatorización) cuando ejecute el experimento.

Para generar una vista previa, haga clic en el botón *Vista previa*.

## Accediendo a la tabla de bucle en Python inline script

La tabla de LOOP original, como la ve en la interfaz de usuario de OpenSesame, es un objeto [`DataMatrix`](http://datamatrix.cogsci.nl/) llamado `dm`, y es una propiedad del elemento LOOP.

Esta tabla de LOOP original generalmente se transforma de varias maneras; por ejemplo, el orden de las filas se puede aleatorizar y las filas se pueden repetir varias veces. El LOOP transformado también es un objeto `DataMatrix` y se llama `live_dm`. `live_dm` se crea justo antes de que se ejecute el bucle y se establece en `None` cuando finaliza el bucle; es decir, `live_dm` solo está disponible durante la fase de *ejecución* del LOOP.

Finalmente, el índice de la fila actual se guarda como la variable experimental `live_row`. Es decir, `live_row` indica la fila activa actual de `live_dm`.

Entonces digamos que tenemos un LOOP llamado *block_loop*. Podríamos acceder a la tabla LOOP en un script inline de Python de la siguiente manera:

~~~ .python
print('La tabla de loop original:')
print(items['block_loop'].dm)

print('La tabla de loop transformada:')
print(items['block_loop'].live_dm)

print('La fila actual:')
print(items['block_loop'].live_dm[var.live_row])
~~~

Incluso puedes definir programáticamente la tabla LOOP. Tienes que hacer esto en la fase de Preparación de un INLINE_SCRIPT que precede al LOOP.

```python
from datamatrix import DataMatrix

items['block_loop'].dm = DataMatrix(length=4)
items['block_loop'].dm.cue_side = 'left', 'right', 'left', 'right'
items['block_loop'].dm.cue_validity = 'valid', 'valid', 'invalid', 'invalid'
```

Los objetos `DataMatrix` son estructuras poderosas para trabajar con datos tabulares. Para obtener más información, consulta:

- <https://pydatamatrix.eu/>