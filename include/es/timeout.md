## Tiempo de espera

El campo *Tiempo de espera* indica un valor de tiempo de espera en milisegundos o 'infinito' para no tener tiempo de espera. Cuando ocurre un tiempo de espera, suceden lo siguiente:

- Se establece `response_time` al valor del tiempo de espera, o más bien al tiempo que tarda en registrarse un tiempo de espera, lo que puede desviarse ligeramente del valor del tiempo de espera.
- Se establece la `respuesta` en 'None'. Esto significa que puedes especificar 'None' para la respuesta correcta cuando debe ocurrir un tiempo de espera; esto puede ser útil, por ejemplo, en una tarea de ir/no ir, cuando el participante debe retener una respuesta en las pruebas de no ir.