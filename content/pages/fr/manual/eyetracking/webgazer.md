title: WebGazer.js
hash: 47ee55649881bcf2ff92c750daeac0bdea5feb3a8719e0e99c5309e49686ecc6
locale: fr
language: French

Nécessite OSWeb v1.4.6.1
{:.page-notification}

[TOC]


## À propos de WebGazer

WebGazer.js est une bibliothèque de suivi oculaire écrite en JavaScript. Vous pouvez l'inclure avec OSWeb pour effectuer un suivi oculaire dans des expériences en ligne.

- <https://webgazer.cs.brown.edu/>


## Inclure WebGazer.js dans l'expérience

WebGazer.js n'est pas inclus par défaut avec OSWeb. Cependant, vous pouvez l'inclure en tant que bibliothèque externe en entrant un lien vers `webgazer.js` dans les bibliothèques JavaScript externes. Actuellement, un lien fonctionnel est :

```
https://webgazer.cs.brown.edu/webgazer.js
```

Voir aussi :

- %link:manual/osweb/osweb%


## Expérience exemple

Vous pouvez télécharger ci-dessous une expérience exemple qui utilise WebGazer.js. Les participants sont d'abord invités à cliquer sur et à regarder un ensemble de points ; cela amènera WebGazer.js à effectuer automatiquement quelque chose qui ressemble à une procédure d'étalonnage. Ensuite, l'expérience montre un écran simple pour tester la précision de l'enregistrement de la position du regard. En général, un suivi oculaire à grain fin n'est pas réalisable, mais vous pouvez dire dans quel quadrant de l'écran un participant regarde. Pour exécuter cette expérience, vous devez inclure WebGazer.js dans l'expérience, comme décrit ci-dessus.

- %static:attachments/webgazer.osexp%

Vous pouvez également lancer l'expérience directement dans le navigateur :

- <https://jatos.mindprobe.eu/publix/BowSAFY2VWl>