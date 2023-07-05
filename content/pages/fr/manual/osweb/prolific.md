title: Prolific
hash: fd3ba787ea541676148e558d0e902641c2b9f9eb848745aff73e95c443e9fc56
locale: fr
language: French

[TOC]


## À propos de Prolific

[Prolific](https://prolific.co/) est un outil commercial pour recruter des participants pour la recherche. Pour exécuter des expériences OSWeb sur Prolific, vous devez suivre les étapes expliquées ci-dessous.

Voir aussi :

- <http://www.jatos.org/Use-Prolific.html>


## Créez une étude sur JATOS

D'abord, importez votre expérience dans JATOS, comme expliqué ci-dessus. Ensuite, allez dans le Gestionnaire de travailleurs et de lots, activez le Travailleur Multiple Général, obtenez une URL en cliquant sur Obtenir le lien, et copiez-la (%FigJatosURL).

%--
figure:
 id: FigJatosURL
 source: jatos-url.png
 caption: Obtenez une URL d'étude de JATOS.
--%



## Créez une étude sur Prolific

Ensuite, créez une étude sur Prolific. Sous les Détails de l'étude (%FigProlific), insérez l'URL de l'étude JATOS dans le champ "Quelle est l'URL de votre étude?". Cela indiquera à Prolific comment démarrer l'expérience. Ajoutez d'importance la chose suivante à la fin de l'URL (cela passera des informations importantes de Prolific à votre expérience) :

{% raw %}
```bash
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```
{% endraw %}

Lorsque l'expérience est terminée, Prolific doit en être informé. Pour cela, Prolific utilise une URL de redirection finale, qui est répertoriée dans le champ "Pour prouver que les participants ont terminé votre étude …". Copiez cette URL de redirection finale. Cochez également la case "J'ai configuré mon étude pour rediriger vers cette url à la fin".

%--
figure:
 id: FigProlific
 source: prolific.png
 caption: Détails de l'étude sur Prolific.
--%



## Définir une URL de redirection finale dans JATOS

Revenez maintenant à JATOS, et ouvrez les Propriétés de votre étude (%FigJatosProperties). Collez-y l'URL de redirection finale que vous avez copiée de Prolific dans le champ "URL de redirection finale". Cela indiquera à JATOS que le participant doit être redirigé vers Prolific lorsque l'expérience est terminée, afin que Prolific sache que le participant a terminé l'expérience.


%--
figure:
 id: FigJatosProperties
 source: jatos-properties.png
 caption: Définir l'URL de redirection finale dans JATOS.
--%


## Enregistrer les informations Prolific dans votre expérience

Chaque participant de Prolific est identifié par un ID unique. Il est important de consigner cet ID dans votre expérience, car cela vous permettra d'identifier à quelle entrée dans les résultats de JATOS correspond chaque participant de Prolific. Vous pouvez le faire en ajoutant le script ci-dessous dans la phase de préparation d'un élément `inline_javascript` au tout début de votre expérience.

Lors de l'exécution de l'expérience à travers Prolific, cela rendra l'ID Prolific disponible en tant que variable expérimentale `prolific_participant_id`. Lors de l'exécution de l'expérience de n'importe quelle autre manière (par exemple, pendant les tests), la variable `prolific_participant_id` sera définie à -1. La même logique s'applique à l'ID d'étude Prolific (`prolific_study_id`) et à l'ID de session Prolific (`prolific_session_id`).


```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('Les informations Prolific sont disponibles')
    var prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    var prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    var prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('Les informations Prolific ne sont pas disponibles (valeurs définies à -1)')
    var prolific_participant_id = -1
    var prolific_study_id = -1
    var prolific_session_id = -1
}
console.log('prolific_participant_id = ' + prolific_participant_id)
console.log('prolific_study_id = ' + prolific_study_id)
console.log('prolific_session_id = ' + prolific_session_id)
```


## Testez l'étude

Retournez sur la page Détails de l'étude sur Prolific. En bas de la page, il y a un bouton Aperçu. Cela vous permet de tester l'expérience en agissant comme un participant vous-même. N'oubliez pas de vérifier les résultats JATOS pour vous assurer que l'expérience s'est terminée avec succès et que toutes les informations nécessaires (y compris les informations Prolific) ont été enregistrées !