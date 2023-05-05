title: Haciendo cosas en secuencia
hash: 15313148d00600657d102430c4e197e7a888d543ca35e349a350210120cb1e11
locale: es
language: Spanish

El elemento SEQUENCE tiene dos funciones importantes:

- Ejecuta varios otros elementos uno tras otro.
- Determina qué elementos deben ejecutarse y cuáles no.

Las SEQUENCEs se ejecutan de arriba hacia abajo; es decir, el elemento en la parte superior se ejecuta primero. El orden de una SEQUENCE siempre es secuencial.

## Expresiones run-if

Puedes usar expresiones run-if para determinar si un elemento en particular debe ejecutarse o no. Por ejemplo, si deseas que una pantalla se presente solo si un participante ha realizado una respuesta incorrecta, puedes establecer las expresiones run-if para ese elemento en:

```python
{correct} == 0
```

Si dejas las expresiones run-if vacías o ingresas `True`, el elemento siempre se ejecutará. Las expresiones run-if utilizan la misma sintaxis que otras expresiones condicionales. Para obtener más información, consulta:

- %link:manual/variables%

Las expresiones run-if solo afectan qué elementos se ejecutan, no cuáles se preparan. Dicho de otro modo, la fase de preparación de todos los elementos en una SEQUENCE siempre se realiza, independientemente de las expresiones run-if. Consulta también:

- %link:prepare-run%


## Deshabilitar elementos

Para deshabilitar completamente un elemento en una SEQUENCE, haz clic derecho sobre él y selecciona 'Deshabilitar'. Esto es especialmente útil durante el desarrollo de tu experimento, por ejemplo, para omitir temporalmente las instrucciones.