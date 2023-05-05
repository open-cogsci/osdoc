title: Ejecutando experimentos en línea con OSWeb
hash: d164c11575309f8213f7683999953e7c4d0eb5adf6c728cb34d716947a673fbf
locale: es
language: Spanish

[TOC]

## El flujo de trabajo

Para una introducción al flujo de trabajo, consulta también:

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Related preprint (not identical to published manuscript)](https://doi.org/10.31234/osf.io/wnryc)</small>

### Desarrollando tu experimento

Primero, desarrollas tu experimento como lo harías normalmente, utilizando la aplicación de escritorio OpenSesame. No todas las funciones están disponibles en los experimentos en línea. En particular, no puedes usar elementos Python INLINE_SCRIPT, sino que tienes que usar elementos JavaScript INLINE_JAVASCRIPT. Durante el desarrollo de tu experimento, es importante verificar que tu experimento sea compatible con OSWeb.

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%
- %link:manual/osweb/questionnaires%

### Subiendo tu experimento a JATOS

Una vez que hayas desarrollado tu experimento, debes exportarlo desde OpenSesame y subirlo a JATOS. JATOS es un servidor web que gestiona experimentos: te permite generar enlaces que puedes distribuir a los participantes y guarda los datos que se han recopilado.

No hay un único servidor JATOS. Más bien, muchas instituciones mantienen su propio servidor JATOS. Además, <https://mindprobe.eu> es un servidor JATOS gratuito, patrocinado por ESCoP y OpenSesame.

- %link:jatos%

### Recolectando datos

Una vez que hayas subido tu experimento a JATOS, puedes comenzar a recolectar datos. Puedes hacerlo enviando manualmente enlaces a los participantes, por ejemplo a través de correo electrónico. O puedes utilizar una plataforma para la contratación de participantes, como Prolific, Mechanical Turk o Sona Systems.

- %link:prolific%
- %link:mturk%
- %link:sonasystems%

## Tutoriales

- %link:tutorials/intermediate-javascript%
- %link:wcst%
