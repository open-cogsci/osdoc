# OpenSesame documentation area

Copyright 2010-2016

Sebastiaan Mathôt <s.mathot@cogsci.nl>

## About

This repository contains the source for <http://osdoc.cogsci.nl/>.

## Format

All files are formatted with Markdown syntax, supplemented with [academicmarkdown][].

## Important files and folders

- `sitemap.yaml` contains the site structure used to generate the menu.
- `versions.yml` contains a description of all branches of the documentation. Each branch corresponds to a different documentation site, and lives in a different git branch of the repository.
- `content/pages/` contains the site content.

## Site generation

To regenerate the menu file, run:

	python3 build-menu.py

To regenerate the Python API docs, run (see the source for assumptions about where OpenSesame and PyGaze are located):

	python3 build-api.py

Finally, to generate the site, run:

	pelican

This will generate the site in the folder `output`.

## Dependencies

Most dependencies are available from the Ubuntu repositories or from the [Cogsci.nl PPA][]. Only [htmlcompressor.jar][] and [yui-compressor.jar][] must be downloaded from their respective websites and manually placed in the osdoc source folder.

	pelican
	pyyaml
	htmlmin
	python-academicmarkdown
	python-yamldoc
	linkchecker         # Optional, for checking for dead links
	htmlcompressor.jar  # Optional, for compressing HTML
	yuicompressor		# Optional, for compressing HTML

## License information

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OpenSesame documentation area</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://osdoc.cogsci.nl" property="cc:attributionName" rel="cc:attributionURL">Sebastiaan Mathôt</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">Creative Commons Attribution 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/smathot/osdoc" rel="dct:source">https://github.com/smathot/osdoc</a>.

[academicmarkdown]: https://github.com/smathot/academicmarkdown
[kramdown]: http://kramdown.rubyforge.org/
[jekyll]: https://github.com/mojombo/jekyll
[cogsci.nl ppa]: https://launchpad.net/~smathot/+archive/cogscinl/
[htmlcompressor.jar]: https://code.google.com/p/htmlcompressor/
[yui-compressor.jar]: https://github.com/yui/yuicompressor/downloads
