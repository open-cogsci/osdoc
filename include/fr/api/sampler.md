<div class="ClassDoc YAMLDoc" markdown="1">

# classe __Sampler__

La classe `Sampler` fournit des fonctionnalités pour jouer des échantillons sonores. Vous 
créez généralement un objet `Sampler` avec la fonction usine `Sampler()`, 
comme décrit dans la section [Créer un Sampler](#creating-a-sampler).

__Exemple :__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
my_sampler.play()
~~~

[TOC]

## Choses à savoir

### Créer un Sampler

Vous créez généralement un `Sampler` avec la fonction usine `Sampler()`, qui
prend le chemin complet vers un fichier sonore comme premier argument.

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
~~~

Facultativement, vous pouvez passer [Mots-clés de lecture](#playback-keywords) à `Sampler()`
pour définir le comportement par défaut :

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
~~~

### Taux d'échantillonnage

Si vous trouvez que votre échantillon se lit trop lentement (tonalité basse) ou trop rapidement (tonalité élevée),
assurez-vous que le taux d'échantillonnage de votre échantillon correspond au taux d'échantillonnage du backend de l'échantillonneur tel que spécifié dans les paramètres backend.

### Formats de fichier pris en charge

Les fichiers son au format `.wav`, `.mp3` et `.ogg` sont pris en charge. Si vous devez
convertir des échantillons à partir d'un autre format, vous pouvez utiliser
[Audacity](http://sourceforge.net/projects/audacity/).

### Mots-clés de lecture

Les fonctions qui acceptent `**playback_args` prennent les arguments clés suivants :

- `volume` spécifie un volume entre `0.0` (silencieux) et `1.0` (maximum).
- `pitch` spécifie une hauteur (ou vitesse de lecture), où les valeurs > 1 indiquent une
  hauteur plus élevée, et les valeurs < 1 indiquent une hauteur plus basse.
- `pan` spécifie une panoramique, où les valeurs < 0 indiquent une panoramique vers la gauche, et
  les valeurs > 0 indiquent une panoramique vers la droite. Alternativement, vous pouvez régler pan sur
  'left' ou 'right' pour ne jouer qu'un seul canal.
- `duration` spécifie la durée du son en millisecondes, ou est défini sur
  `0` ou `None` pour jouer le son complet.
- `fade_in` spécifie le temps de fondu d'entrée (ou d'attaque) du son, ou est défini sur
  `0` ou `None` pour désactiver le fondu d'entrée.
- `block` indique si l'expérience doit bloquer (`True`) pendant
  la lecture ou pas (`False`).

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.play(volume=.5, pan='left')
~~~

Les mots-clés de lecture n'affectent que l'opération en cours (sauf lorsqu'ils sont passés à
`Sampler()` lors de la création de l'objet). Pour changer le comportement pour toutes les
opérations ultérieures, définissez les propriétés de lecture directement :

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.volume = .5
my_sampler.pan = 'left'
my_sampler.play()
~~~

Ou passez les mots-clés de lecture à `Sampler()` lors de la création de l'objet :

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~

## close_sound(experiment)

Ferme le mixeur après la fin de l'expérience.


__Paramètres__

- **experiment**: L'objet expérimental.


## init_sound(experiment)

Initialise le mixeur pygame avant le début de l'expérience.


__Paramètres__

- **experiment**: L'objet expérimental.


## is_playing(self)

Vérifie si un son est en cours de lecture.



__Renvoie__

- True si un son est en cours de lecture, False sinon.

__Exemple__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
if my_sampler.is_playing():
        print('Le Sampler est toujours en cours de lecture!')
~~~



## pause(self)

Met en pause la lecture (le cas échéant).



__Exemple__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~



## play(\*arglist, \*\*kwdict)

Joue le son.


__Paramètres__

- **\*\*playback_args**: Facultative [mots-clés de lecture](#playback-keywords) qui seront utilisés
pour cet appel à `Sampler.play()`. Cela n'affecte pas les opérations suivantes.

__Exemple__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play(pitch=.5, block=True)
~~~



## resume(self)

Reprend la lecture (le cas échéant).



__Exemple__

~~~ .python
src = pool['my_sound.ogg']
mon_sampler = Sampler(src)
mon_sampler.play()
sleep(100)
mon_sampler.pause()
sleep(100)
mon_sampler.resume()
~~~



## set_config(\*\*cfg)

Met à jour les éléments configurables.


__Paramètres__

- **\*\*cfg**: Les éléments configurables à mettre à jour.


## stop(self)

Arrête le son en cours de lecture (le cas échéant).



__Exemple__

~~~ .python
src = pool['my_sound.ogg']
mon_sampler = Sampler(src)
mon_sampler.play()
sleep(100)
mon_sampler.stop()
~~~



## wait(self)

Bloque jusqu'à ce que le son ait fini de jouer ou renvoie immédiatement
si aucun son n'est en cours de lecture.



__Exemple__

~~~ .python
src = pool['my_sound.ogg']
mon_sampler = Sampler(src)
mon_sampler.play()
mon_sampler.wait()
print("Le sampler est terminé !")
~~~



</div>