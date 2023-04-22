<div class="ClassDoc YAMLDoc" id="eyetracker" markdown="1">

# classe __eyetracker__

Une bibliothèque Python générique pour le suivi du regard.

<div class="FunctionDoc YAMLDoc" id="eyetracker-calibrate" markdown="1">

## fonction __eyetracker\.calibrate__\(\)

Calibre le système de suivi du regard. Le comportement réel de cette
fonction dépend du type de suivi du regard et est décrit ci-dessous.

__EyeLink:__

Cette fonction active l'écran de configuration de la caméra, qui permet
d'ajuster la caméra et d'effectuer une procédure de calibration/validation.
Appuyer sur 'q' quittera la routine de configuration. Appuyer
sur 'échap' déclenchera d'abord une boîte de dialogue de confirmation, puis, après
confirmation, lève une exception.

__EyeTribe:__

Active une routine de calibration simple.

__Retourne:__

Renvoie Vrai si la calibration a réussi, ou Faux si ce n'est pas le cas; en
plus, un journal de calibration est ajouté au fichier journal et certaines
propriétés sont mises à jour (c'est-à-dire les seuils pour la détection
algorithmes).

- Type : bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-close" markdown="1">

## fonction __eyetracker\.close__\(\)

Ferme soigneusement la connexion au tracker. Sauvegarde les données et définit
`self.connected` à Faux.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-connected" markdown="1">

## function __eyetracker\.connected__\(\)

Vérifie si le suivi est connecté.

__Retourne:__

Vrai si la connexion est établie, Faux si ce n'est pas le cas; définit
`self.connected` à la même valeur.

- Type : bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-draw_calibration_target" markdown="1">

## function __eyetracker\.draw\_calibration\_target__\(x, y\)

Dessine une cible de calibration.

__Arguments:__

- `x` -- La coordonnée X
	- Type : int
- `y` -- La coordonnée Y
	- Type : int

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-draw_drift_correction_target" markdown="1">

## function __eyetracker\.draw\_drift\_correction\_target__\(x, y\)

Dessine une cible de correction de dérive.

__Arguments:__

- `x` -- La coordonnée X
	- Type : int
- `y` -- La coordonnée Y
	- Type : int

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-drift_correction" markdown="1">

## function __eyetracker\.drift\_correction__\(pos=None, fix\_triggered=False\)

Effectue une procédure de correction de dérive. Le comportement exact de cette
fonction dépend du type de suivi du regard et est décrit ci-dessous. Parce que
la correction de dérive peut échouer, vous appellerez généralement cette fonction dans
une boucle.

__EyeLink:__

Appuyer sur 'q' pendant la correction de dérive activera l'écran de configuration de la caméra. À partir de là, appuyer sur 'q' à nouveau entraînera l'échec immédiat de la correction de dérive. Appuyer sur 'échap' donnera la possibilité d'interrompre l'expérience, auquel cas une exception est levée.

__Mots-clés:__

- `pos` -- Position (x, y) du point de fixation ou None pour une fixation centrale.
	- Type : tuple, NoneType
	- Par défaut : None
- `fix_triggered` -- Booléen indiquant si la vérification de la dérive doit être effectuée en fonction de la position du regard (Vrai) ou sur l'espace pressé (Faux).
	- Type : bool
	- Par défaut : Faux

__Retourne:__

Un booléen indiquant si la vérification de la dérive est correcte (Vrai) ou non (Faux).

- Type : bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-fix_triggered_drift_correction" markdown="1">

## function __eyetracker\.fix\_triggered\_drift\_correction__\(pos=None, min\_samples=30, max\_dev=60, reset\_threshold=10\)

Effectue une correction de dérive déclenchée par la fixation en collectant
un certain nombre d'échantillons et en calculant la distance moyenne par rapport à la
position de fixation

__Mots-clés:__

- `pos` -- Position (x, y) du point de fixation ou None pour une fixation centrale.
	- Type : tuple, NoneType
	- Par défaut : None
- `min_samples` -- Le nombre minimal d'échantillons après lequel une déviation moyenne est calculée.
	- Type : int
	- Par défaut : 30
- `max_dev` -- La déviation maximale par rapport à la fixation en pixels.
	- Type : int
	- Par défaut : 60
- `reset_threshold` -- Si la distance horizontale ou verticale en pixels entre deux échantillons consécutifs est supérieure à ce seuil, la collecte d'échantillons est réinitialisée.
	- Type : int
	- Par défaut : 10

__Renvoie :__

Un booléen indiquant si la vérification de dérive est correcte (True) ou non (False).

- Type : bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-get_eyetracker_clock_async" markdown="1">

## fonction __eyetracker\.get\_eyetracker\_clock\_async__\(\)

Renvoie la différence entre l'heure du suiveur et l'heure de PyGaze, qui peut être utilisée pour synchroniser le temps

__Renvoie :__

La différence entre l'heure du suiveur de regard et l'heure de PyGaze.

- Type : int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-log" markdown="1">

## fonction __eyetracker\.log__\(msg\)

Écrit un message dans le fichier de journal.

__Arguments :__

- `msg` -- Un message.
	- Type : str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-log_var" markdown="1">

## fonction __eyetracker\.log\_var__\(var, val\)

Écrit le nom et la valeur d'une variable dans le fichier de journal

__Arguments :__

- `var` -- Un nom de variable.
	- Type : str, unicode
- `val` -- Une valeur de variable

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-pupil_size" markdown="1">

## fonction __eyetracker\.pupil\_size__\(\)

Renvoie la taille de la pupille la plus récente ; la taille peut être mesurée comme le diamètre ou la surface de la pupille, selon votre configuration (notez que la taille de la pupille est généralement donnée en unités arbitraires).

__Renvoie :__

Renvoie la taille de la pupille pour l'œil qui est actuellement suivi (tel que spécifié par self.eye_used) ou -1 lorsque aucune donnée n'est obtenable.

- Type : int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-sample" markdown="1">

## fonction __eyetracker\.sample__\(\)

Renvoie la position du regard la plus récente disponible.

__Renvoie :__

Un tuple (x, y) ou un (-1, -1) en cas d'erreur.

- Type : tuple

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-send_command" markdown="1">

## fonction __eyetracker\.send\_command__\(cmd\)

Envoie directement une commande au suiveur de regard (non pris en charge pour toutes les marques ; peut produire un message d'avertissement si votre configuration ne prend pas en charge les commandes directes).

__Arguments :__

- `cmd` -- La commande à envoyer au suiveur de regard.
	- Type : str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_detection_type" markdown="1">

## fonction __eyetracker\.set\_detection\_type__\(eventdetection\)

Définit le type de détection des événements sur les algorithmes PyGaze, ou
les algorithmes natifs fournis par le fabricant (seulement si
disponible : le type de détection sera par défaut PyGaze si aucune fonction native
n'est disponible)

__Arguments :__

- `eventdetection` -- Une chaîne indiquant quel type de détection
doit être utilisé : soit 'pygaze' pour
les algorithmes de détection d'événements PyGaze ou
'native' pour les algorithmes du fabricant (seulement
si disponible ; par défaut à 'pygaze' si aucune
détection d'événements native n'est disponible)
	- Type : str, unicode

__Renvoie :__

Type de détection pour les saccades, les fixations et les clignotements dans un tuple, par exemple ('pygaze','native','native') lorsque 'native' a été passé, mais la détection native n'était pas disponible pour la détection de saccade.

- Type : tuple

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_draw_calibration_target_func" markdown="1">

## fonction __eyetracker\.set\_draw\_calibration\_target\_func__\(func\)

Spécifie une fonction personnalisée pour dessiner la cible de calibration. Cette fonction remplacera la fonction par défaut [draw_calibration_target].

__Arguments :__

- `func` -- La fonction pour dessiner une cible de calibration. Cette fonction doit accepter deux paramètres, pour les coordonnées x et y de la cible.
	- Type : fonction

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_draw_drift_correction_target_func" markdown="1">

## fonction __eyetracker\.set\_draw\_drift\_correction\_target\_func__\(func\)

Spécifie une fonction personnalisée pour dessiner la cible de correction de dérive. Cette fonction remplacera la fonction par défaut [draw_drift_correction_target].

__Arguments :__

- `func` -- La fonction pour dessiner une cible de correction de dérive. Cette fonction doit accepter deux paramètres, pour les coordonnées x et y de la cible.
	- Type : fonction

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_eye_used" markdown="1">

## fonction __eyetracker.set_eye_used__()

Enregistre la variable `eye_used`, selon l'œil spécifié (si les deux yeux sont suivis, l'œil gauche est utilisé). Ne retourne rien.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-start_recording" markdown="1">

## fonction __eyetracker.start_recording__()

Démarre l'enregistrement. Définit `self.recording` sur `True` lorsque l'enregistrement est démarré avec succès.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-status_msg" markdown="1">

## fonction __eyetracker.status_msg__(msg)

Envoie un message d'état à l'eye tracker, qui est affiché dans l'interface graphique du traceur (uniquement disponible pour les configurations EyeLink).

__Arguments :__

- `msg` -- Une chaîne de caractères à afficher sur le PC de l'expérimentateur,
par exemple : "essai en cours : %d" % trialnr.
  - Type : str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-stop_recording" markdown="1">

## fonction __eyetracker.stop_recording__()

Arrête l'enregistrement. Définit `self.recording` sur `False` lorsque l'enregistrement est arrêté avec succès.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_blink_end" markdown="1">

## fonction __eyetracker.wait_for_blink_end__()

Attend la fin d'un clignement et renvoie le temps de fin du clignement.
Détection basée sur Dalmaijer et al. (2013) si EVENTDETECTION est défini
sur 'pygaze', ou à l'aide de fonctions de détection natives si EVENTDETECTION
est défini sur 'native' (NOTE : tous les systèmes n'ont pas de fonctionnalité native ;
retournera à ;pygaze' si 'native' n'est pas disponible !)

__Renvoie :__

Temps de fin du clignement en millisecondes, mesuré depuis le début de l'expérience.

- Type : int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_blink_start" markdown="1">

## fonction __eyetracker.wait_for_blink_start__()

Attend le début d'un clignement et renvoie le temps de début du clignement.
Détection basée sur Dalmaijer et al. (2013) si EVENTDETECTION est défini
sur 'pygaze', ou à l'aide de fonctions de détection natives si EVENTDETECTION
est défini sur 'native' (NOTE : tous les systèmes n'ont pas de fonctionnalité native ;
retournera à ;pygaze' si 'native' n'est pas disponible !)

__Renvoie :__

Temps de début du clignement en millisecondes, mesuré depuis le début de l'expérience

- Type : int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_event" markdown="1">

## fonction __eyetracker.wait_for_event__(event)

Attend un événement.

__Arguments :__

- `event` -- Un code d'événement entier, l'un des suivants :

- 3 = STARTBLINK
- 4 = ENDBLINK
- 5 = STARTSACC
- 6 = ENDSACC
- 7 = STARTFIX
- 8 = ENDFIX
  - Type : int

__Renvoie :__

Une méthode `self.wait_for_*` est appelée, en fonction de l'événement spécifié ; la valeur de retour de la méthode correspondante est renvoyée.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_fixation_end" markdown="1">

## fonction __eyetracker.wait_for_fixation_end__()

Renvoie le temps et la position du regard lorsqu'une fixation s'est terminée ;
la fonction suppose qu'une "fixation" est terminée lorsqu'un écart de
plus de self.pxfixtresh par rapport à la position de fixation initiale a
été détecté (self.pxfixtresh est créé dans la calibration de soi-même,
basée sur self.fixtresh, une propriété définie dans self.__init__).
Détection basée sur Dalmaijer et al. (2013) si EVENTDETECTION est défini
sur 'pygaze', ou à l'aide de fonctions de détection natives si EVENTDETECTION
est défini sur 'native' (NOTE : tous les systèmes n'ont pas de fonctionnalité native ;
retournera à ;pygaze' si 'native' n'est pas disponible !)

__Renvoie :__

Un tuple `time, gazepos`. Le temps est le temps de fin en millisecondes (depuis le début de l'expérience), gazepos est un tuple de position du regard (x,y) de la position à partir de laquelle la fixation a été initiée.

- Type : tuple

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_fixation_start" markdown="1">

## fonction __eyetracker.wait_for_fixation_start__()

Renvoie l'heure de début et la position lorsqu'une fixation est commencée ;
la fonction suppose qu'une "fixation" a commencé lorsque la position du regard
reste raisonnablement stable (c'est-à-dire lorsque la plupart des échantillons déviants sont
à l'intérieur de self.pxfixtresh) pendant cinq échantillons d'affilée (self.pxfixtresh
est créé dans self.calibration, basé sur self.fixtresh, une propriété
définie dans self.__init__).
Détection basée sur Dalmaijer et al. (2013) si EVENTDETECTION est défini
à 'pygaze', ou en utilisant des fonctions de détection natives si EVENTDETECTION
est défini sur 'native' (NOTE : tous les systèmes n'ont pas de fonctionnalité native ;
retournera à 'pygaze' si 'native' n'est pas disponible!)

__Renvoie :__

Un tuple `time, gazepos`. Time est l'heure de début en millisecondes (à partir de expstart), gazepos est un tuple de position (x,y) du regard à partir duquel la fixation a été initiée.

- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_saccade_end" markdown="1">

## fonction __eyetracker\.wait\_for\_saccade\_end__\(\)

Renvoie l'heure de fin, la position de départ et la position de fin lorsqu'une saccade est
terminée ; basée sur l'algorithme de détection de saccades en ligne de Dalmaijer et al. (2013) si EVENTDETECTION est défini à 'pygaze', ou en utilisant des
fonctions de détection natives si EVENTDETECTION est défini sur 'native' (NOTE: pas
tous les systèmes ont une fonctionnalité native ; retournera à 'pygaze'
si 'native' n'est pas disponible !)

__Renvoie :__

Un tuple `endtime, startpos, endpos`. Endtime en millisecondes (à partir de expbegintime) ; startpos et endpos sont des tuples de position (x,y) du regard.

- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_saccade_start" markdown="1">

## fonction __eyetracker\.wait\_for\_saccade\_start__\(\)

Renvoie l'heure de début et la position de départ lorsqu'une saccade est
commencée ; basée sur l'algorithme de détection de saccades en ligne de Dalmaijer et al. (2013) si EVENTDETECTION est défini à 'pygaze', ou en utilisant des
fonctions de détection natives si EVENTDETECTION est défini sur 'native' (NOTE: pas
tous les systèmes ont une fonctionnalité native ; retournera à 'pygaze'
si 'native' n'est pas disponible !)

__Renvoie :__

Un tuple `endtime, startpos`. Endtime en millisecondes (à partir de expbegintime) ; startpos est un tuple de position (x,y) du regard.

- Type: tuple

</div>

</div>

