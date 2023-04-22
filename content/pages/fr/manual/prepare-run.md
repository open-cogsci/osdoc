title: La stratégie de préparation-exécution
hash: e91e8e57fbac78eb05547ef89cd9bbb3ae1f177e7d96e295fb31c6e7da95965d
locale: fr
language: French

[TOC]

## À propos

Les expériences sont généralement composées de courts intervalles ('trials') durant lesquels les participants perçoivent des stimuli et effectuent une tâche. Le temps doit être contrôlé pendant un trial, mais une certaine variation imprévisible de la durée de l'intervalle entre les trials est acceptable. Il est donc judicieux d'effectuer des tâches chronophages avant un trial et de réduire au minimum les opérations effectuées pendant un trial.

OpenSesame fait cela en appelant chaque élément d'un élément SEQUENCE deux fois. Il s'agit de la *stratégie de préparation-exécution* :

- Pendant la phase de préparation, les éléments ont l'opportunité de se préparer. Par exemple, un SYNTH génère un son (mais ne le joue pas) ; et un SKETCHPAD dessine un canevas (mais ne l'affiche pas).
- Pendant la phase d'exécution, les éléments font le moins possible. Par exemple, un SYNTH lit un son préparé précédemment ; et un SKETCHPAD montre un canevas préparé précédemment.

Cela réduit le risque de problèmes de temporisation. La stratégie de préparation-exécution est mise en œuvre au niveau des éléments SEQUENCE, qui contiennent généralement les parties critiques en termes de temps d'une expérience. Cela signifie qu'avant qu'une SEQUENCE ne démarre, il y a une certaine gigue temporelle imprévisible.

## Notes spécifiques aux éléments

### éléments loop

Un élément LOOP n'est pas préparé à l'avance. Il est important de prendre cela en compte lors de l'utilisation d'un LOOP pour mettre en œuvre des parties temporellement critiques. Par exemple, vous pouvez être tenté d'implémenter un flux RSVP à l'aide d'un élément LOOP comme suit :

~~~text
rsvp_loop item (4 cycles)
- stimulus_item
~~~

Dans cette construction, *stimulus_item* sera préparé et exécuté quatre fois en alternance, comme ceci :

~~~text
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
~~~

Il est donc nécessaire de vérifier que la préparation de *stimulus_item* ne provoque pas de problèmes de temporisation.

### éléments sequence

Tous les éléments faisant partie d'une SEQUENCE sont préparés à l'avance. Par conséquent, la construction suivante ...

~~~text
trial_sequence
- fixation_sketchpad
- target_sketchpad
- keyboard_response
- logger
~~~

... sera exécutée comme suit ...

~~~text
prepare fixation_sketchpad
prepare target_sketchpad
prepare keyboard_response
prepare logger
run fixation_sketchpad
run target_sketchpad
run keyboard_response
run logger
~~~

### éléments sketchpad et feedback

Les éléments SKETCHPAD et FEEDBACK diffèrent dans leur préparation. Pour les SKETCHPAD, la préparation se fait lors de la phase de préparation ; pour les éléments FEEDBACK, la préparation ne se fait que lors de la phase d'exécution.

Pour plus d'informations, voir :

- %link:manual/stimuli/visual%

### éléments synth et sampler

Pour les éléments SYNTH et SAMPLER, le son est généré et préchargé pendant la phase de préparation.

### éléments inline_script

Dans un élément INLINE_SCRIPT, vous pouvez choisir comment vous souhaitez implémenter la stratégie de préparation et d'exécution. En général, il est recommandé de suivre les directives suivantes :

- Les fonctionnalités de préparation chronophages sont insérées dans la phase de préparation. Par exemple, créer des objets canevas et générer des sons.
- Un minimum de code est placé dans la phase d'exécution. Par exemple, afficher uniquement un canevas préparé précédemment.

### Autres éléments et plugins

En général, les éléments doivent suivre le principe visant à effectuer autant que possible une préparation chronophage lors de la phase de préparation et à minimiser la phase d'exécution. Cependant, chaque plugin est implémenté différemment. Si vous avez des doutes sur un cas spécifique, n'hésitez pas à poser une question sur le forum.

## Expressions conditionnelles (run if, show if, break if, etc)

Dans les éléments SEQUENCE, la condition 'Run if' est évaluée au dernier moment, pendant la phase d'exécution. Ainsi, vous pouvez utiliser une condition comme `correct == 0`, qui dépend des résultats d'un élément KEYBOARD_RESPONSE qui a été appelé juste avant. Il est important de prendre en compte que l'expression 'Run if' s'applique *uniquement* à la phase d'exécution d'un élément - La phase de préparation est *toujours* exécutée.

Dans les éléments COROUTINES, la condition 'Exécuter si' est évaluée pendant la phase de Préparation. Par conséquent, les conditions ne peuvent pas dépendre des événements qui se produisent pendant l'exécution des COROUTINES.

Dans les éléments SKETCHPAD, la condition 'Afficher si' est évaluée pendant la phase de Préparation, lorsque le canevas est construit. Dans les éléments FEEDBACK, la condition 'Afficher si' est évaluée pendant la phase d'Exécution (car le canevas n'est construit que durant la phase d'Exécution).