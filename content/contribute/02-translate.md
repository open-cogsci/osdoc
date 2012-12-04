---
layout: osdoc
title: Translate
group: contribute
permalink: /translate/
level: 1
sortkey: 0013.002
---

In order to improve usability for non-English speaking users, the goal is to have OpenSesame adapt to the default language of the operating system. As of v0.27, the OpenSesame user interface is largely translatable. Very little technical skill is needed to contribute a translation.

If you want to provide a translation, it's recommended to first send an enquiry to <lvanderlinden@cogsci.nl> or post a message on the [forum][], to make sure that your language is not already being worked on.

Step 1: Download translatables.ts
---------------------------------

`translatables.ts` is an XML file that contains all the strings that are to be translated. You can download it from here:

- <https://github.com/smathot/OpenSesame/blob/master/resources/ts/translatables.ts>

At the top-right of the file, you will see a 'Raw' link. Right-click on this link and select 'Save file as' (or something along those lines, depending on your browser) to save the file your disk.

Step 2: Install QtLinguist
--------------------------

QtLinguist is a graphical tool that will assist you in the translation process. It's very user friendly, and allows you to simply select a string of (English) text and enter a translation.

### Windows and Mac OS

You can download it as part of the Qt development toolkit (<http://qt.nokia.com/downloads>) or as a standalone program (<http://code.google.com/p/qtlinguistdownload/>). The standalone option is probably easiest for most people.

### Linux

On Linux, the QtLinguist is generally available in the repositories. For example, on Ubuntu it can be installed with:

	sudo apt-get install qt4-linguist-tools

Step 3: Open translatables.ts in QtLinguist
-------------------------------------------

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

Step 4: Save and submit your translations
-----------------------------------------

Once you are satisfied with your translations, save the translations.ts file under a new name and send it to <l.vanderlinden@cogsci.nl>.

[forum]: http://forum.cogsci.nl/