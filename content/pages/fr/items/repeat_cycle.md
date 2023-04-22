title: cycle_de_répétition
hash: 8b04755715703af99fbd951772e0c47a5a1abbf7dcaac1e5ab6f9665cd07cb2c
locale: fr
language: French

Ce plug-in vous permet de répéter les cycles d'une `loop`. Le plus souvent, cela sera pour répéter un essai lorsqu'un participant a fait une erreur ou était trop lent.

Par exemple, pour répéter tous les essais sur lesquels une réponse a été plus lente que 3000 ms, vous pouvez ajouter un élément `repeat_cycle` après (généralement) le `keyboard_response` et ajouter l'instruction suivante de répétition si :

```bash
[response_time] > 3000
```

Vous pouvez également forcer un cycle à être répété en définissant la variable `repeat_cycle` à 1 dans un `inline_script`, comme ceci :

```python
var.repeat_cycle = 1
```