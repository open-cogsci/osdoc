title: Systèmes Sona
hash: b16a73f1e8a3fb7fd7efb983a26825940c0de47ec814bf27280a22d31c398657
locale: fr
language: French

[TOC]


## À propos de Sona Systems

Sona Systems est un outil en ligne que de nombreuses universités utilisent pour recruter des participants, accorder des crédits de cours aux participants étudiants, etc.

Voir aussi :

- <https://www.sona-systems.com/help/integration_test.aspx>


## Créer une étude sur JATOS

D'abord, importez votre expérience dans JATOS, comme décrit ci-dessus. Ensuite, allez dans le Gestionnaire de travailleurs et de lots, activez le travailleur général multiple, obtenez une URL en cliquant sur Obtenir un lien, et copiez-la.


## Créer une étude sur Sona Systems

Ensuite, créez une étude sur Sona Systems. Insérez l'URL de l'étude JATOS dans le champ intitulé "Study URL". Cela indiquera à Sona Systems comment démarrer l'expérience. Importantly, ajoutez ce qui suit à la fin de l'URL (cela passera l'ID Sona du participant à votre expérience) :

```bash
&SONA_ID=%SURVEY_CODE% 
```

Sona Systems n'utilise pas d'URL de redirection. Cela signifie que Sona Systems ne saura pas automatiquement si le participant a terminé l'étude ou non.


## Enregistrez l'ID Sona dans votre expérience

Chaque participant de Sona est identifié par un ID unique. Il est important de consigner cet ID dans votre expérience, car cela vous permet de savoir quel participant de Sona correspond à quelle entrée dans les résultats de JATOS. Vous pouvez le faire en ajoutant le script ci-dessous dans la phase de préparation d'un élément `inline_javascript` au tout début de votre expérience.

Lors de l'exécution de l'expérience via Sona, cela rendra l'ID Sona disponible en tant que variable expérimentale `sona_participant_id`. Lors de l'exécution de l'expérience d'une autre manière (par exemple pendant les tests), la variable `sona_participant_id` sera définie sur -1. 

```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('Les informations Sona sont disponibles')
    vars.sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('Les informations Sona ne sont pas disponibles (valeur fixée à -1)')
    vars.sona_participant_id = -1
}
console.log('sona_participant_id = ' + vars.sona_participant_id)
```

## Accorder automatiquement des crédits à la fin de l'étude

Sona Systems fournit une URL de fin (côté client), qui doit être appelée lorsqu'une étude est terminée avec succès, afin que Sona Systems puisse accorder des crédits au participant (voir %FigCompletionURL).

%--
figure:
 id: FigCompletionURL
 source: completion-url.png
 légende: L'URL de fin dans les informations de l'étude Sona Systems.
--%

L'URL de fin (côté client) a trois arguments :

- `experiment_id` qui identifie l'étude et est la même pour tous les participants
- `credit_token` qui (apparemment) change lorsque vous modifiez les informations de l'étude, mais est sinon la même pour tous les participants
- `survey_code` qui correspond à l'ID de participant Sona, et est donc différent pour chaque participant

Copiez l'URL de fin et remplacez les `XXX` par `[SONA_ID]`. Allez dans les propriétés de l'étude sur JATOS et insérez l'URL résultante dans le champ URL de fin de redirection.

%--
figure:
 id: FigEndRedirectURL
 source: end-redirect-url.png
 légende: L'URL de fin de redirection dans les propriétés de l'étude JATOS.
--%