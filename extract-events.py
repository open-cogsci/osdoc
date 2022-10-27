import re
from pathlib import Path

pattern = r'extension_manager.fire\(u?[\'"](?P<event>\w+)[\'"].*?\)'
events = {}
for src in ('/home/sebastiaan/git/OpenSesame/libqtopensesame',
            '/home/sebastiaan/git/rapunzel/opensesame_extensions'):
    for path in Path(src).rglob('*.py'):
        with open(path) as fd:
            code = fd.read()
        for match in re.finditer(pattern, code, re.DOTALL | re.MULTILINE):
            event = match['event']
            call = match.group(0)
            if event not in events:
                events[event] = []
            events[event].append((path, call))
with open('include/events.md', 'w') as fd:
    for event in sorted(events.keys()):
        fd.write(f'### {event}\n\n')
        for path, call in events[event]:
            url = str(path) \
                .replace('/home/sebastiaan/git/rapunzel', 'https://github.com/open-cogsci/rapunzel/blob/master') \
                .replace('/home/sebastiaan/git/OpenSesame', 'https://github.com/open-cogsci/OpenSesame/blob/master')
            fd.write(f'Fired in: [{Path(path).name}]({url})\n\n')
            fd.write(f'```python\n{call}\n```\n\n')
