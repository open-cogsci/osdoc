title: Tobii
hash: b29e3b34f4a2f2600b95bc2d17497c21e352fb3a5834b0f4061bd6cd27e4e3dd
locale: fr
language: French

## Installation de Tobii research

`tobii-research` est la bibliothèque Python permettant la prise en charge de Tobii. Actuellement, `tobii-research` ne prend en charge que Python 3.10 et les versions antérieures, tandis que les paquets standards d’OpenSesame sont construits avec Python 3.13. Par conséquent, vous devez utiliser la version d’OpenSesame pour Python 3.10 (ou antérieure) disponible sur [GitHub releases](https://github.com/open-cogsci/OpenSesame/releases).

Ensuite, `tobii-research` peut être installé :

```
pip install tobii-research
```

Pour plus d’informations, consultez :

- <http://www.tobii.com/en/eye-tracking-research/global/>


## PyGaze

Après avoir installé `tobii-research`, vous pouvez utiliser Tobii avec PyGaze ! Voir :

- %link:pygaze%


## Plugin Titta de poursuite oculaire

Bob Rosbag, Diederick C. Niehorster et Marcus Nyström ont développé leurs propres plug-ins Tobii pour OpenSesame. Ces plug-ins sont assez similaires à ceux de PyGaze, mais offrent certaines fonctionnalités qui ne sont pas disponibles via PyGaze et peuvent aussi être plus stables. Pour installer ces plug-ins, exécutez :

```
pip install opensesame-plugin-titta-eyetracking
```

Pour plus d’informations, veuillez visiter :

- <https://github.com/dev-jam/opensesame-plugin-titta_eyetracking>