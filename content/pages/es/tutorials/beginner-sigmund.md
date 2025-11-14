title: Tutorial de SigmundAI: señalización de la mirada
hash: 80f0a9ae4381f62b46aa6b1cca4b807990e8235070ac5187f47bc98a6f028d00
locale: es
language: Spanish

[TOC]


## Sobre este tutorial

En este tutorial, construirás un experimento de psicología colaborando con SigmundAI, tu copiloto de IA para OpenSesame. Aprenderás a dar instrucciones claras a Sigmund, detectar y corregir errores, y crear experimentos más rápido que nunca.

Crearemos un experimento clásico de orientación de la mirada. Es un paradigma divertido e interesante, donde las personas no pueden evitar seguir hacia donde mira una cara.

Este tutorial se basa en [el tutorial para principiantes](%url:beginner%), usando el mismo experimento, pero mostrándote cómo crearlo con asistencia de IA.


## Qué aprenderás

Al finalizar este tutorial, sabrás cómo:

- 💡 Darle a Sigmund instrucciones claras y efectivas
- 💡 Dividir tareas complejas en pasos sencillos
- 💡 Detectar y corregir los errores de Sigmund (sí, ¡la IA se equivoca!)
- 💡 Crear la estructura de experimentos rápidamente
- 💡 Trabajar eficientemente con un copiloto de IA


## Lo que necesitarás

**OpenSesame 4.1 o posterior** con todas las actualizaciones instaladas. Si ves una notificación sobre actualizaciones disponibles, haz clic en "Instalar actualizaciones..." y luego en "Ejecutar script de actualización." Reinicia OpenSesame después de actualizar. También puedes actualizar manualmente ejecutando el siguiente comando en la consola de OpenSesame.

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

**Conocimientos básicos de OpenSesame.** ¿Nuevo en OpenSesame? Comienza primero con el [tutorial para principiantes](%url:beginner%). Comprender lo básico te ayudará a colaborar efectivamente con Sigmund. La IA es poderosa, pero no reemplaza entender cómo funcionan las cosas.

**Una suscripción a SigmundAI.** Necesitarás una suscripción activa en [sigmundai.eu](https://sigmundai.eu/).


## Conectando OpenSesame a Sigmund

Sigmund es un asistente de IA diseñado específicamente para OpenSesame. A diferencia de chatbots generales como ChatGPT, Sigmund:

- Conoce OpenSesame a la perfección
- Funciona directamente dentro de la interfaz de OpenSesame
- Puede hacer cambios en tu experimento automáticamente

Para conectar, simplemente inicia sesión en [sigmundai.eu](https://sigmundai.eu). El panel de Sigmund en OpenSesame se conectará automáticamente:

<video controls width="100%">
  <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>


## El experimento

Como se mencionó, crearemos un experimento de orientación de la mirada, desarrollado originalmente por [Friesen y Kingstone (1998)][references]. Así es como funciona:

1. Aparece una cara en el centro de la pantalla
2. La cara mira hacia la izquierda o derecha
3. Una letra objetivo ('F' o 'H') aparece en un lado
4. Una letra distractora ('X') aparece en el otro lado
5. Los participantes identifican la letra objetivo lo más rápido posible

¿El hallazgo interesante? Las personas son más rápidas cuando la cara mira hacia el objetivo, ¡aunque la dirección de la mirada no predice dónde aparecerá el objetivo! Esto demuestra que los humanos siguen automáticamente la mirada de otros.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  El paradigma de orientación de la mirada [(Friesen y Kingstone, 1998)][references]. Este ejemplo muestra un ensayo **incongruente**, porque la cara mira al distractor ('X') en lugar del objetivo ('F').
--%


## Paso 1: Crear la secuencia principal

Comencemos construyendo la estructura básica. El experimento tiene dos fases: práctica y experimental. Cada fase necesita instrucciones antes y un mensaje después. Comenzar con una estructura clara ayuda tanto a ti como a Sigmund a mantener el orden.

¡Al hablar con Sigmund, sé específico! Indícale exactamente lo que deseas, y también lo que *no* deseas aún. Esto previene que Sigmund haga demasiado de una sola vez.

💬 **Pregunta:**

```text
¡Hola Sigmund! Me gustaría construir juntos un experimento de orientación de la mirada. Comencemos con la estructura básica:

- experiment (sequence)
  - instructions (form_text_display)
  - practice_loop (loop)
    - block_sequence (sequence)
  - end_of_practice (form_text_display)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_of_experiment (form_text_display)
```

Por favor, crea esta estructura pero aún no agregues contenido a los elementos. ¡Lo haremos paso a paso!
```

Después de que Sigmund cree esta estructura, vamos a limpiar las cosas. Hazlo en una solicitud aparte para no abrumar a Sigmund con demasiadas tareas al mismo tiempo.

💬 **Sugerencia:** 

```text
¡Genial! Ahora, por favor elimina cualquier elemento que no necesitemos y ponle un título claro al experimento.
```

Tu área de resumen debería verse como %FigStep1. (El título de tu experimento podría ser un poco diferente. ¡Eso está bien!)

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  La área de resumen al final del Paso 1.
--%


<div class='info-box' markdown='1'>

**💡 ¡Mantén a Sigmund bajo control!**

Al final del panel de Sigmund, puedes elegir si quieres revisar las acciones de Sigmund antes de que sucedan. Cuando está activado, aprobarás cada cambio que haga Sigmund.

- **Para aprender:** Mantén esto ACTIVADO. Así entenderás lo que hace Sigmund.
- **Para velocidad:** Desactiva esto cuando te sientas cómodo.

¡Recuerda que Sigmund comete errores! Siempre revisa los resultados, especialmente al principio.

</div>


## Paso 2: Crea la secuencia de bloques

Ahora vamos a construir lo que sucede en cada bloque de ensayos. Cada bloque sigue este patrón:

1. Restablece la retroalimentación (para que el desempeño en los bloques previos no afecte la retroalimentación en el actual)
2. Ejecuta un bucle de ensayos
3. Muestra la retroalimentación sobre el desempeño

Las fases de práctica y experimental usan el mismo elemento *block_sequence*. Esto se llama una copia vinculada. Cuando cambias uno, el otro también cambia. Usar copias vinculadas es conveniente cuando la misma funcionalidad (como un bloque de ensayos) ocurre en varios lugares de tu experimento.

💬 **Sugerencia:**

```text
¡Perfecto! Ahora agreguemos contenido a block_sequence. Este debe ser compartido entre la fase de práctica y la experimental (una copia vinculada). Estructúralo así:

- block_sequence (sequence)
  - reset_feedback (reset_feedback)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)

Nuevamente, solo crea la estructura. Agregaremos contenido después. ¿Listo? ¡Vamos!
```

Tu área de resumen debería verse ahora como %FigStep2.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  El área de resumen al final del Paso 2.
--%


## Paso 3: Define las condiciones de los ensayos

Todo experimento tiene variables independientes. Esas son las cosas que vas a manipular. En nuestro experimento, variamos:

- Hacia dónde mira la cara (izquierda o derecha)
- Dónde aparece el objetivo (izquierda en -300, o derecha en 300)
- Qué letra es el objetivo (F o H)

También necesitamos calcular:

- Dónde va el distractor (lado opuesto al objetivo)
- Cuál es la tecla de respuesta correcta (z para F, m para H)

Esto crea un diseño 2 × 2 × 2 = 8 tipos de ensayo diferentes.

Al explicarle el diseño a Sigmund, le ayudamos a entender la lógica y a crear todas las combinaciones correctas.

💬 **Sugerencia:**

```text
Ahora definamos las variables en block_loop. Es un diseño 2 × 2 × 2 (total 8 filas):

- gaze_cue: left o right
- target_pos: -300 o 300 (coordenada x, negativo = izquierda, 0 = centro)
- target_letter: F o H
- dist_pos: opuesto a target_pos
- correct_response: z cuando target_letter es F, m cuando target_letter es H

¿Puedes crearlo? ¡Gracias!
```

Tu *block_loop* debería verse ahora como %FigStep3, con 8 filas mostrando todas las combinaciones posibles.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "El *block_loop* al final del Paso 3."
--%


<div class='info-box' markdown='1'>

**🤖 ¡Elige un modelo de IA que te funcione!**

Sigmund no es una sola IA. Es un chatbot que puede usar diferentes modelos de IA. En [sigmundai.eu](https://sigmundai.eu), puedes seleccionar entre varios modelos.

Este tutorial fue probado con **Claude Sonnet 4.5** y **GPT-5**, ambos en modo de conversación.

Consejos:

- Diferentes modelos tienen diferentes fortalezas. Experimenta para encontrar tu favorito.
- Los modelos de resolución de problemas son más lentos y no siempre son mejores para tareas sencillas.

</div>


## Paso 4: Agrega imágenes y sonidos al pool de archivos

Necesitamos algunos archivos para nuestros estímulos:

- Imágenes de una cara mirando de forma neutral, hacia la izquierda y hacia la derecha
- Un sonido para reproducir cuando los participantes cometen un error

Sigmund no puede descargar archivos por ti, así que tendrás que hacer esta parte manualmente. Descarga los archivos a continuación y arrástralos a tu grupo de archivos:

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

el grupo de archivos debe verse como %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%


## Paso 5: Construir la secuencia de ensayo

Es hora de crear la estructura de un solo ensayo. Esto es lo que sucede en cada ensayo:

1. Mostrar un punto de fijación (¡prepárate!)
2. Mostrar la cara neutral (aquí viene la cara)
3. Mostrar la indicación de la mirada (la cara mira a la izquierda o a la derecha)
4. Mostrar el objetivo y el distractor (¡hora de responder!)
5. Registrar la respuesta del teclado
6. Reproducir el sonido de error (solo si la respuesta fue incorrecta)
7. Registrar los datos

El sonido de error solo debe reproducirse en los ensayos incorrectos. Esto utiliza una expresión "run-if": una condición que determina cuándo se ejecuta un ítem.

💬 **Sugerencia:**

```text
Agreguemos ítems a la trial_sequence:

- fixation_dot (sketchpad)
- neutral_gaze (sketchpad)
- gaze_cue (sketchpad)
- target (sketchpad)
- keyboard_response (keyboard_response)
- incorrect_sound (sampler) — solo se reproduce tras una respuesta incorrecta
- logger (logger)

Solo crea los ítems por ahora, aún no agregues contenido. ¿Puedes hacerlo?
```

Esta tarea requiere muchas acciones y Sigmund a veces se confunde. Asegúrate de revisar su trabajo cuidadosamente.

Errores comunes que comete Sigmund aquí:

- Olvidar crear algunos de los ítems
- Olvidar agregar la expresión run-if para *incorrect_sound*

%--
figure:
 id: FigSigMistake
 source: sigmund-makes-mistake.png
 caption: "Oops! Sigmund forgot to add a logger and to define a run-if expression for incorrect_sound."
--%

Si Sigmund cometió un error (como olvidar el logger o la expresión run-if), dale un recordatorio amable con instrucciones específicas:

💬 **Sugerencia** (ajusta según lo que falte):

```text
Noto que falta el logger. ¿Podrías agregarlo por favor?

Y después, ¿podrías seleccionar la trial_sequence y agregar una expresión run-if para el incorrect_sound sampler? Recuerda, las expresiones run-if se configuran en la secuencia que contiene el ítem, no en el ítem en sí.
```

¿Por qué Sigmund comete errores? La IA es impredecible, lo que significa que los errores pueden ocurrir en cualquier tarea. Sin embargo, a Sigmund le cuesta especialmente en tareas de varios pasos. ¡La tarea anterior requería 9 acciones separadas! Cuando pidas tareas complejas, revisa siempre los resultados.

Tu *trial_sequence* debe verse como %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%


## Paso 6: Dibuja los ítems de visualización

¡Ahora viene la parte divertida: crear lo que verán los participantes! Revisaremos cada visualización una por una.

Primero, configuremos los colores y dibujemos el punto de fijación inicial. Nuestros estímulos de mirada usan un fondo blanco, así que necesitamos un fondo blanco con elementos en negro.

💬 **Sugerencia:**

```text
¿Podrías cambiar los ajustes del experimento para usar estímulos negros sobre fondo blanco? Luego, agrega un punto de fijación al ítem fixation_dot y ajusta su duración a 745 ms.
```

Ahora, la visualización de la cara neutral:

💬 **Sugerencia:**

```text
¡Genial! Ahora agrega la imagen de la mirada neutral. La duración debe ser de 745 ms.
```

Sigmund debería haberse dado cuenta de usar el archivo *gaze_neutral.png* del grupo de archivos. ¡Revisa el sketchpad para verificar!

Ahora la indicación de la mirada (hacia dónde mira la cara):

💬 **Sugerencia:**

```text
¡Perfecto! Ahora agrega la visualización de la indicación de la mirada. Debe mostrarse durante 495 ms.
```

Sigmund debería usar la variable `gaze_cue` para mostrar *gaze_left.png* o *gaze_right.png*.

Finalmente, la visualización del objetivo (la más compleja):

💬 **Sugerencia:**

```text
¡Excelente! Ahora crea la pantalla del objetivo. Debe mostrar:

- La pista de mirada (rostro sigue mirando)
- La letra objetivo a la izquierda o derecha (según target_pos)
- Una 'X' en el lado opuesto
```

La duración debe ser 0 porque el elemento *keyboard_response* viene a continuación y esperará una respuesta. ¡Verifica que Sigmund haya hecho esto correctamente!


## Paso 7: Configura la respuesta del teclado

Ahora necesitamos recopilar las respuestas de los participantes.

💬 **Indicación:**

```text
Por favor, configura el keyboard_response con un tiempo límite de 2000 ms. Solo acepta las teclas de respuesta correctas (z y m).
```


## Paso 8: Configura el sonido de error

Cuando los participantes cometan errores, deben escuchar una retroalimentación.

💬 **Indicación:**

```text
Ahora configura el incorrect_sound sampler para reproducir el archivo de sonido de error.
```


## Paso 9: Crea la pantalla de retroalimentación

Después de cada bloque, los participantes deben ver cómo les está yendo.

💬 **Indicación:**

```text
Agrega retroalimentación al elemento feedback mostrando la precisión promedio y el tiempo de respuesta del bloque.
```


## Paso 10: Establece las repeticiones de los bloques

Ahora necesitamos especificar cuántas veces repetir cada bloque.

💬 **Indicación:**

```text
Establece la fase de práctica en 2 bloques y la fase experimental en 8 bloques. También crea una variable 'practice' (sí o no) para distinguir las pruebas de práctica de las experimentales en nuestros datos.
```


## Paso 11: Escribe las pantallas de instrucciones

¡Los participantes deben saber qué hacer! Pidamos a Sigmund que escriba instrucciones claras.

💬 **Indicación:**

```text
Por favor, redacta instrucciones claras y concisas para el experimento, además de mensajes útiles al final de la práctica y al final del experimento. ¡Usa tu criterio para el contenido!
```

Lee las instrucciones. ¿Tienen sentido? ¿Son claras? ¡No dudes en pedirle a Sigmund que las revise si es necesario!


## Paso 12: ¡Prueba y depura!

Ha llegado el momento de la verdad. ¡Ejecuta el experimento! Presiona el botón azul de ejecución rápida y observa qué sucede. ¡Puede que aparezca un error! Esto es completamente normal. Puede aparecer el siguiente error:

%--
figure:
 id: FigFStringError
 source: fstringerror.png
 caption: "An error appears. Don't panic!"
--%

¿Qué está pasando? El elemento end-of-practice intenta mostrar la variable `acc` antes de que exista. Esto ocurre debido a las fases de preparación-ejecución de OpenSesame: los elementos se preparan por adelantado y, a veces, las variables aún no se han definido en ese momento.

Sigmund normalmente puede solucionar estos problemas. Simplemente haz clic en "Ask Sigmund to fix this" cuando aparezca el error. Una vez solucionado, intenta ejecutar el experimento de nuevo. Repite el proceso si es necesario.

¡Listo! Felicidades. ¡Has creado un experimento completo con Sigmund!

💬 **Indicación final:**

```text
¡Gracias Sigmund! ¡Excelente trabajo!
```


## Puntos clave

¡Aprendiste a trabajar eficazmente con un copiloto de IA! Aquí tienes las lecciones principales:

- ✅ **Sé específico y claro** en tus indicaciones.
- ✅ **Divide tareas complejas en pasos simples**. No pidas demasiado de una sola vez.
- ✅ **Siempre revisa el trabajo de Sigmund**. ¡La IA comete errores!
- ✅ **Haz preguntas de seguimiento** cuando algo no esté bien.
- ✅ **Sé paciente**. La depuración es parte del proceso.

¡Con práctica, tú y Sigmund serán un gran equipo! 🤝


## Referencias

<div class='reference' markdown='1'>

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

</div>

[references]: #references