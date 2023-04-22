title: Veuillez fournir le texte à traduire.
hash: 6c70867370aa97b006209d57e083504cd28b4f73a9eb715aae26ff5532faaf08
locale: fr
language: French

Si vous souhaitez proposer une traduction, il est recommandé d'envoyer d'abord une demande à <s.mathot@cogsci.nl> ou de poster un message sur le [forum](https://forum.cogsci.nl/) pour vous assurer que votre langue n'est pas déjà en cours de traduction.

Très peu de compétences techniques sont nécessaires pour contribuer à une traduction !

[TOC]


## Démarrer OpenSesame avec une langue spécifique

Par défaut, OpenSesame utilise la langue par défaut de votre système d'exploitation si une traduction est disponible, et revient à l'anglais si une traduction n'est pas disponible. Pour démarrer OpenSesame avec une langue spécifique, vous pouvez modifier l'option Langue dans Menu → Outils → Préférences.


## Comment traduire


### Traduire les onglets Markdown


#### Comment traduire les onglets Markdown

Les onglets Markdown sont les onglets de type site web qui présentent du texte et des options de base. Un exemple d'onglet Markdown est l'onglet Démarrer que vous voyez lorsque vous lancez OpenSesame.

Pour traduire un onglet Markdown, localisez d'abord le fichier `.md` non traduit (anglais). Dans le cas de l'onglet Démarrer, il s'agit de :

- `opensesame_extensions\get_started\get_started.md`

Ensuite, copiez ce fichier original vers `[dossier original]\locale\[votre code de langue]\get_started.md`. Ainsi, si vous travaillez sur une traduction française (`fr_FR`), vous copieriez le fichier `get_started.md` original vers (en créant des sous-dossiers s'ils n'existent pas encore) :

- `opensesame_extensions\get_started\locale\fr_FR\get_started.md`

Enfin, ouvrez simplement le fichier `get_started.md` à traduire dans un éditeur de texte et traduisez-le.


#### Liste des onglets Markdown à traduire

Dans le [code source d'OpenSesame](https://github.com/smathot/opensesame) :

- `opensesame_extensions/update_checker/failed.md`
- `opensesame_extensions/update_checker/update-available.md`
- `opensesame_extensions/update_checker/up-to-date.md`
- `opensesame_extensions/toolbar_menu/system-information.md`
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

Dans le [code source de Rapunzel](https://github.com/smathot/rapunzel) :

- `opensesame_extensions/RapunzelWelcome/rapunzel_welcome.md`


### Traduire le code source et l'interface utilisateur


#### Étape 1 : Télécharger translatables.ts

Si vous commencez une traduction à partir de zéro, vous commencez par `translatables.ts`, qui contient toutes les chaînes de caractères à traduire. OpenSesame et Rapunzel ont chacun leur propre version de ce fichier, qui doivent toutes deux être traduites.

Dans le [code source d'OpenSesame](https://github.com/smathot/OpenSesame/), ce fichier se trouve à :

- `opensesame_resources/ts/translatables.ts`

Dans le [code source de Rapunzel](https://github.com/smathot/rapunzel/), ce fichier se trouve à :

- `opensesame_extensions/RapunzelLocale/translatables.ts`

Vous pouvez soit télécharger ou cloner le code source et ouvrir directement ces fichiers. Ou vous pouvez les visualiser via GitHub. Dans ce dernier cas, en haut à droite du fichier, vous verrez un lien 'Raw'. Faites un clic droit sur ce lien et sélectionnez 'Enregistrer le fichier sous' (ou quelque chose du genre, selon votre navigateur) pour enregistrer le fichier sur votre disque.

#### Étape 2 : Installer Qt Linguist

Qt Linguist est un outil graphique qui vous aidera dans le processus de traduction. Il est convivial et vous permet de simplement sélectionner une chaîne de texte (en anglais) et de saisir une traduction.

__Windows__

Vous pouvez télécharger une version autonome de Qt Linguist ici :

- <https://github.com/thurask/Qt-Linguist/releases>

__Mac OS__

Vous pouvez télécharger une version autonome de Qt Linguist ici :
- <https://github.com/lelegard/qtlinguist-installers/releases>

__Linux__

Sur Linux, Qt Linguist est généralement disponible dans les dépôts. Par exemple, sur Ubuntu, il peut être installé avec :

	sudo apt-get install qttools5-dev-tools

#### Étape 3 : Ouvrir translatables.ts dans Qt Linguist

Lancez Qt Linguist et ouvrez `translatables.ts`. Vous serez d'abord invité à saisir une langue source et une langue cible. Laissez la source telle quelle : 'POSIX/ Any country'. La langue cible doit être réglée sur la langue dans laquelle vous traduirez OpenSesame. Laissez l'option Pays/Région sur 'Any country'. Vous pouvez modifier ces paramètres ultérieurement via Menu → Edit → Translation file settings.

Vous pouvez maintenant commencer à traduire ! Sur la gauche, vous verrez une liste de 'contexts'. Ceux-ci indiquent dans quel contexte le texte est affiché, ce qui est utile. Pour traduire, cliquez simplement sur la première chaîne de texte source dans le premier contexte, saisissez une traduction appropriée et appuyez sur `Ctrl+Enter` pour passer à la chaîne suivante.

Certaines chaînes contiendront des balises HTML, comme ceci :

	Size<br /><i>in pixels</i>

Dans ce cas, ne changez que le texte et laissez les balises HTML telles quelles. Ainsi, pour une traduction en français, cela deviendrait :

	Taille<br /><i>en pixels</i>

De plus, certaines chaînes contiennent des caractères génériques, comme ceci :

	Tell me more about the %s item

Ces caractères génériques `%s` (et `%d`, `%f`, `{}`, etc.) sont des espaces qui sont remplis à la volée par OpenSesame. Veuillez les respecter (la suppression d'un caractère générique fera planter le programme!) et essayez de construire une traduction appropriée autour d'eux. Ainsi, pour une traduction en français, cela deviendrait :

	Parlez-moi davantage de l'élément %s

#### Étape 4 : Compiler votre traduction en `.qm` et la tester

OpenSesame n'utilise pas directement le fichier `.ts`, mais nécessite un fichier au format `.qm`. Vous pouvez créer ce fichier facilement à partir de Qt Linguist en sélectionnant 'File → Release as'. Créez un fichier `.qm` avec le même nom (à l'exception de l'extension) que le fichier original.

Pour OpenSesame, ce fichier doit être enregistré sous (changer `fr_FR` par la langue appropriée) :

- `opensesame_resources/locale/fr_FR.qm`

Pour Rapunzel, ce fichier doit être sauvegardé sous (changer `fr_FR` par la langue appropriée) :

- `opensesame_extensions/RapunzelLocale/fr_FR.qm`

## Enregistrez et soumettez vos traductions

### Envoyer par e-mail

Une fois que vous êtes satisfait de vos traductions, envoyez le fichier `.ts` traduit et tous les fichiers `md` traduits à <s.mathot@cogsci.nl>.

### Soumettre via GitHub

Vous pouvez également soumettre (et mettre à jour) votre traduction via GitHub. D'abord, ajoutez votre traduction à votre fork d'OpenSesame, sous `opensesame_resources/ts/ll_RR.ts`, où `ll` correspond à la langue et `RR` à la région. Par exemple, `en_US` est l'anglais américain, `fr_FR` est le français et `zh_CN` est le chinois. Vous pouvez trouver une liste des régions et langues valides [ici](http://www.iana.org/assignments/language-subtag-registry).

De même, ajoutez tous les fichiers `.md` traduits à votre fork d'OpenSesame.

Enfin, soumettez une demande d'extraction (pull request) pour que votre traduction soit incluse dans OpenSesame.

## Mettre à jour une traduction existante

Le processus de mise à jour d'une traduction existante est similaire à celui décrit ci-dessus pour la création d'une nouvelle traduction. La différence cruciale est que vous ne commencez pas avec `resources/ts/translatables.ts`, mais avec un fichier de traduction non vide, tel que `resources/ts/fr_FR.ts`.