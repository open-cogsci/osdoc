title: Access experimental variables

<summary_prompt>
Write a summary for the API below:

- Describe the API's overall functionality
- Explain that this is a Python API for OpenSesame, software for implementing psychology experiments
- Explain that the `var` object does not need to be imported
- Explain that there are two ways to refer to experimental variables:
    - Preferred: as global variables: (`my_var = 10`)
    - Non-preferred: as properties of the `var` object (`var.my_var = 10`)
- Provide a bulleted list of all available functions and their parameters. Important: Don't just name the functions, but create one bullet per function.

Your response should be a comprehensive summary.

```markdown
{content}
```
</summary_prompt>

%-- include: include/api/var.md --%
