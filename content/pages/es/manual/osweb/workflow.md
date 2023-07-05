title: Ejecutando experimentos en línea con OSWeb
hash: f0cc1f57958c34a65409a874ee511e03fee4f8ee35bc0bef55d0af11ac74f56e
locale: es
language: Spanish

[TOC]


## El flujo de trabajo

Para una introducción al flujo de trabajo, también puedes consultar:

Mathôt, S., & March, J. (2022). Realizando experimentos lingüísticos en línea con OpenSesame y OSWeb. *Aprendizaje de lenguas*. doi:10.1111/lang.12509
<br /><small>[Preimpresión relacionada (no idéntica al manuscrito publicado)](https://doi.org/10.31234/osf.io/wnryc)</small>


### Desarrollando tu experimento

Primero, desarrollas tu experimento como normalmente lo harías, utilizando la aplicación de escritorio de OpenSesame. No todas las funcionalidades están disponibles en los experimentos en línea. En particular, no puedes usar los elementos de Python INLINE_SCRIPT, sino que debes usar los elementos de JavaScript INLINE_JAVASCRIPT en su lugar. Durante el desarrollo de tu experimento, por lo tanto, es importante verificar que tu experimento sea compatible con OSWeb.

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%


### Subiendo tu experimento a JATOS

Una vez que hayas desarrollado tu experimento, lo publicas en JATOS. JATOS es un servidor web que gestiona experimentos: te permite generar enlaces que puedes distribuir a los participantes, y guarda los datos que se han recopilado.

No hay un único servidor JATOS. Más bien, muchas instituciones mantienen su propio servidor JATOS. Además, <https://mindprobe.eu> es un servidor JATOS gratuito, patrocinado por ESCoP y OpenSesame.

- %link:jatos%


### Recopilación de datos

Una vez que hayas publicado tu experimento en JATOS, puedes comenzar a recopilar datos. Puedes hacer esto enviando manualmente enlaces a los participantes, por ejemplo por correo electrónico. O puedes usar una plataforma para el reclutamiento de participantes, como Prolific, Mechanical Turk o Sona Systems.

- %link:prolific%
- %link:mturk%
- %link:sonasystems%


### Análisis de datos

Una vez que la recopilación de datos esté terminada, puedes descargar los datos desde JATOS y convertirlos a formato `.xlsx` o `.csv` para su posterior análisis:

- %link:manual/osweb/data%


## Tutoriales

- %link:tutorials/intermediate-javascript%
- %link:wcst%