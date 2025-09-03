title: Tobii
hash: b29e3b34f4a2f2600b95bc2d17497c21e352fb3a5834b0f4061bd6cd27e4e3dd
locale: de
language: German

## Installation von Tobii research

`tobii-research` ist die Python-Bibliothek für Tobii-Unterstützung. Derzeit unterstützt `tobii-research` nur Python 3.10 und früher, während die Standardpakete von OpenSesame mit Python 3.13 erstellt werden. Daher müssen Sie das OpenSesame-Paket für Python 3.10 (oder früher) von [GitHub-Releases](https://github.com/open-cogsci/OpenSesame/releases) verwenden.

Anschließend kann `tobii-research` installiert werden:

```
pip install tobii-research
```

Für weitere Informationen siehe:

- <http://www.tobii.com/en/eye-tracking-research/global/>


## PyGaze

Nachdem Sie `tobii-research` installiert haben, können Sie Tobii mit PyGaze verwenden! Siehe:

- %link:pygaze%


## Titta Eye-Tracking-Plugin

Bob Rosbag, Diederick C. Niehorster & Marcus Nyström haben eigene Tobii-Plugins für OpenSesame entwickelt. Diese ähneln den PyGaze-Plugins, bieten jedoch einige Funktionen, die über PyGaze nicht verfügbar sind, und können zudem stabiler sein. Um diese Plugins zu installieren, führen Sie aus:

```
pip install opensesame-plugin-titta-eyetracking
```

Für weitere Informationen besuchen Sie bitte:

- <https://github.com/dev-jam/opensesame-plugin-titta_eyetracking>
