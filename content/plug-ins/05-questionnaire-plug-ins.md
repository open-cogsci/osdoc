---
layout: osdoc
title: Questionnaire plug-ins
group: Plug-ins
permalink: /questionnaire-plug-ins/
level: 1
sortkey: 007.005
---

##### As of OpenSesame 0.27, [forms][] provide a better way to implement questionnaires

About the questionnaire plug-ins
--------------------------------

The questionnaire plug-ins provide functionality for creating questionnaires and the like. They are aimed primarily at social psychologists, although it may come in handy in a wide range of experiments, of course. An example experiment is included. Right now there are four plug-ins:

- **text_screen** - a simple text screen for instructions etc.
- **open_question** - a text input field for collecting open questions
- **multiple_choice** - collects multiple choice responses using check-boxes
- **rating_scale** - provides a rating scale (i.e., Likert scale)

Installation instructions
-------------------------

### Step 1

Dowload the plug-ins from GitHub (choose the latest version): <https://github.com/smathot/opensesame_questionnaire_plugins/tags>

### Step 2

Install the plug-ins by extracting them into the OpenSesame plug-in folder, as described [here][installation]

### Step 3 (not necessary for 0.25 or any version on Linux)

These plug-ins need some Python libraries which are not included with the Windows and Mac OS binary packages of OpenSesame. Notably, you need htmllib.py, htmlentitydefs.py, HTMLparser.py and sgmlib.py. The easiest workaround is to download these missing files [here][htmllib] and extract them directly into the multiple_choice plug-in folder.http://www.koders.com/python/fid4CD0462C6AD8D7AFBAE9FF73227BB9C594388037.aspx?s=cdef%3atimer

For Mac OS only, you also need to download markupbase.py ([link][markupbase] or use google) and put it in the multple_choice plug-in folder (thanks to Roger for the tip!).

Support for non-western alphabets
---------------------------------

These plug-ins should work with non-western alphabets, but you will have to change the default font to a font that supports the alphabet you need. Copy the custom font (truetype format) to the following location and replace the default `sans.ttf`.

	multiple_choice/data/themes/default/sans.ttf

Screenshot
----------

![](/img/fig/fig7.5.1.png)

[forms]: /forms
[installation]: /plug-ins/plug-in-installation/
[htmllib]: http://files.cogsci.nl/software/opensesame/plugins/questionnaire_plugins/resources/htmllib.zip
[markupbase]: http://www.koders.com/python/fid4CD0462C6AD8D7AFBAE9FF73227BB9C594388037.aspx?s=cdef%3atimer