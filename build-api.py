import inspect
import textwrap
import sys
from numpydoc import docscrape
from pathlib import Path


def dedent_docstring(docstring):
    if '\n' not in docstring:
        return docstring
    firstline, rest = docstring.expandtabs(4).split('\n', 1)
    return firstline.lstrip() + '\n' + textwrap.dedent(rest)


def docstring_to_markdown(docstring):
    if '{nodoc}' in docstring:
        return
    docstring = dedent_docstring(docstring)
    parsed_docstring = docscrape.NumpyDocString(docstring)
    summary = parsed_docstring['Summary'] + [''] + \
        parsed_docstring['Extended Summary']
    if not summary:
        return
    md = "\n".join(summary) + "\n\n"

    if parsed_docstring['Parameters']:
        md += "__Parameters__\n\n"
        for name, type_, desc in parsed_docstring['Parameters']:
            name = name.replace('*', r'\*')
            desc = '\n'.join(desc)
            md += f"- **{name}**: {desc}\n"

    if parsed_docstring['Returns']:
        md += "\n__Returns__\n\n"
        for name, type_, desc in parsed_docstring['Returns']:
            desc = '\n'.join(desc)
            md += f"- {desc}\n"
            
    if parsed_docstring['Examples']:
        examples = parsed_docstring['Examples']
        if examples[0].startswith('>>>'):
            examples = [line[4:] for line in examples]
            example = '\n'.join(examples)
            md += f"\n__Example__\n\n~~~ .python\n{example.strip()}\n~~~\n\n"
        else:
            example = '\n'.join(examples)
            md += f"\n__Example__\n\n{example.strip()}\n\n"
            
    return md


def generate_markdown_docs(obj, name=None, descriptor=None):
    methods = inspect.getmembers(obj, predicate=inspect.isfunction)
    md = '<div class="ClassDoc YAMLDoc" markdown="1">\n\n'
    if name is None:
       name = obj.__name__
    if descriptor is None:
        descriptor = 'class'
    if isinstance(obj, type):
        md += f"# {descriptor} __{name}__\n\n"
        md += docstring_to_markdown(obj.__doc__)
    for method_name, method in methods:
        if method_name.startswith('_') or method.__doc__ is None:
            continue
        npdoc = docstring_to_markdown(method.__doc__)
        if npdoc is None:
            continue
        # Get the function signature but remove self as the first argument
        method_sig = str(inspect.signature(method)).replace('self, ', '') \
            .replace('*', r'\*')
        if method_sig == 'self':
            method_sig = ''
        md += f"## {method_name}{method_sig}\n\n{npdoc}\n\n"
    return md + '</div>\n\n'


def gendoc(obj, path, name=None, descriptor=None):
    root = Path('include/api')
    Path(root / path).write_text(generate_markdown_docs(obj, name, descriptor))


sys.path.append('/home/sebastiaan/git/OpenSesame')
# sys.path.append('/home/sebastiaan/git/PyGaze')
from opensesame_plugins.core.joystick._libjoystick.basejoystick import BaseJoystick
gendoc(BaseJoystick, 'joystick.md', 'joystick', descriptor='instance')
from opensesame_plugins.core.srbox.libsrbox import LibSrbox
gendoc(LibSrbox, 'srbox.md', 'srbox', descriptor='instance')
from libopensesame.var_store import VarStore
gendoc(VarStore, 'var.md', 'var', descriptor='instance')
from libopensesame.file_pool_store import FilePoolStore
gendoc(FilePoolStore, 'pool.md', 'pool', descriptor='instance')
from libopensesame.item_store import ItemStore
gendoc(ItemStore, 'items.md', 'items', descriptor='instance')
from libopensesame.response_store import ResponseStore
gendoc(ResponseStore, 'responses.md', 'responses', descriptor='instance')
from libopensesame import python_workspace_api
gendoc(python_workspace_api, 'python_workspace_api.md')
from openexp._canvas.canvas import Canvas
gendoc(Canvas, 'canvas.md')
from openexp._sampler.sampler import Sampler
gendoc(Sampler, 'sampler.md')
from openexp._keyboard.keyboard import Keyboard
gendoc(Keyboard, 'keyboard.md')
from openexp._mouse.mouse import Mouse
gendoc(Mouse, 'mouse.md')
from openexp._clock.clock import Clock
gendoc(Clock, 'clock.md', 'clock', descriptor='instance')
from openexp._log.log import Log
gendoc(Log, 'log.md', 'log', descriptor='instance')
from libopensesame.widgets._form import Form
# gendoc(Form, 'form.md')
# from libopensesame.widgets._button import Button
# gendoc(Button, 'button.md')
# from libopensesame.widgets._image import Image
# gendoc(Image, 'image.md')
# from libopensesame.widgets._image_button import ImageButton
# gendoc(ImageButton, 'image_button.md')
# from libopensesame.widgets._checkbox import Checkbox
# gendoc(Checkbox, 'checkbox.md')
# from libopensesame.widgets._rating_scale import RatingScale
# gendoc(RatingScale, 'rating_scale.md')
# from libopensesame.widgets._label import Label
# gendoc(Label, 'label.md')
# from libopensesame.widgets._text_input import TextInput
# gendoc(TextInput, 'text_input.md')
