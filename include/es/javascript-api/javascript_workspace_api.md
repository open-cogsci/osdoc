## reset_feedback()
Reinicia todas las variables de retroalimentación a su estado inicial.

**Ejemplo**
```js
reset_feedback()
```
<a name="set_subject_nr"></a>

## set_subject_nr(nr)
Establece el número de sujetos y la paridad (par / impar). Esta función se llama
automáticamente cuando inicia un experimento, por lo que solo necesita llamarla
si sobrescribe el número de tema que se especificó cuando se
lanzó el experimento.


| Param | Tipo | Descripción |
| --- | --- | --- |
| nr | <code>Number</code> | El número de sujetos |

**Ejemplo**
```js
set_subject_nr(1)
console.log('Número de sujeto = ' + vars.subject_nr)
console.log('Paridad de sujeto = ' + vars.subject_parity)
```
<a name="sometimes"></a>

## sometimes([p])
Devuelve verdadero con cierta probabilidad. (Para una aleatorización más avanzada,
use el paquete `random-ext`, que está disponible como `random`).



| Param | Tipo | Predeterminado | Descripción |
| --- | --- | --- | --- |
| [p] | <code>Number</code> | <code>.5</code> | La probabilidad de devolver verdadero |

**Ejemplo**
```js
if (sometimes()) {
  console.log('A veces ganas')
} else {
  console.log('A veces pierdes')
}
```
<a name="xy_from_polar"></a>

## xy_from_polar(rho, phi, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
Convierte coordenadas polares (distancia, ángulo) a coordenadas cartesianas
(x, y).

**Devuelve**: <code>Array.&lt;Number&gt;</code> - Un array [x, y].  


| Param | Tipo | Predeterminado | Descripción |
| --- | --- | --- | --- |
| rho | <code>Number</code> |  | La coordenada radial, también distancia o excentricidad. |
| phi | <code>Number</code> |  | La coordenada angular. Esto refleja una rotación     en sentido horario en grados (es decir, no en radianes), donde 0 está completamente a la derecha. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | El punto de referencia. |

**Ejemplo**
```js
// ECMA 5.1
var xy1 = xy_from_polar(100, 45)
var xy2 = xy_from_polar(100, -45)
var c = Canvas()
c.line({sx: xy1[0], sy: xy1[1], ex: -xy1[0], ey: -xy1[1]})
c.line({sx: xy2[0], sy: xy2[1], ex: -xy2[0], ey: -xy2[1]})
c.show()
// ECMA 6
let [x1, y1] = xy_from_polar(100, 45)
let [x2, y2] = xy_from_polar(100, -45)
let c = Canvas()
c.line({sx: x1, sy: y1, ex: -x1, ey: -y1})
c.line({sx: x2, sy: y2, ex: -x2, ey: -y2})
c.show()
```
<a name="xy_to_polar"></a>

## xy_to_polar(x, y, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
Convierte coordenadas cartesianas (x, y) a coordenadas polares (distancia,
ángulo).


**Devuelve**: <code>Array.&lt;Number&gt;</code> - Un array [rho, phi]. Aquí, `rho` es la coordenada radial,
    también distancia o excentricidad. `phi` es la angular
    coordenada en grados (es decir, no en radianes), y refleja una
    rotación en sentido antihorario, donde 0 está completamente a la derecha.  


| Param | Tipo | Predeterminado | Descripción |
| --- | --- | --- | --- |
| x | <code>Number</code> |  | La coordenada X. |
| y | <code>Number</code> |  | La coordenada Y |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | El punto de referencia. |

**Ejemplo**
```js
// ECMA 5.1 (navegador + escritorio)
var rho_phi = xy_to_polar(100, 100)
var rho = rho_phi[0]
var phi = rho_phi[1]
// ECMA 6 (solo navegador)
let [rho, phi] = xy_to_polar(100, 100)
```
<a name="xy_distance"></a>

## xy_distance(x1, y1, x2, y2) ⇒ <code>Number</code>
Da la distancia entre dos puntos.

**Devuelve**: <code>Number</code> - La distancia entre los dos puntos.  


| Param | Tipo | Descripción |
| --- | --- | --- |
| x1 | <code>Number</code> | La coordenada x del primer punto. |
| y1 | <code>Number</code> | La coordenada y del primer punto. |
| x2 | <code>Number</code> | La coordenada x del segundo punto. |
| y2 | <code>Number</code> | La coordenada y del segundo punto. |

<a name="xy_circle"></a>

## xy_circle(n, rho, [phi0], [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Genera una lista de puntos (coordenadas x, y) en un círculo. Esto puede ser
usado para dibujar estímulos en una disposición circular.

**Devuelve**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Un array de arrays de coordenadas [x,y].  

| Parámetro | Tipo | Predeterminado | Descripción |
| --- | --- | --- | --- |
| n | <code>Number</code> |  | El número de coordenadas x,y a generar. |
| rho | <code>Number</code> |  | La coordenada radial, también distancia o excentricidad,     del primer punto. |
| [phi0] | <code>Number</code> | <code>0</code> | La coordenada angular para la primera coordenada.     Esta es una rotación antihoraria en grados (es decir, no en radianes),     donde 0 está completamente a la derecha. |
| [polo] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | El punto de referencia. |

**Ejemplo**  
```js
// Dibujar 8 rectángulos alrededor de un punto de fijación central
// ECMA 5.1 (navegador + escritorio)
var c = Canvas()
c.fixdot()
var puntos = xy_circulo(8, 100)
for (var i in puntos) {
  var x = puntos[i][0]
  var y = puntos[i][1]
  c.rect({x: x - 10, y: y - 10, ancho: 20, alto: 20})
}
c.show()
// ECMA 6 (solo navegador)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_circulo(8, 100)) {
  c.rect({x: x - 10, y: y - 10, ancho: 20, alto: 20})
}
c.show()
```
<a name="xy_grid"></a>

## xy\_parrilla(n, espacio, [polo]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Genera una lista de puntos (coordenadas x,y) en una cuadrícula. Esto se puede usar
para dibujar estímulos en un arreglo de cuadrícula.


**Devuelve**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Un array de arrays de coordenadas [x,y].  

| Parámetro | Tipo | Predeterminado | Descripción |
| --- | --- | --- | --- |
| n | <code>Number</code> \| <code>Array.&lt;Number&gt;</code> |  | Un número que indica el número de     columnas y filas, de modo que `n=2` indica una cuadrícula de 2x2, o un [n_col,     n_row] array, de modo que `n=[2,3]` indica una cuadrícula de 2x3. |
| espacio | <code>Number</code> \| <code>Array.&lt;Number&gt;</code> |  | Un valor numérico que indica el     espacio entre celdas, o un array [col_espacio, row_espacio]. |
| [polo] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | El punto de referencia. |

**Ejemplo**  
```js
// Dibujar una cuadrícula de 4x4 de rectángulos
// ECMA 5 (escritorio + navegador)
var c = Canvas()
c.fixdot()
var puntos = xy_parrilla(4, 100)
for (var i in puntos) {
  var x = puntos[i][0]
  var y = puntos[i][1]
  c.rect({x: x - 10, y: y - 10, ancho: 20, alto: 20})
}
c.show()
// ECMA 6 (solo navegador)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_parrilla(4, 100)) {
  c.rect({x: x-10, y: y-10, ancho: 20, alto: 20})
}
c.show()
```
<a name="xy_random"></a>

## xy\_aleatorio(n, ancho, alto, [min_dist], [polo]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Genera una lista de puntos aleatorios (coordenadas x,y) con una mínima
espaciado entre cada par de puntos. Esta función lanzará un error
cuando la lista de coordenadas no se pueda generar, normalmente porque hay
demasiados puntos, el min_dist está demasiado alto, o el ancho o el alto están
configurados demasiado bajos.


**Devuelve**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Un array de arrays de coordenadas [x,y].  

| Parámetro | Tipo | Predeterminado | Descripción |
| --- | --- | --- | --- |
| n | <code>Number</code> |  | El número de puntos a generar. |
| ancho | <code>Number</code> |  | El ancho del campo con puntos aleatorios. |
| alto | <code>Number</code> |  | El alto del campo con puntos aleatorios. |
| [min_dist] | <code>Number</code> | <code>0</code> | La distancia mínima entre cada punto. |
| [polo] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | El punto de referencia. |

**Ejemplo**  
```js
// Dibujar 50 rectángulos en una cuadrícula aleatoria
// ECMA 5 (escritorio + navegador)
var c = Canvas()
c.fixdot()
var puntos = xy_aleatorio(50, 500, 500, 40)
for (var i in puntos) {
  var x = puntos[i][0]
  var y = puntos[i][1]
  c.rect({x: x - 10, y: y - 10, ancho: 20, alto: 20})
}
c.show()   
// ECMA 6 (solo navegador)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_aleatorio(50, 500, 500, 40)) {
  c.rect({x: x-10, y: y-10, ancho: 20, alto: 20})
}
c.show()
```