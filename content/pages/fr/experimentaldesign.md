title: Notation pour la conception expérimentale
hash: 060f0c16a9d8bf841b056d49c16778928d77563cfa43fa451a8ff159ed884b3b
locale: fr
language: French

Passer d'une question de recherche abstraite à un plan expérimental concret peut être difficile. Vous pouvez clarifier le plan pour vous-même en l'écrivant dans une notation formelle. Il existe de nombreuses notations, mais ici nous utiliserons celle proposée par [Rouanet et Lepine (1977)][références]. Cette notation est simple, mais suffisamment flexible pour couvrir la plupart des plans expérimentaux que vous rencontrerez dans la réalité.

[TOC]

## La notation de base

Dans cette notation, les conditions (ou facteurs) sont indiquées par une seule lettre, avec un petit nombre qui indique le nombre de niveaux. Par exemple, si vous avez trois durées de stimulus, vous pouvez l'indiquer comme D<sub>3</sub>. Une condition spéciale est 'sujet'. Si vous avez *N* sujets, vous indiquez cela comme <u>S</u><sub>N</sub>. Cela peut paraître étrange de se référer au sujet comme une condition, mais, en un sens, c'est exactement ce que c'est.

Il y a deux opérateurs :

- &lt; &gt; indique "boxing in", généralement utilisé pour les conditions qui varient entre les sujets
- × indique "croisement", généralement utilisé pour les conditions qui varient au sein des sujets

Il y a souvent plusieurs façons d'écrire un plan expérimental. Par exemple, vous pouvez omettre les conditions qui ne sont pas pertinentes pour votre question de recherche, telles que si un stimulus apparaît sur le côté gauche ou droit de l'affichage.

## Plans intra-sujet

Dans un plan intra-sujet, tous les participants réalisent toutes les conditions. C'est le type de plan le plus puissant, car il ne souffre pas beaucoup de la variabilité entre les participants : Vous pouvez comparer la performance d'un participant dans la condition A avec sa performance dans la condition B.

Considérons un paradigme d'orientation de Posner [(Posner, 1980)][références], dans lequel une flèche pointe vers le côté gauche ou droit de l'écran. La flèche est suivie d'une cible, qui apparaît également sur le côté gauche ou droit de l'écran. Nous avons donc deux conditions qui varient au sein des participants :

- *côté d'orientation* avec deux niveaux (gauche, droite) ou C<sub>2</sub>
- *côté cible* avec deux niveaux (gauche, droite) ou T<sub>2</sub>

Nous pouvons écrire ce plan comme <u>S</u><sub>N</sub>×C<sub>2</sub>×T<sub>2</sub>

## Plans inter-sujet

Dans un plan inter-sujet, différents participants réalisent différentes conditions expérimentales. Ce plan est moins puissant qu'un plan intra-sujet, car les différences entre les participants sont une source importante de bruit : Si la performance du participant 1 dans la condition A est meilleure que celle du participant 2 dans la condition B, vous ne savez pas si cela est dû à un effet de condition ou simplement parce que le participant 1 a tendance à mieux performer que le participant 2. Pour cette raison, les plans inter-sujet nécessitent un grand nombre de participants.

Prenons l'expérience célèbre (et controversée) de [Bargh (1996)][références] sur l'amorçage social, dans laquelle certains participants lisent des mots associés à la vieillesse (par exemple, "retraité"), tandis que d'autres participants lisent des mots neutres (par exemple, "assoiffé").

Nous avons donc une condition qui varie entre les participants :

- *type d'amorce* avec deux niveaux (vieux, neutre) ou P<sub>2<sub>

Nous pouvons écrire ce plan comme <u>S</u><sub>N</sub> &lt; P<sub>2</sub> &gt;

Rouanet et Lepine appellent cela l'*emboîtement*, ou "boxing in". Cela signifie simplement que les deux niveaux de P ont leur propre groupe de N sujets. Par conséquent, le nombre total de sujets est de 2*N.

## Plans compliqués

Occasionnellement, vous rencontrerez des plans plus compliqués qui ne sont pas facilement classés comme étant intra- ou inter-sujet. Les expériences en psycholinguistique sont de bons exemples de cela.

Prenons en considération une expérience d'amorçage sémantique, dans laquelle un mot cible est précédé soit par une amorce sémantiquement liée (par exemple, "jardin" -> "fleur" ou "chat" -> "chien") ou une amorce non liée (par exemple, "argent" -> "fleur" ou "oui" -> "chien"). Pour éviter que le participant voie un mot plusieurs fois, vous pouvez "faire tourner" les conditions entre les mots :

- Les participants impairs (1, 3, 5, etc.) font la rotation A :
    - 'fleur' est dans la condition liée
    - 'chien' est dans la condition non liée
- Les participants pairs (2, 4, 6, etc.) font la rotation B :
    - 'fleur' est dans la condition non liée
    - 'chien' est dans la condition liée

Nous avons donc deux conditions :

- *type d'amorce* avec deux niveaux (lié, non lié), ou P<sub>2</sub> ; ceci est varié au sein des sujets
- *rotation* avec deux niveaux (A, B), ou R<sub>2</sub> ; ceci est varié entre les participants

Par conséquent, le plan est <u>S</u><sub>n</sub> &lt; R<sub>2</sub> &gt; × P<sub>2</sub>

## Limitations

Cette notation a plusieurs limitations, notamment :

- Vous ne pouvez pas indiquer combien de fois certaines conditions se produisent. Par exemple, dans une tâche de guidage Posner, les essais valides (c'est-à-dire l'indice et la cible du même côté) se produisent généralement plus souvent que les essais invalides (c'est-à-dire l'indice et la cible sur des côtés opposés). Ceci ne peut pas être écrit dans la notation décrite ici.
- Il est difficile d'indiquer le rôle de 'l'élément' dans un plan. Par exemple, dans le plan sous [Conceptions compliquées], le mot cible joue un rôle similaire à celui du participant. Il est possible d'écrire un plan centré sur l'élément ou un plan centré sur le participant (comme dans l'exemple), mais je n'ai pas trouvé de moyen de faire les deux de manière satisfaisante.

## Références

<div class="reference" markdown="1">

Bargh, J. A., Chen, M., & Burrows, L. (1996). Automaticité du comportement social : effets directs de la construction du trait et de l'activation des stéréotypes sur l'action. *Journal of Personality and Social Psychology*, *71*(2), 230.

Posner, M. I. (1980). Orientation de l'attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25. doi:10.1080/00335558008248231

Rouanet, H., & Lepine, D. (1977). Structures linéaires et analyse des comparaisons. *Mathématiques et Sciences Humaines*, *56*, 5–46. Extrait de : <http://www.numdam.org/item?id=MSH_1977__56__5_0>

</div>