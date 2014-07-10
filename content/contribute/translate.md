---
layout: osdoc
title: Translate
group: contribute
permalink: /translate/
parser: academicmarkdown
---

In order to improve usability for non-English speaking users, the goal is to have OpenSesame adapt to the default language of the operating system. As of v0.27, the OpenSesame user interface is largely translatable. Very little technical skill is needed to contribute a translation.

If you want to provide a translation, it's recommended to first send an inquiry to <lvanderlinden@cogsci.nl> or post a message on the [forum][], to make sure that your language is not already being worked on.

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Status of current translations

|**Code**	|**Language**		|**Status**			|**Author(s)**					|
|`en_EN`	|English			|Default			|								|
|`it_IT` 	|Italian			|Complete			|Andrea Epifani					|
|`fr_FR`	|French				|Complete			|Romain Monfollet				|
|`zh_CN`	|Chinese			|Complete			|[Zhongquan Li](https://github.com/zqlinju) and Gabriel Chan	|
|`nl_NL`	|Dutch				|In progress		|[Lotje van der Linden](https://github.com/lvanderlinden)			|
|`de_DE`	|German				|Complete			|Timo Lüke				|
|`ru_RU`	|Russian 			|Complete			|Vladimir Kosonogov		|

## Starting OpenSesame with a specific language

By default, OpenSesame will try to use the default locale of your operating system, and fall back to English if a translation is not available. To start OpenSesame with a specific language, you can use the `--locale` command line argument. For example, to use the Italian translation start OpenSesame as follows:

	opensesame --locale it_IT

This will look for a file called `resources/locale/it_IT.qm`, and fall back to English if no such file exists.

## The five-step translation process

### Step 1: Download translatables.ts

`translatables.ts` is an XML file that contains all the strings that are to be translated. You can download it from here:

- <https://github.com/smathot/OpenSesame/blob/master/resources/ts/translatables.ts>

At the top-right of the file, you will see a 'Raw' link. Right-click on this link and select 'Save file as' (or something along those lines, depending on your browser) to save the file your disk.

### Step 2: Install QtLinguist

QtLinguist is a graphical tool that will assist you in the translation process. It's very user friendly, and allows you to simply select a string of (English) text and enter a translation.

#### Windows and Mac OS

You can download it as part of the Qt development toolkit (<http://qt-project.org/downloads>) or as a standalone program (<http://code.google.com/p/qtlinguistdownload/>). The standalone option is probably easiest for most people.

#### Linux

On Linux, the QtLinguist is generally available in the repositories. For example, on Ubuntu it can be installed with:

	sudo apt-get install qt4-linguist-tools

### Step 3: Open translatables.ts in QtLinguist

Now start QtLinguist and open `translatables.ts`. You will first be asked to enter a source and target language. Leave the source as it is: 'POSIX/ Any country'. The target language should be set to the language that you will translate OpenSesame into. Leave the Country/Region option at 'Any country'. You can change these settings later via Menu -> Edit -> Translation file settings.

Now you can start translating! On the left you will see a list of 'contexts'. These correspond to different parts of the OpenSesame GUI. The 'script' context corresponds to the translatable text messages that are generated on-the-fly (i.e. not part of static menus, etc.). To translate, simply click on the first source text-string in the first context, enter an appropriate translation, and press 'Control+Enter' to advance to the next string.

Some strings will contain HTML tags, like so:

	Size<br /><i>in pixels</i>

In this case, only change the text and leave the HTML tags as they are. So, for a Dutch translation this would become:

	Grootte<br /><i>in pixels</i>

Also, some strings contain wildcards, like so:

	Tell me more about the %s item

These `%s` (and `%d`, `%f`, etc.) wildcards are blanks that are filled in on-the-fly by OpenSesame. Please respect these (removing a wild-card will crash the program!) and try to build an appropriate translation around them. So, for a Dutch translation this would become:

	Vertel me meer over het %s item

### Step 4: Compile your translation to `.qm` and test it

OpenSesame doesn't use the `.ts` file directly, but requires a file in `.qm` format. You can create this file easily from within Qt Linguist by selecting 'File -> Release as'. Create a `.qm` file with the same name (except for the extension) as the original file, and place it in the `resources/locale` subfolder of the OpenSesame folder. So, for example, if you're working on a French translation, your original source file would be `resources/ts/fr_FR.ts` and your compiled file would be `resources/locale/fr_FR.qm`.

Once you have compiled your translation file to `.qm` format and placed it in the resources folder, run OpenSesame with your new locale as described [here](#select).

### Step 5: Save and submit your translations

#### Send by e-mail

Once you are satisfied with your translations, save the `translations.ts` file under a new name and send it to <l.vanderlinden@cogsci.nl>.

#### Submit through GitHub

You can also submit (and update) your translation via GitHub. First, add your translation to your fork of OpenSesame, as `resources/ts/ll_RR.ts`, where `ll` corresponds to the language and `RR` to the region. For example, `en_US` is US english, `fr_FR` is French, and `zh_CN` is Chinese. You can find a list of valid regions and languages [here](http://www.iana.org/assignments/language-subtag-registry). Next, submit a pull request to have your translation included in OpenSesame.

[forum]: http://forum.cogsci.nl/
