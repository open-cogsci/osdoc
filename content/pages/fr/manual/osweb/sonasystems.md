title: Systèmes Sona
hash: d944a35b3e0c80d34ad14fc5152e628c6249312a06e28b86e5e6da4470fa60a2
locale: fr
language: French

[TOC]


## À propos de Sona Systems

Sona Systems est un outil en ligne utilisé par de nombreuses universités pour recruter des participants, accorder des crédits de cours à des étudiants participants, etc.

Voir aussi :

- <https://www.sona-systems.com/help/integration_test.aspx>


## Créer une étude sur JATOS

Premièrement, importez votre expérience sur JATOS, comme décrit ci-dessus. Ensuite, allez dans le Gestionnaire de Travailleur & Lot, activez le Travailleur Multiple Général, obtenez une URL en cliquant sur Obtenir un Lien, et copiez-la.


## Créer une étude sur Sona Systems

Ensuite, créez une étude sur Sona Systems. Insérez l'URL d'étude JATOS dans le champ intitulé "URL de l'étude". Cela indiquera à Sona Systems comment démarrer l'expérience. De manière importante, ajoutez le suivant à la fin de l'URL (cela transmettra l'ID de Sona du participant à votre expérience) :

```bash
&SONA_ID=%SURVEY_CODE% 
```

Sona Systems n'utilise pas une URL de redirection. Cela signifie que Sona Systems ne saura pas automatiquement si le participant a terminé l'étude ou non.


## Enregistrez l'ID Sona dans votre expérience

Chaque participant de Sona est identifié par un ID unique. Il est important d'enregistrer cet ID dans votre expérience, car cela vous permet de dire quel participant de Sona correspond à quelle entrée dans les résultats de JATOS. Vous pouvez le faire en ajoutant le script ci-dessous dans la phase de préparation d'un élément `inline_javascript` au tout début de votre expérience.

Lors de l'exécution de l'expérience via Sona, cela rendra l'ID de Sona disponible en tant que variable expérimentale `sona_participant_id`. Lors de l'exécution de l'expérience de toute autre manière (par exemple, lors des tests), la variable `sona_participant_id` sera définie sur -1.


```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('Les informations de Sona sont disponibles')
    var sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('Les informations de Sona ne sont pas disponibles (valeur définie à -1)')
    var sona_participant_id = -1
}
console.log('sona_participant_id = ' + sona_participant_id)
```


## Accorder automatiquement des crédits à la fin de l'étude

Sona Systems fournit une URL d'achèvement (côté client), qui doit être appelée lorsqu'une étude est réussie, afin que Sona Systems puisse accorder un crédit au participant (voir %FigCompletionURL).

%--
figure:
 id: FigCompletionURL
 source: completion-url.png
 caption: L'URL d'achèvement dans les informations de l'étude Sona Systems.
--%

L'URL d'achèvement (côté client) a trois arguments en elle:

- `experiment_id` qui identifie l'étude et est la même pour tous les participants
- `credit_token` qui (apparemment) change lorsque vous modifiez les informations de l'étude, mais est sinon la même pour tous les participants
- `survey_code` qui correspond à l'ID du Participant Sona, et est donc différent pour chaque participant

Copiez l'URL d'achèvement, et remplacez les `XXX` par `[SONA_ID]`. Allez dans les Propriétés de l'Étude sur JATOS, et insérez l'URL résultante dans le champ URL de Redirection de Fin.

%--
figure:
 id: FigEndRedirectURL
 source: end-redirect-url.png
 caption: L'URL de redirection à la fin dans les propriétés de l'étude JATOS.
--%