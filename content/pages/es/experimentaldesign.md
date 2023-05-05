title: Notación para diseño experimental
hash: 060f0c16a9d8bf841b056d49c16778928d77563cfa43fa451a8ff159ed884b3b
locale: es
language: Spanish

Ir de una pregunta de investigación abstracta a un diseño experimental concreto puede ser difícil. Puedes aclarar el diseño para ti mismo escribiéndolo en notación formal. Hay muchas notaciones, pero aquí utilizaremos la propuesta por [Rouanet y Lepine (1977)][referencias]. Esta notación es simple, pero lo suficientemente flexible como para cubrir la mayoría de los diseños experimentales que encontrarás en la vida real.

[TOC]

## La notación básica

En esta notación, las condiciones (o factores) se denotan por una sola letra, con un número pequeño que indica cuántos niveles hay. Por ejemplo, si tienes tres duraciones de estímulos, podrías indicarlo como D<sub>3</sub>. Una condición especial es 'sujeto'. Si tienes *N* sujetos, indica esto como <u>S</u><sub>N</sub>. Puede sonar extraño referirse al sujeto como una condición, pero, en cierto sentido, eso es exactamente lo que es.

Hay dos operadores:

- &lt; &gt; indica 'encajonar', generalmente usado para condiciones que varían entre sujetos
- × indica 'cruzar', generalmente usado para condiciones que varían dentro de los sujetos

A menudo hay varias formas de escribir un diseño experimental. Por ejemplo, puedes omitir condiciones que no son relevantes para tu pregunta de investigación, como si un estímulo aparece en el lado izquierdo o derecho de la pantalla.

## Diseños intrasujetos

En un diseño intrasujetos, todos los participantes realizan todas las condiciones. Este es el tipo de diseño más poderoso, porque no sufre mucho de la variabilidad entre los participantes: Puedes comparar el desempeño de un participante en la condición A con su desempeño en la condición B.

Considera un paradigma de atención de Posner [(Posner, 1980)][referencias], en el que una flecha apunta hacia el lado izquierdo o derecho de la pantalla. La flecha está seguida por un objetivo que también aparece en el lado izquierdo o derecho de la pantalla. Por lo tanto, tenemos dos condiciones que varían dentro de los participantes:

- *lado de la señal* con dos niveles (izquierdo, derecho), o C<sub>2</sub>
- *lado del objetivo* con dos niveles (izquierdo, derecho), o T<sub>2</sub>

Podemos escribir este diseño como <u>S</u><sub>N</sub>×C<sub>2</sub>×T<sub>2</sub>

## Diseños intersujetos

En un diseño intersujetos, diferentes participantes realizan diferentes condiciones experimentales. Esto es menos poderoso que un diseño intrasujetos, porque las diferencias entre los participantes son una fuente importante de ruido: Si el desempeño del participante 1 en la condición A es mejor que el del participante 2 en la condición B, no sabes si esto se debe a un efecto de la condición o simplemente porque el participante 1 tiende a desempeñarse mejor que el participante 2. Por esta razón, los diseños intersujetos requieren un gran número de participantes.

Considera el famoso (y controvertido) experimento de priming social de [Bargh (1996)][referencias] en el que algunos participantes leen palabras asociadas con la vejez (por ejemplo, 'jubilado'), mientras que otros participantes leen palabras neutrales en edad (por ejemplo, 'sediento').

Por lo tanto, tenemos una condición que varía entre los participantes:

- *tipo de prime* con dos niveles (viejo, neutral), o P<sub>2<sub>

Podemos escribir este diseño como <u>S</u><sub>N</sub> &lt; P<sub>2</sub> &gt;

Rouanet y Lepine llaman a esto *emboîtement*, o 'encajonamiento'. Esto simplemente significa que ambos niveles de P tienen su propio grupo de sujetos N. Por lo tanto, el número total de sujetos es 2*N.

## Diseños complicados

Ocasionalmente, encontrarás diseños más complicados que no se pueden clasificar fácilmente como diseños intrasujetos o intersujetos. Los experimentos psicolingüísticos son buenos ejemplos de esto.

Consideremos un experimento de priming semántico, en el que una palabra objetivo está precedida por una palabra prime semánticamente relacionada (por ejemplo, 'jardín' -> 'flor' o 'gato' -> 'perro') o una palabra prime no relacionada (por ejemplo, 'dinero' -> 'flor' o 'sí' -> 'perro'). Para evitar que un participante vea una palabra varias veces, puedes 'rotar' las condiciones entre palabras:

- Participantes impares (1, 3, 5, etc.) hacen la rotación A:
    - 'flor' está en la condición relacionada
    - 'perro' está en la condición no relacionada
- Participantes pares (2, 4, 6, etc.) hacen la rotación B:
    - 'flor' está en la condición no relacionada
    - 'perro' está en la condición relacionada

Por lo tanto, tenemos dos condiciones:

- *tipo de prime* con dos niveles (relacionado, no relacionado), o P<sub>2</sub>; esto varía dentro de los sujetos
- *rotación* con dos niveles (A, B), o R<sub>2</sub>; esto varía entre los participantes

Entonces, el diseño es <u>S</u><sub>n</sub> &lt; R<sub>2</sub> &gt; × P<sub>2</sub>

## Limitaciones

Esta notación tiene varias limitaciones, que incluyen:

- No se puede indicar con qué frecuencia ocurren ciertas condiciones. Por ejemplo, en una tarea de señalización de Posner, los ensayos válidos (es decir, señal y objetivo en el mismo lado) generalmente ocurren con más frecuencia que los ensayos no válidos (es decir, señal y objetivo en lados opuestos). Esto no se puede anotar en la notación descrita aquí.
- Es difícil indicar el papel del 'ítem' en un diseño. Por ejemplo, en el diseño bajo [Diseños complicados], la palabra objetivo desempeña un papel similar al del participante. Es posible escribir un diseño centrado en el ítem o un diseño centrado en el participante (como en el ejemplo), pero no he encontrado una manera de hacerlo de manera satisfactoria en ambos casos.

## Referencias

<div class="reference" markdown="1">

Bargh, J. A., Chen, M., & Burrows, L. (1996). Automaticidad del comportamiento social: Efectos directos de la activación del rasgo constructivo y del estereotipo en la acción. *Revista de Personalidad y Psicología Social*, *71*(2), 230.

Posner, M. I. (1980). Orientación de la atención. *Revista Trimestral de Psicología Experimental*, *32*(1), 3–25. doi:10.1080/00335558008248231

Rouanet, H., & Lepine, D. (1977). Estructuras lineales y análisis de comparaciones. *Mathématiques et Sciences Humaines*, *56*, 5–46. Obtenido de: <http://www.numdam.org/item?id=MSH_1977__56__5_0>

</div>