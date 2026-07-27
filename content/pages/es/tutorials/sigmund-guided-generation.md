title: Usa guided generation para crear cualquier experimento con SigmundAI
hash: 3cca055564d833b594ffb053c8d6d796732c86b27c92b7bbcf8a874169c96a50
locale: es
language: Spanish

[TOC]


## Acerca de este tutorial

En este tutorial, aprenderás a construir cualquier experimento con SigmundAI. Este no es un tutorial paso a paso centrado en un experimento específico. Más bien, describe un flujo de trabajo general, que puedes ajustar según tus necesidades.

¡No esperes milagros! Si tienes un experimento complejo, es probable que Sigmund tenga dificultades si se le deja completamente a su aire. A menudo necesitas trabajar activamente junto con Sigmund para implementar un experimento.

A esto lo llamo *guided generation*, porque guías a Sigmund a través del proceso.

Si aún no has trabajado con Sigmund, te recomiendo que primero completes [el tutorial para principiantes de SigmundAI](%url:beginner-sigmund%).


## Lo que aprenderás

Al final de este tutorial, sabrás cómo:

- 💡 Darle a Sigmund instrucciones claras y eficaces
- 💡 Dividir el proceso de construir un experimento completo desde cero en pasos manejables
- 💡 Corregir errores que Sigmund pueda cometer mientras construye un experimento.


## ¿Qué modelo debería usar?

La mayoría de los pasos no requieren un modelo especialmente potente. Yo uso principalmente Z.ai GLM 5.2, que al momento de escribir esto ofrece un buen equilibrio entre inteligencia y costo. Sin embargo, el paso final de implementación lleva al límite lo que la mayoría de los modelos de IA pueden hacer. Por lo tanto, en ese momento puedes cambiar a un modelo más potente, como Claude Sonnet 5. Ten en cuenta que los modelos más potentes también son (mucho) más caros.

En la práctica, prueba diferentes modelos para ver cuál da los mejores resultados para tus experimentos específicos.


## Flujo de trabajo

Esto es lo que vamos a hacer:

1. Describir el experimento que quieres construir con un lenguaje claro.
2. Pedirle a Sigmund que desarrolle tu descripción en una descripción narrativa completa que especifique el experimento con todo detalle.
3. Revisar la descripción completa. Si es necesario, discutirla y ajustarla.
4. Pedirle a Sigmund que desarrolle una especificación JSON (un formato técnico legible por humanos) que describa la estructura experimental.
5. Revisar la especificación JSON. Si es necesario, discutirla y ajustarla.
6. Pedirle a Sigmund que construya todo el experimento de una sola vez.
7. Probar y pulir el experimento.

Este tutorial trata sobre cómo comunicarse eficazmente con Sigmund. Vamos a ayudar a Sigmund a subdividir la compleja tarea de construir un experimento en subtareas manejables y a proporcionar instrucciones concretas sobre qué hacer y cuándo.

__Importante:__ Necesitas hablar con Sigmund a través del panel de chat dentro de OpenSesame. Si usas la interfaz web, Sigmund no podrá controlar OpenSesame.


## Desarrollar una descripción narrativa completa del experimento

Aquí está la descripción del experimento que usaremos para este ejemplo:

💬 **Descripción:**

```text
Una tarea típica de memoria de trabajo visual en la que deben recordarse círculos de diferentes colores. Se evalúa un círculo presentando un círculo del mismo color o de un color diferente en la ubicación original de ese círculo. El participante responde con un juicio de igual/diferente. Se varía el tamaño del conjunto.
```

Comenzamos pidiéndole a Sigmund que desarrolle una descripción detallada de un experimento basada en esta descripción. En la descripción de tu experimento, proporciona tantos detalles como puedas, porque esto ayuda a Sigmund a proponer un diseño que coincida con lo que tienes en mente. Por ejemplo, si crees que la lógica del ensayo debería implementarse con un `inline_script`, indícalo.

Incluimos esta descripción en un prompt que proporciona instrucciones claras a Sigmund:

💬 **Prompt:**

```text
¡Tengo una tarea desafiante para ti! Vamos a implementar un experimento de OpenSesame desde cero. Dividiremos el proceso en unos pocos pasos para que sea manejable. En el paso actual, tu tarea es ampliar la descripción de la tarea experimental para que contenga todos los detalles que necesitamos para implementarla.

Aquí tienes algunas cosas que debes considerar para la estructura del ensayo:

- La forma en que los participantes responden
- El timing de los estímulos
- La apariencia de los estímulos
- La disposición de los estímulos
- Si se proporciona retroalimentación al participante y, de ser así, cómo
- Cualquier estímulo que no se mencione explícitamente pero que deba incluirse
- Pantallas en blanco o de fijación entre estímulos (si hay un punto de fijación, normalmente se muestra durante todo el ensayo)

Aquí hay algunas cosas que se deben tener en cuenta para la estructura del experimento:

- Variables independientes y dependientes
- Si hay o no una fase de práctica
- Si los ensayos están o no subdivididos en bloques de ensayos
- El número de ensayos y (si corresponde) bloques
- Cualquier pantalla de bienvenida, instrucciones y despedida

Por favor, incluye también cualquier información adicional que consideres relevante.

<experimental_task_description>
Una tarea típica de memoria de trabajo visual en la que deben recordarse círculos de diferentes colores. Se evalúa un círculo presentando un círculo del mismo o de un color diferente en la ubicación original del círculo. El participante responde con un juicio de igual/diferente. Se varía el tamaño del conjunto.
</experimental_task_description>

Por favor, responde con una descripción completa. No la guardes todavía como una nota, porque primero vamos a revisarla.
```

Sigmund responderá con una descripción elaborada del experimento. Revísala y proporciona correcciones si es necesario. Si estás conforme, pídele a Sigmund que haga una nota de ello.


💬 **Prompt:**

```text
¡Genial! Por favor, guarda la descripción completa como una nota persistente para que no la olvides. No la resumas, sino guárdala íntegramente.
```


## Desarrollo de una especificación JSON para la estructura experimental

Ahora vamos a pedirle a Sigmund que diseñe la estructura experimental. Esto especifica qué elementos componen el experimento y cómo están conectados.

El segundo punto del prompt menciona qué tipos de ítems se pueden usar. Para ayudar a Sigmund, elimina los tipos de ítems que sabes que no serán necesarios. Por ejemplo, si los participantes no van a usar el ratón para responder, puedes eliminar el tipo de ítem `mouse_response`.


💬 **Prompt:**

```text
¡Continuamos! Aquí está tu siguiente tarea:

- Redacta una especificación JSON basada en la descripción narrativa del experimento que acabas de guardar como una nota.
- Cada dict en el JSON debe corresponder a un único ítem de OpenSesame. Puedes usar los siguientes ítems: [loop, sequence, sketchpad, feedback, synth, sampler, keyboard_response, mouse_response, logger, inline_script, inline_javascript, form_multiple_choice, form_text_display, form_text_input, reset_feedback]
- Los ítems de sketchpad se preparan con antelación y, por lo tanto, no pueden tener en cuenta variables que se definan después de su fase de prepare. Por ello, para mostrar pantallas con contenido variable, a menudo conviene usar ítems de feedback en su lugar, pero solo para pantallas que no sean críticas en cuanto al tiempo.
- No uses múltiples ítems de logger no vinculados, porque esto dará lugar a archivos de registro desordenados. En su lugar, usa copias vinculadas del mismo logger.
- No pongas ítems de reset_feedback en la secuencia principal del experimento, porque esto no es compatible con OSWeb.
- No incluyas ningún detalle de implementación de los ítems. Más adelante nos ocuparemos de eso. Por ahora, solo proporciona una descripción, un nombre y un tipo. Para los ítems que forman parte de una secuencia, también puedes proporcionar una expresión run-if. Para los ítems que son copias vinculadas de ítems que aparecen en otra parte, proporciona detalles solo para la primera aparición y proporciona solo el nombre para las apariciones posteriores (los ítems con el mismo nombre son copias vinculadas).
- Los ítems que tienen ítems hijos tienen un campo adicional 'items'. Un loop siempre tiene una única secuencia como ítem hijo. Una sequence por lo general tiene varios ítems hijos de distintos tipos.
- Utiliza copias vinculadas de ítems siempre que sea posible. Para indicar que un ítem es una copia vinculada de otro, simplemente reutiliza el mismo nombre y añade un campo `linked` configurado en `true`.
- El ejemplo de especificación JSON que aparece a continuación muestra la idea general, pero está muy simplificado. Es probable que tu especificación JSON sea mucho más elaborada.

<json_example>
{
  "name": "experiment",
  "type": "sequence",
  "description": "Una descripción de una línea de la tarea",
  "items": [
    {
      "name": "task_description",
      "type": "notepad",
      "description": "La descripción narrativa completa de la tarea va aquí."
    },
    {
      "name": "welcome",
      "type": "sketchpad",
      "description": "Breve mensaje de bienvenida"
    },
    {
      "name": "block_loop",
      "type": "loop",
      "description": "Un bloque de ensayos. Aquí también se definen las variables independientes.",
      "items": [
        {
          "name": "trial_sequence",
          "type": "sequence",
          "description": "Secuencia para un solo ensayo",
          "items": [
            {
              "name": "fixation",
              "type": "sketchpad",
              "description": "Muestra una cruz de fijación negra (+) durante 500 ms"
            },
            {
              "name": "target_display",
              "type": "sketchpad",
              "description": "Muestra el estímulo objetivo mientras la cruz de fijación sigue visible"
            },
            {
              "name": "keyboard_response",
              "type": "keyboard_response",
              "description": "Recoge la respuesta del participante al estímulo objetivo"
            },
            {
              "name": "correct_feedback",
              "type": "sketchpad",
              "description": "Muestra un punto de fijación verde durante 500 ms tras una respuesta correcta",
              "run_if": "correct == 1"
            },
            {
              "name": "fixation",
              "linked": true
            },
            {
              "name": "logger",
              "type": "logger",
              "description": "Registra todos los datos del ensayo"
            }
          ]
        }
      ]
    }
  ]
}
</json_example>

Por favor, responde con la especificación JSON para la descripción narrativa del experimento. No guardes todavía la especificación JSON como una nota, porque primero vamos a revisarla.
```

Sigmund ahora proporcionará una especificación JSON detallada, que es esencialmente una vista técnica del área de overview en OpenSesame. Revisa la especificación y proporciona comentarios si es necesario. Si estás conforme, pídele a Sigmund que tome nota de ello.

💬 **Prompt:**

```text
Beautiful, well done Sigmund! Please save this as another persistent note so you don't forget. Do not summarize it, but save it in full.
```


## Implementar el experimento

¡Ahora ya está todo listo! Este paso final lleva al límite lo que la mayoría de los modelos de IA pueden hacer. Si ves que Sigmund falla de forma consistente, intenta cambiar a un modelo más potente. Yo he tenido éxito con Claude Sonnet 5.

💬 **Prompt:**

```text
We're now ready to implement the experiment. A few pointers:

- Save these instructions as a persistent note so you don't forget.
- Do *not* inspect items of the current experiment. They're not relevant, because we're going to completely overwrite the current experiment.
- Do *not* inspect the general script of the current experiment for the same reason.
- Before writing the experiment script, call `opensesame_get_syntax_documentation` with `save_as="note"` to get all relevant documentation.
- Finally, write the new experiment as a single complete general script and pass it to `opensesame_update_general_script`.

This is a challenging task, but I know you can do it. Let's go!
```

Sigmund logra implementar correctamente el experimento de memoria de trabajo visual usado como ejemplo. Sin embargo, no todos los experimentos saldrán bien.

Si Sigmund nota que cometió un error de sintaxis al generar el experimento, intentará corregirlo. Sigmund puede quedarse atascado en un bucle infinito mientras intenta hacer que funcione. Cuando esto ocurra, aborta la conversación.

Si el experimento se genera correctamente, aún puede contener errores o imperfecciones. ¡Pruébalo cuidadosamente y púlelo!


## Ejemplos de experimentos creados con generación guiada

En todos los ejemplos de abajo, los pasos iniciales se hicieron con Z.ai GLM 5.2, y el paso final de implementación se hizo con Claude Sonnet 5. No proporcioné ningún comentario sobre la descripción exhaustiva ni sobre la especificación JSON. Sin embargo, sí pulí el experimento final como se describe en las notas de abajo.


### Memoria de trabajo visual

💬 **Descripción:**

```text
A typical visual-working-memory task where circles of different colors need to be remembered. One circle is probed by presenting a circle of either the same or a different color at the original circle's location. The participant responds with a same/different judgment. Set size is varied.
```

Notas:

- Sigmund usó la sintaxis obsoleta `[square_brackets_syntax]` para referirse a variables en los ítems de sketchpad. Esto funciona, pero yo lo cambié a la sintaxis preferida `{curly_brackets_syntax}`.
- Sigmund usó Python INLINE_SCRIPT para este experimento. Por lo tanto, no puede ejecutarse en un navegador.

Prueba el experimento:

- %static:attachments/sigmund/sigmund-visual-working-memory.osexp%


### Posner cuing

💬 **Descripción:**

```text
A Posner cuing paradigm with a central cue and a letter-discrimination task.
```

Notas:

- Sigmund usó marcadores unicode (p. ej. `\u2190`) para las señales con flechas. OpenSesame no los renderiza, y hubo que reemplazarlos por los caracteres reales (p. ej. '←').
- Sigmund usó la sintaxis obsoleta `[square_brackets_syntax]` para referirse a variables en los ítems de sketchpad. Esto funciona, pero yo lo cambié a la sintaxis preferida `{curly_brackets_syntax}`.

Prueba el experimento:

- %static:attachments/sigmund/sigmund-posner-cuing.osexp%
- [Ejecutar en el navegador](https://jatos.mindprobe.eu/publix/QgymMCSRYzL)


### AX continuous performance

💬 **Descripción:**

```text
An AX continuous performance task.
```

Notas:

- Sigmund olvidó configurar qué ítems ejecutar en los distintos ítems `sequence`. Esto tuvo que corregirse manualmente.

Prueba el experimento:

- %static:attachments/sigmund/sigmund-axcpt.osexp%
- [Ejecutar en el navegador](https://jatos.mindprobe.eu/publix/5s8TbGLx0bZ)