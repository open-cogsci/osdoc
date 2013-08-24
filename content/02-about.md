---
layout: osdoc
title: About
group: General
permalink: /about/
level: 0
sortkey: 002.001
singleton: true
---

OpenSesame is a graphical, open-source experiment builder for the social sciences. It sports a modern and intuitive user interface that allows you to build complex experiments with a minimum of effort. With OpenSesame you can create a wide range of experiments. The [plug-in framework][plug-ins] and [Python scripting][python-scripting] allow you to incorporate [external devices][external-devices], such as eye trackers, response boxes, and parallel port devices, into your experiment.

OpenSesame is freely available under the [General Public Licence][gpl].

![](/img/fig/fig1.2.1.png)

The team
--------

OpenSesame is developed by a loose collection of individuals. Anyone is welcome to join the team of regular contributors.

<table class="no-table-border">
	<tr>
		<td>
			<img src="/img/team/sebastiaan.png" />
		</td>
		<td>
			{% capture sebastiaan %}{% include team/sebastiaan.md %}{% endcapture %}
			{{ sebastiaan | markdownify }}
		</td>
	</tr>
	<tr>
		<td>
			<img src="/img/team/daniel.png" />
		</td>
		<td>
			{% capture daniel %}{% include team/daniel.md %}{% endcapture %}
			{{ daniel | markdownify }}
		</td>
	</tr>
	<tr>
		<td>
			<img src="/img/team/lotje.png" />
		</td>
		<td>
			{% capture lotje %}{% include team/lotje.md %}{% endcapture %}
			{{ lotje | markdownify }}
		</td>
	</tr>
	<tr>
		<td>
			<img src="/img/team/edwin.png" />
		</td>
		<td>
			{% capture edwin %}{% include team/edwin.md %}{% endcapture %}
			{{ edwin | markdownify }}
		</td>
	</tr>
</table>

Acknowledgements
----------------

Many thanks go out to Jan Theeuwes, Wouter Kruijne, Jarik den Hartog, Cor Stoof, the entire Department of Cognitive Psychology at the VU University, Jonathan Grainger, Françoise Vitu, Eric Castet, the rest of the people at the LPC in Marseille, and Andrea Epifani.

We would like to thank [SR Research][sr-research] for their generous support.

OpenSesame is powered by the following libraries (and many more). Credits go out to the respective authors:

- [Python][]
- [Qt4][]
- [PyGame][]
- [PySerial][]
- [Faenza icon theme][faenza]
- [SciPy and NumPy][scipy]
- [Expyriment][]
- [PsychoPy][]
- [PyOpenGL][]

[sr-research]: http://www.sr-research.com/
[gpl]: http://www.gnu.org/licenses/gpl.html
[python]: http://www.python.org/
[qt4]: http://qt.nokia.com/
[pygame]: http://www.pygame.org/
[pyserial]: http://pyserial.sourceforge.net/
[faenza]: http://tiheum.deviantart.com/art/Faenza-Icons-173323228
[scipy]: http://www.scipy.org/
[expyriment]: http://www.expyriment.org/
[psychopy]: http://www.psychopy.org/
[pyopengl]: http://pyopengl.sourceforge.net/
[plug-ins]: /plug-ins
[external-devices]: /devices/
[python-scripting]: /python-inline-code