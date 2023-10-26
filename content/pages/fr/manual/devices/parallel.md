title: Port parallèle (déclencheurs EEG)
reviewed: false
hash: 173d67c1a3fbe4fb17b8a936fe30584d71443f518bf86bd65c9ad6da21c4e229
locale: fr
language: French

Dans les études EEG / ERP, il est courant d'envoyer des déclencheurs pour marquer le timestamp des événements importants (par exemple, le début d'un essai, la présentation d'un stimulus particulier, etc.). Les déclencheurs sont généralement des octets qui sont envoyés via le port parallèle à l'appareil EEG.

[TOC]

## Utilisation du plugin `parallel_port_trigger`

Parallel_port_trigger est un plugin tiers et n'est pas maintenu par l'équipe d'OpenSesame.
{: .page-notification}

Un plug-in OpenSesame pour envoyer des déclencheurs de synchronisation de stimulus via le port parallèle aux systèmes d'acquisition de données.

- <https://github.com/dev-jam/opensesame-plugin-parallel_port_trigger/>

Vous pouvez installer le plugin `parallel_port_trigger` depuis PyPi :

```
pip install opensesame-plugin-parallel-port-trigger
```

## Utilisation de `dportio.dll` dans un script Python inline (uniquement pour Windows)

Au lieu d'utiliser le plugin `parallel_port_trigger`, il est également possible d'envoyer des déclencheurs avec `dlportio.dll` via un script Python inline. Cette approche fonctionne uniquement sur Windows. Pour ce faire, ajoutez d'abord un INLINE_SCRIPT au début de l'expérience avec le code suivant dans la phase de préparation :

~~~ .python
try:
	from ctypes import windll
	global io
	io = windll.dlportio # requires dlportio.dll !!!
except:
	print('Le port parallèle n\'a pas pu être ouvert')
~~~

Ceci chargera `dlportio.dll` comme un objet global appelé `io`. Veuillez noter qu'une défaillance ne fera pas échouer l'expérience, alors assurez-vous de vérifier la fenêtre de débogage pour les messages d'erreur !

Maintenant, utilisez le code suivant dans un INLINE_SCRIPT n'importe où dans l'expérience pour envoyer un déclencheur :

~~~ .python
global io
trigger = 1
port = 0x378
try:
	io.DlPortWritePortUchar(port, trigger)
except:
	print('Échec de l'envoi du déclencheur !')
~~~

Notez que cela envoie le déclencheur 1 au port 0x378 (=888). Changez ces valeurs en fonction de votre configuration.

## Obtention de l'accès au port parallèle

### Linux

Sur Linux, nous utilisons le module `parport_pc` (testé sur Debian Wheezy) et nous devons nous donner les permissions pour ce faire. Nous pouvons accomplir cela en exécutant les commandes suivantes :

	sudo rmmod lp
	sudo rmmod parport_pc
	sudo modprobe parport_pc
	sudo adduser [user] lp

Ici, `[user]` doit être remplacé par votre nom d'utilisateur. Ensuite, déconnectez-vous et reconnectez-vous, et vous êtes prêt à y aller !

### Windows XP et Windows Vista (32 bits)

1. Téléchargez le pilote DLPortIO 32 bits à partir de [ici][win32-dll] et décompressez l'archive zip.
2. Allez dans le dossier `DriverLINX/drivers` et copiez `dlportio.dll` et `dlportio.sys` dans le dossier `install`. C'est le dossier où se trouve `install.exe`. Ensuite, exécutez `install.exe`
3. Vous devez copier `dlportio.dll` dans le dossier OpenSesame (c'est-à-dire le dossier qui contient `opensesame.exe`).

### Windows 7 (32 et 64 bits)

1. Téléchargez le pilote DLPortIO 32 bits ou 64 bits [ici][win7-dll] et décompressez l'archive zip.
2. Comme Windows 7 dispose d'un système de sécurité renforcé (au moins par rapport à XP), on ne peut pas simplement installer le pilote DLPortIO. Cela ne fonctionnera pas car Windows 7 bloquera toutes les tentatives d'installation d'un pilote non officiellement signé (par Microsoft). Bon pour la sécurité d'un utilisateur moyen -- mauvais pour nous. Pour contourner cette restriction, il faut utiliser un petit programme d'aide appelé "Digital Signature Enforcement Overrider" (DSEO) qui peut être téléchargé [ici][dseo] (bien sûr, il existe d'autres moyens possibles de le faire, mais ce programme est mentionné dans le `readme.txt` de DLPortIO et il ne faut pas se plonger plus profondément dans les spécificités de l'architecture de MS Windows 7).
3. Démarrez DSEO avec des privilèges d'administrateur (clic droit sur `dseo13b.exe`, sélectionnez "exécuter en tant qu'administrateur"). La fenêtre DSEO apparaît. Elle présente simplement une liste d'options pour choisir l'opération à effectuer ensuite.
4. Choisissez l'option "sign driver/sys-file" et appuyez sur ok. Une autre fenêtre apparaît où vous devez taper le chemin absolu vers le fichier `DLPortIO.sys` (seulement celui-ci, pas le dll !). N'oubliez pas d'échapper les espaces dans le chemin si vous en avez (ne demandez pas combien de temps cela m'a pris) sinon vos fichiers ne seront pas trouvés. En appuyant sur ok, vous signerez le fichier sys.
5. Retournez dans la liste DSEO, choisissez "enable test mode" et appuyez sur ok. Ensuite, choisissez "exit" et redémarrez votre PC. Windows 7 se plaint à tort que DSEO n'a peut-être pas été installé correctement -- cliquez simplement sur "oui, le logiciel est installé correctement".
6. Une fois le démarrage terminé, vous verrez que quelque chose comme "Windows 7 test mode built #number#" est écrit sur le bureau, juste au-dessus de l'horloge dans la barre de démarrage. C'est nécessaire. Vous devez être en mode test pour exécuter ce pilote non officiellement signé.
7. Exécutez maintenant `DLPortIO_install.bat` avec des privilèges d'administrateur (dans l'explorateur Windows, cliquez avec le bouton droit sur le fichier, ...). Répondez "oui" si Windows vous avertit des modifications de registre.
8. Redémarrez.
9. Copiez `DLPortIO.dll` dans le dossier Opensesame, c'est-à-dire le même dossier qui contient `opensesame.exe`.

Source : [Forum post by Absurd][post-3]

## Recommandations

- Commencez votre expérience avec un déclencheur 'zéro' pour vous assurer que toutes les broches sont réglées sur zéro.
- Il est recommandé d'utiliser les backends [psycho] ou [xpyriment] au lieu du backend [legacy] (utilisant PyGame) pour les expériences critiques en termes de temps. Cela est dû au fait que [psycho] et [xpyriment] tiennent compte de la fréquence de rafraîchissement du moniteur lorsqu'ils retournent des horodatages, alors que [legacy] ne le fait pas. Pour plus d'informations, consultez [miscellaneous/timing].
- Envoyez le code de déclenchement juste après (au lieu de juste avant) la présentation de votre stimulus (en supposant que ce soit le début du stimulus que vous voulez marquer). En faisant cela, vous vous assurerez que le timestamp est aussi précis que possible et ne souffrira pas d'un léger jitter aléatoire dû à la fréquence de rafraîchissement de votre moniteur. [Source : lvanderlinden][post-2]

## Dépannage

Il existe plusieurs sujets de forum pertinents dans lesquels les problèmes liés aux déclencheurs sont discutés (et, pour la plupart, résolus !).

- Un post sur les déclencheurs fantômes, c'est-à-dire les déclencheurs non désirés qui sont mystérieusement enregistrés par l'appareil EEG : [lien][post-2]
- Un post avec des instructions d'installation détaillées pour DLPortIO sur Windows 7 ([Source : absurd][post-3]).

N'hésitez pas à poser des questions sur le forum, ou à nous faire part de vos expériences (bonnes ou mauvaises).

[win32-dll]: http://files.cogsci.nl/misc/dlportio.zip
[win7-dll]: http://real.kiev.ua/avreal/download/#DLPORTIO_TABLE
[dseo]: http://www.ngohq.com/home.php?page=dseo
[post-2]: http://forum.cogsci.nl/index.php?p=/discussion/comment/780#Comment_780
[post-3]: http://forum.cogsci.nl/index.php?p=/discussion/comment/745#Comment_745
[miscellaneous/timing]: /miscellaneous/timing
[legacy]: /backends/legacy
[xpyriment]: /backends/xpyriment
[psycho]: /backends/psycho