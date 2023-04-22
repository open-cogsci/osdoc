title: Réinitialiser_retour
hash: 1bac08e9d7c690dc8199e762ae4574622cf3faa0486e3ecdcb98823269756ab7
locale: fr
language: French

Ce plug-in a le même effet que de présenter un élément FEEDBACK avec une durée de 0 ms
{: .page-notification}

Si vous ne réinitialisez pas les variables de feedback, vous pouvez mélanger votre feedback avec des réponses qui ne sont pas pertinentes pour la tâche. Par exemple, les pressions de touches effectuées pendant la phase d'instruction peuvent affecter le feedback pendant le premier bloc de l'expérience. Par conséquent, vous devrez réinitialiser les variables de feedback aux moments appropriés.

Ce plug-in réinitialisera les variables suivantes à 0 :

- `total_response_time`
- `total_response`
- `acc`
- `accuracy`
- `avg_rt`
- `average_response_time`