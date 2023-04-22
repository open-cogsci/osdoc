title: Prolific
hash: ae0240db997107f3570b2cbf0d4576f801d25a57fbdd0a043e7f8be1bb82d715
locale: fr
language: French

[TOC]

## À propos de Prolific

[Prolific](https://prolific.co/) est un outil commercial pour recruter des participants pour la recherche. Pour exécuter des expériences OSWeb sur Prolific, vous devez suivre les étapes expliquées ci-dessous.

Voir aussi :

- <http://www.jatos.org/Use-Prolific.html>

## Créer une étude sur JATOS

D'abord, importez votre expérience dans JATOS, comme décrit ci-dessus. Ensuite, allez dans le Gestionnaire de travailleurs et de lots, activez le travailleur général multiple, obtenez une URL en cliquant sur Obtenir le lien et copiez-la (%FigJatosURL).

%--
figure :
 id: FigJatosURL
 source: jatos-url.png
 légende : Obtenir une URL d'étude de JATOS.
--%

## Créer une étude sur Prolific

Ensuite, créez une étude sur Prolific. Sous Détails de l'étude (%FigProlific), insérez l'URL de l'étude JATOS dans le champ étiqueté «Quelle est l'URL de votre étude ?». Cela indiquera à Prolific comment démarrer l'expérience. Importamment, ajoutez ce qui suit à la fin de l'URL (cela transmettra des informations importantes de Prolific à votre expérience) :

{% raw %}
```bash
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```
{% endraw %}

Lorsque l'expérience est terminée, Prolific doit en être informé. À cette fin, Prolific utilise une URL de redirection de fin, qui est répertoriée dans le champ étiqueté «Pour prouver que les participants ont terminé votre étude ...». Copiez cette URL de redirection de fin. Cochez également la case étiquetée "J'ai configuré mon étude pour rediriger vers cette url à la fin".

%--
figure:
 id: FigProlific
 source: prolific.png
 légende: Détails de l'étude sur Prolific.
--%

## Définir une URL de redirection de fin dans JATOS

Revenez maintenant à JATOS, et ouvrez les Propriétés de votre étude (%FigJatosProperties). Collez-y l'URL de redirection de fin que vous avez copiée de Prolific dans le champ étiqueté "End Redirect URL". Cela indiquera à JATOS que le participant doit être redirigé vers Prolific lorsque l'expérience est terminée, afin que Prolific sache que le participant a terminé l'expérience.

%--
figure:
 id: FigJatosProperties
 source: jatos-properties.png
 légende: Définir l'URL de redirection de fin dans JATOS.
--%

## Enregistrer les informations Prolific dans votre expérience

Chaque participant de Prolific est identifié par un identifiant unique. Il est important de consigner cet identifiant dans votre expérience, car cela vous permet de savoir quel participant de Prolific correspond à quelle entrée dans les résultats JATOS. Vous pouvez le faire en ajoutant le script ci-dessous dans la phase de préparation d'un élément `inline_javascript` au tout début de votre expérience.

Lors de l'exécution de l'expérience via Prolific, cela rendra l'ID Prolific disponible sous forme de variable expérimentale `prolific_participant_id`. Lors de l'exécution de l'expérience de toute autre manière (par exemple lors des tests), la variable `prolific_participant_id` sera définie sur -1. La même logique s'applique à l'ID d'étude Prolific (`prolific_study_id`) et à l'ID de session Prolific (`prolific_session_id`).

```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('Les informations Prolific sont disponibles')
    vars.prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    vars.prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    vars.prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('Les informations Prolific ne sont pas disponibles (valeurs définies à -1)')
    vars.prolific_participant_id = -1
    vars.prolific_study_id = -1
    vars.prolific_session_id = -1
}
console.log('prolific_participant_id = ' + vars.prolific_participant_id)
console.log('prolific_study_id = ' + vars.prolific_study_id)
console.log('prolific_session_id = ' + vars.prolific_session_id)
```

## Tester l'étude

Retournez sur la page Détails de l'étude sur Prolific. En bas de la page, il y a un bouton Aperçu. Cela vous permet de tester l'expérience en agissant comme un participant vous-même. N'oubliez pas de vérifier les résultats JATOS pour vous assurer que l'expérience s'est terminée avec succès et que toutes les informations nécessaires (y compris les informations Prolific) ont été enregistrées !