title: Translate


If you want to provide a translation, it's recommended to first send an inquiry to <l.vanderlinden@cogsci.nl> or post a message on the [forum][] to make sure that your language is not already being worked on.

Very little technical skill is needed to contribute a translation!

[TOC]


## Starting OpenSesame with a specific language

By default, OpenSesame uses the default locale of your operating system if a translation is available, and falls back to English if a translation is not available. To start OpenSesame with a specific language, you can open change the Language option under Menu → Tools → Preferences.


## How to translate

### Translating Markdown tabs

#### How to translate Markdown tabs

Markdown tabs are the website-like tabs that present text and basic options. An example of a Markdown tab is the Get Started tab that you see when you launch OpenSesame.

To translate a Markdown tab, first locate the untranslated (English) `.md` file. In the case of the Get Started tab, this is:

- `opensesame_extensions\get_started\get_started.md`

Next, copy this original file to `[original folder]\locale\[your locale code]\get_started.md`. So, if you're working on a French (`fr_FR`) translation, you would copy the original `get_started.md` to (creating subfolders if they don't exist yet):
	
- `opensesame_extensions\get_started\locale\fr_FR\get_started.md`

Finally, simply open the to-be-translated `get_started.md` in a text editor, and translate it.

#### A list of Markdown tabs that need to be translated

- `opensesame_extensions/update_checker/failed.md`
- `opensesame_extensions/update_checker/update-available.md`
- `opensesame_extensions/update_checker/up-to-date.md`
- `opensesame_extensions/help/offline_help.md`
- `opensesame_extensions/bug_report/failure.md`
- `opensesame_extensions/bug_report/report.md`
- `opensesame_extensions/bug_report/success.md`
- `opensesame_extensions/after_experiment/finished.md`
- `opensesame_extensions/system_information/system-information.md`
- `opensesame_extensions/get_started/get_started.md`
- `opensesame_extensions/opensesame_3_notifications/new-user.md`
- `opensesame_extensions/opensesame_3_notifications/old-experiment.md`
- `opensesame_extensions/opensesame_3_notifications/new-experiment.md`
- `opensesame_plugins/notepad/notepad.md`
- `opensesame_plugins/port_reader/port_reader.md`
- `opensesame_plugins/repeat_cycle/repeat_cycle.md`
- `opensesame_plugins/quest_staircase_init/quest_staircase_init.md`
- `opensesame_plugins/parallel/parallel.md`
- `opensesame_plugins/advanced_delay/advanced_delay.md`
- `opensesame_plugins/joystick/joystick.md`
- `opensesame_plugins/reset_feedback/reset_feedback.md`
- `opensesame_plugins/fixation_dot/fixation_dot.md`
- `opensesame_plugins/touch_response/touch_response.md`
- `opensesame_plugins/external_script/external_script.md`
- `opensesame_plugins/quest_staircase_next/quest_staircase_next.md`
- `opensesame_plugins/video_player/video_player.md`
- `opensesame_resources/help/missing.md`
- `opensesame_resources/help/new_item_warning.md`


### Translating the source code and user interface

#### Step 1: Download translatables.ts

`translatables.ts` is an XML file that contains all the strings that are to be translated. You can download it from here:

- <https://github.com/smathot/OpenSesame/blob/james/opensesame_resources/ts/translatables.ts>

At the top-right of the file, you will see a 'Raw' link. Right-click on this link and select 'Save file as' (or something along those lines, depending on your browser) to save the file your disk.

#### Step 2: Install QtLinguist

QtLinguist is a graphical tool that will assist you in the translation process. It's very user friendly, and allows you to simply select a string of (English) text and enter a translation.

__Windows and Mac OS__

You can download QtLinguist as part of the [Qt development toolkit](http://qt-project.org/downloads) or as a [standalone program] (http://code.google.com/p/qtlinguistdownload/). The standalone option is probably easiest for most people.

__Linux__

On Linux, QtLinguist is generally available in the repositories. For example, on Ubuntu it can be installed with:

	sudo apt-get install qt4-linguist-tools

#### Step 3: Open translatables.ts in QtLinguist

Now start QtLinguist and open `translatables.ts`. You will first be asked to enter a source and target language. Leave the source as it is: 'POSIX/ Any country'. The target language should be set to the language that you will translate OpenSesame into. Leave the Country/Region option at 'Any country'. You can change these settings later via Menu -> Edit -> Translation file settings.

Now you can start translating! On the left you will see a list of 'contexts'. These indicate in which context the text is shown, which is helpful. To translate, simply click on the first source text-string in the first context, enter an appropriate translation, and press 'Control+Enter' to advance to the next string.

Some strings will contain HTML tags, like so:

	Size<br /><i>in pixels</i>

In this case, only change the text and leave the HTML tags as they are. So, for a Dutch translation this would become:

	Grootte<br /><i>in pixels</i>

Also, some strings contain wildcards, like so:

	Tell me more about the %s item

These `%s` (and `%d`, `%f`, etc.) wildcards are blanks that are filled in on-the-fly by OpenSesame. Please respect these (removing a wild-card will crash the program!) and try to build an appropriate translation around them. So, for a Dutch translation this would become:

	Vertel me meer over het %s item

#### Step 4: Compile your translation to `.qm` and test it

OpenSesame doesn't use the `.ts` file directly, but requires a file in `.qm` format. You can create this file easily from within Qt Linguist by selecting 'File -> Release as'. Create a `.qm` file with the same name (except for the extension) as the original file, and place it in the `opensesame_resources/locale` subfolder of the OpenSesame folder. So, for example, if you're working on a French translation, your original source file would be `opensesame_resources/ts/fr_FR.ts` and your compiled file would be `opensesame_resources/locale/fr_FR.qm`.

Once you have compiled your translation file to `.qm` format and placed it in the resources folder, run OpenSesame with your new locale as described at the top of this page.

## Save and submit your translations

### Send by e-mail

Once you are satisfied with your translations, send the translated `.ts` file and all translated `md` files to <l.vanderlinden@cogsci.nl>.

### Submit through GitHub

You can also submit (and update) your translation via GitHub. First, add your translation to your fork of OpenSesame, as `opensesame_resources/ts/ll_RR.ts`, where `ll` corresponds to the language and `RR` to the region. For example, `en_US` is US english, `fr_FR` is French, and `zh_CN` is Chinese. You can find a list of valid regions and languages [here](http://www.iana.org/assignments/language-subtag-registry).

Similarly, add all translated `.md` files to your fork of OpenSesame.

Finally, submit a pull request to have your translation included in OpenSesame.


## Updating an existing translation

The process to update an existing translation is similar to that described above for creating a new translation. The crucial difference is that you don't start with `resources/ts/translatables.ts`, but with a non-blank translation file, such as `resources/ts/fr_FR.ts`.

[forum]: http://forum.cogsci.nl/
