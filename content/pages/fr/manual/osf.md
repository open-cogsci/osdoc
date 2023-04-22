title: Intégration avec le Open Science Framework
hash: b86c05caa254209c5f4d161cd5c5a9daffef60ec5e5d5fca41a7aec00643d1f7
locale: fr
language: French

[TOC]

## À propos

L'extension OpenScienceFramework connecte OpenSesame au [Open Science Framework](https://osf.io) (OSF), qui est une plateforme web pour partager, connecter et rationaliser les flux de travail scientifiques. Pour utiliser cette extension, [vous devez avoir un compte OSF](https://osf.io/login/?sign_up=True).

Avec l'extension OpenScienceFramework, vous pouvez :

- Enregistrer automatiquement votre expérience sur l'OSF
- Téléverser automatiquement les données sur l'OSF
- Ouvrir des expériences depuis l'OSF
- Partager votre expérience et vos données avec d'autres chercheurs, en leur donnant accès via l'OSF

## Se connecter à l'OSF

Pour vous connecter à l'OSF :

- Créez un compte sur <https://osf.io>. (Vous ne pouvez pas créer de compte depuis OpenSesame.)
- Dans OpenSesame, cliquez sur le bouton de connexion dans la barre d'outils principale et entrez vos informations d'identification.
- Une fois connecté, vous pouvez ouvrir l'Explorateur OSF en cliquant sur votre nom à l'endroit où se trouvait le bouton de connexion, puis en sélectionnant *Afficher l'explorateur*. L'explorateur affichera un aperçu de tous vos projets OSF et de tous les dépôts/services cloud liés à vos projets.

## Lier une expérience à l'OSF

Si vous liez une expérience à l'OSF, chaque fois que vous enregistrez l'expérience dans OpenSesame, une nouvelle version est également téléversée sur l'OSF.

Pour lier une expérience :

- Enregistrez l'expérience sur votre ordinateur.
- Ouvrez l'explorateur OSF et sélectionnez un dossier ou un dépôt où vous souhaitez que votre expérience soit stockée sur l'OSF. Faites un clic droit sur ce dossier et sélectionnez *Synchroniser l'expérience avec ce dossier*. Le nœud OSF auquel l'expérience est liée sera affiché en haut de l'explorateur.
- L'expérience est ensuite téléversée à l'emplacement sélectionné.
- Si vous cochez *Toujours téléverser l'expérience lors de l'enregistrement*, une nouvelle version est automatiquement enregistrée sur l'OSF à chaque enregistrement ; si vous ne cochez pas cette option, on vous demandera à chaque fois si vous souhaitez le faire ou non.

Pour dissocier une expérience :

- Ouvrez l'explorateur OSF et cliquez sur le bouton *Dissocier* à côté du lien *Expérience liée à*.

## Lier les données à l'OSF

Si vous liez des données à l'OSF, chaque fois que des données sont collectées (normalement après chaque session expérimentale), ces données sont également téléversées sur l'OSF.

Pour lier les données à l'OSF :

- Enregistrez l'expérience sur votre ordinateur.
- Ouvrez l'explorateur OSF, faites un clic droit sur le dossier où vous souhaitez que les données soient téléversées, puis sélectionnez *Synchroniser les données avec ce dossier*. Le nœud OSF auquel les données sont liées sera affiché en haut de l'explorateur.
- Si vous cochez *Toujours téléverser les données collectées*, les fichiers de données seront automatiquement enregistrés sur l'OSF après leur collecte ; si vous ne cochez pas cette option, on vous demandera à chaque fois si vous souhaitez le faire ou non.

Pour dissocier les données de l'OSF :

- Ouvrez l'explorateur OSF et cliquez sur le bouton *Dissocier* à côté du lien *Données stockées dans*.

## Ouvrir une expérience stockée sur l'OSF

Pour ouvrir une expérience depuis l'OSF :

- Ouvrez l'explorateur OSF et trouvez l'expérience.
- Faites un clic droit sur l'expérience et sélectionnez *Ouvrir l'expérience*.
- Enregistrez l'expérience sur votre ordinateur.

## Gérer les versions non concordantes

Si vous ouvrez une expérience sur votre ordinateur liée à l'OSF, mais qui diffère de la version sur l'OSF, il vous sera demandé ce que vous voulez faire :

- Utiliser la version de votre ordinateur ; ou
- Utiliser la version de l'OSF. Si vous choisissez d'utiliser la version de l'OSF, elle sera téléchargée et remplacera l'expérience sur votre ordinateur.

## Installer l'extension OpenScienceFramework

L'extension OpenScienceFramework est installée par défaut dans le package Windows d'OpenSesame. Si l'extension n'est pas installée, vous pouvez l'installer de la manière suivante :

Depuis PyPi :

~~~
pip install opensesame-extension-osf
~~~

Dans un environnement Anaconda

~~~
conda install -c cogsci opensesame-extension-osf
~~~

Le code source de l'extension est disponible sur GitHub :

- <https://github.com/dschreij/opensesame-extension-osf>

Et pour le module `python-qosf`, qui est utilisé par l'extension :

- <https://github.com/dschreij/python-qosf>