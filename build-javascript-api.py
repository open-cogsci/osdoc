# coding=utf-8
import os
import re


def parse_javascript_api():

    for basename in ['canvas.md', 'javascript_workspace_api.md']:
        with open(os.path.join('include/javascript-api', basename)) as fd:
            md = fd.read()
        md = re.sub(r'\*\*Kind\*\*:.*', '', md)
        needle = '### new Canvas()\n'
        if md.find(needle) >= 0:
            md = md[md.find(needle) + len(needle):]  # strip the headers
        needle = '<a name="reset_feedback"></a>'
        if md.find(needle) >= 0:
            md = md[md.find(needle) + len(needle):]  # strip the headers
        md = md.replace('new Canvas()', 'Canvas()')
        with open(os.path.join('include/javascript-api', basename), 'w') as fd:
            fd.write(md)


if __name__ == '__main__':
    parse_javascript_api()
