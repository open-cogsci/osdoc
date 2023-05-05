title: Cuestionarios en OSWeb
hash: f6b463450c96aa0d178ca2cfac0c799d7e678cfdfc3dec34f7ef88f57e8a8fe1
locale: es
language: Spanish

## Formularios y HTML personalizado

Los formularios y HTML personalizado están soportados a partir de OSWeb 1.4
{:.page-notification}

Puede utilizar los complementos de formulario como se describe aquí:

- %link:manual/forms/about%

El complemento FORM_BASE *no* es compatible con OSWeb. En su lugar, puede utilizar el elemento INLINE_HTML para implementar formularios HTML personalizados, como se describe aquí:

- %link:manual/forms/html%


## Enlazando a una plataforma diferente

Como alternativa, puede implementar un cuestionario utilizando otra plataforma, como [LimeSurvey](https://www.limesurvey.org/), y luego enlazar a este cuestionario desde su experimento OSWeb. El siguiente video muestra cómo hacer esto de tal manera que pueda saber después qué datos del cuestionario pertenecen a qué datos de OSWeb.

%--
video:
 source: youtube
 id: BeginnerTutorial
 videoid: 1WvTUQr0JL0
 width: 640
 height: 360
 caption: |
  Combinando OSWeb y LimeSurvey.
--%