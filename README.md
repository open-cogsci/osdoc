# OpenSesame documentation area

Copyright 2010-2014
Sebastiaan Mathôt <s.mathot@cogsci.nl>

## About

This repository contains the source for <http://osdoc.cogsci.nl/>.

## Format

All files are formatted with Markdown syntax, and are compiled using [Kramdown][] or (for the newer pages) [academicmarkdown][]. [Jekyll][] is used to generate the site structure. For documentation, see the respective homepages of these tools.

The site content is available in the folder `content`.

- [academicmarkdown]: https://github.com/smathot/academicmarkdown
- [kramdown]: http://kramdown.rubyforge.org/
- [jekyll]: https://github.com/mojombo/jekyll

## Important files and folders

- `sitemap.txt` contains the site structure.
- `versions.yml` contains a description of all branches of the documentation. Each branch corresponds to a different documentation site, and lives in a different git branch of the repository.
- `content/*` contains the site content.

## Site generation

To generate the full documentation site for the currently active branch, run:

	python generate.py

This will generate the site in the folder `_site/[branch]`. The status of the current branch is read from `versions.yml`.

To quickly generate the site, while skipping PDF generation and optimization:

	python compile.py

## Dependencies

Most dependencies are available from the Ubuntu repositories or from the [Cogsci.nl PPA](https://launchpad.net/~smathot/+archive/cogscinl/). Only [`htmlcompressor.jar`](https://code.google.com/p/htmlcompressor/) and [`yui-compressor.jar`](https://github.com/yui/yuicompressor/downloads) must be downloaded from their respective websites and manually placed in the osdoc source folder.

	jekyll
	python-academicmarkdown
	python-yaml
	kramdown
	node-less
	linkchecker         # Optional, for checking for dead links
	htmlcompressor.jar  # Optional, for compressing HTML
	yuicompressor		# Optional, for compressing HTML

## License information

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OpenSesame documentation area</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://osdoc.cogsci.nl" property="cc:attributionName" rel="cc:attributionURL">Sebastiaan Mathôt</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">Creative Commons Attribution 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/smathot/osdoc" rel="dct:source">https://github.com/smathot/osdoc</a>.
