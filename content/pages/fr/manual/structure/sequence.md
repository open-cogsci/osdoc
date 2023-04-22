title: Faire des choses en séquence
hash: 15313148d00600657d102430c4e197e7a888d543ca35e349a350210120cb1e11
locale: fr
language: French

L'élément SEQUENCE a deux fonctions importantes :

- Il exécute plusieurs autres éléments l'un après l'autre.
- Il détermine quels éléments doivent être exécutés et lesquels ne doivent pas l'être.

Les SEQUENCEs sont exécutées de haut en bas ; c'est-à-dire que l'élément situé en haut est exécuté en premier. L'ordre d'une SEQUENCE est toujours séquentiel.

## Expressions run-if

Vous pouvez utiliser des expressions run-if pour déterminer si un élément particulier doit être exécuté ou non. Par exemple, si vous souhaitez afficher un écran uniquement si un participant a donné une réponse incorrecte, vous pouvez définir les expressions run-if pour cet élément comme suit :

```python
{correct} == 0
```

Si vous laissez les expressions run-if vides ou saisissez `True`, l'élément sera toujours exécuté. Les expressions run-if utilisent la même syntaxe que les autres expressions conditionnelles. Pour plus d'informations, consultez :

- %link:manuel/variables%

Les expressions run-if n'affectent que les éléments exécutés, et non ceux qui sont préparés. Autrement dit, la phase de préparation de tous les éléments d'une SEQUENCE est toujours exécutée, indépendamment des expressions run-if. Voir également :

- %link:prepare-run%


## Désactiver les éléments

Pour désactiver complètement un élément dans une SEQUENCE, cliquez dessus avec le bouton droit de la souris et sélectionnez 'Disable' (Désactiver). Ceci est principalement utile lors du développement de votre expérience, par exemple pour contourner temporairement les instructions.