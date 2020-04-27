# OpenSesame documentation area

Copyright 2010-2020

Sebastiaan Mathôt <s.mathot@cogsci.nl>

## About

This repository contains the source for <http://osdoc.cogsci.nl/>.

## Format

All files are formatted with Markdown syntax, supplemented with [academicmarkdown][].

## Style

- Write item types in uppercase: *SKETCHPAD* (This is automatically parsed and styled.)
- Write item names in italics: `*new_sketchpad*`
- Write backend names in italics: `*psycho*`
- Do not hyphenate 'backend' or 'plugin'
- Capitalize 'Run phase' and 'Prepare phase'

## Important files and folders

- `sitemap.yaml` contains the site structure used to generate the menu.
- `versions.yml` contains a description of all branches of the documentation. Each branch corresponds to a different documentation site, and lives in a different git branch of the repository.
- `content/pages/` contains the site content.

## Site generation

To generate the site for local testing:

	python3 build-menu.py # optional, to regenerate the menu
	python3 build-api.py # optional, to regenerate the Python api
	pelican -s pelicanconf.py

Or, to generate the site for publication, run:

	python3 build-menu.py --publish
	python3 build-api.py # optional, to regenerate the Python api
	pelican -s publishconf.py

This will generate the site in the folder `output`.

## Previewing

Once the site has been generated, open a terminal in the `output` folder and start a basic webserver to view it:

	python -m SimpleHTTPServer

You can now visit `http://localhost:8000` in a browser to view the site, which will be in a subfolder, e.g. `http://localhost:8000/3.1`

## Dependencies

- pelican
- inkscape (used for converting svg to png)
- python-academicmarkdown
- python-yamldoc

To install these on Ubuntu 16.04:

	sudo apt-get install pelican inkscape
	pip install python-academicmarkdown python-yamldoc

## License information

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OpenSesame documentation area</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://osdoc.cogsci.nl" property="cc:attributionName" rel="cc:attributionURL">Sebastiaan Mathôt</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">Creative Commons Attribution 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/smathot/osdoc" rel="dct:source">https://github.com/smathot/osdoc</a>.

[academicmarkdown]: https://github.com/smathot/academicmarkdown
[kramdown]: http://kramdown.rubyforge.org/
[jekyll]: https://github.com/mojombo/jekyll
[cogsci.nl ppa]: https://launchpad.net/~smathot/+archive/cogscinl/
[htmlcompressor.jar]: https://code.google.com/p/htmlcompressor/
[yui-compressor.jar]: https://github.com/yui/yuicompressor/downloads
