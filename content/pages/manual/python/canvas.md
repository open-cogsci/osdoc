title: Canvas functions

<summary_prompt>
Write a summary for the API below:

- Describe the API's overall functionality
- Explain that this is a Python API for OpenSesame, software for implementing psychology experiments
- Explain that `Canvas` and Element classes do not need to be imported
- Explain the process to initialize a `Canvas`
- Discuss three methods of drawing elements:
    - Naming an Element interface (`my_canvas['name'] = FixDot()`)
    - Adding an Element interface (`my_canvas += FixDot()`)
    - Not preferred: function interface (`my_canvas.fixdot()`)
- Illustrate how to modify named elements with an example
- Define the usage of `**style_args`
- Explain how to specify colors
- Explain coordinates: x=0, y=0 is the display center
- Provide a bulleted list of all available functions and their parameters. Important: Don't just name the functions, but create one bullet per function.

Your response should be a comprehensive summary.

```markdown
{content}
```
</summary_prompt>

%-- include: include/api/canvas.md --%
