title: OpenSesameRun (sans interface graphique)
hash: 435d6b0358c5bdd011dbe66206d56d78258410aadf1b385e46d7c8fedd2aecb2
locale: fr
language: French

## À propos

`opensesamerun` est un outil simple qui vous permet d'exécuter des expériences OpenSesame avec une interface graphique minimale, ou directement, en spécifiant toutes les options nécessaires via la ligne de commande. Une interface graphique minimale apparaîtra automatiquement si toutes les options de ligne de commande n'ont pas été spécifiées, notamment le fichier d'expérience, le numéro de sujet et le fichier journal.

~~~
Utilisation : opensesamerun [expérience] [options]

Options :
  --version             afficher le numéro de version du programme et quitter
  -h, --help            afficher ce message d'aide et quitter

  Options de sujet et de fichier journal :
    -s SUJET, --subject=SUJET
                        Numéro de sujet
    -l LOGFILE, --logfile=LOGFILE
                        Fichier journal

  Options d'affichage :
    -f, --fullscreen    Exécuter en plein écran
    -c, --custom_resolution
                        Ne pas utiliser la résolution d'affichage spécifiée dans le
                        fichier d'expérience
    -w WIDTH, --width=WIDTH
                        Largeur d'affichage
    -e HEIGHT, --height=HEIGHT
                        Hauteur d'affichage

  Options diverses :
    -d, --debug         Imprimer beaucoup de messages de débogage sur la sortie standard
                        output
    --stack             Imprimer des informations sur la pile

  Options diverses :
    --pylink            Charger PyLink avant PyGame (nécessaire pour utiliser le
                        plug-ins Eyelink en mode non fictif)
~~~

## Exemple

Disons que vous souhaitez exécuter l'expérience d'exemple de guidage du regard, pour le sujet n°1, et enregistrer le fichier journal dans votre dossier Documents (cet exemple suppose Linux, mais cela fonctionne de manière analogue sur d'autres plates-formes) :

~~~
opensesamerun /usr/share/opensesame/examples/gaze_cuing.opensesame.tar.gz -s 1 -l /home/sebastiaan/Documents/sujet1.tsv -f 
~~~


## Alternative `libopensesame`

Vous pouvez également démarrer des expériences sans utiliser l'interface graphique grâce au module Python `libopensesame` :

- %link:manuel/python/nogui%