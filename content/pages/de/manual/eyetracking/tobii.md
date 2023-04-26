title: Tobii
hash: 91075c11d390d9162057a382ddc27a006029b42c7c7c79882ad81ff5e90f4430
locale: de
language: German

PyGaze bietet *experimentelle* Unterstützung für Tobii Eye Tracker. Das `tobii-research` Paket kann über `pip` installiert werden, aber zum Zeitpunkt des Schreibens erfordert es eine bestimmte Version von Python - und *welche* Version von Python es erfordert, variiert von Veröffentlichung zu Veröffentlichung. Daher ist der erste Schritt herauszufinden, welche Version von Python Sie benötigen. Sie können das tun, indem Sie die `tobii-research` auf PyPi besuchen und auf 'Download-Dateien' klicken:

- <https://pypi.org/project/tobii-research/#files>

Anhand der Dateinamen können Sie erkennen, welche Version von Python Sie benötigen; zum Beispiel bedeutet das `cp310` im Namen 
`tobii_research-1.10.2-cp310-cp310-win_amd64.whl`, dass Sie Python 3.10 benötigen (`cp` steht für C-Python).

Installieren Sie als Nächstes OpenSesame in einer Python-Umgebung der richtigen Version (also Python 3.10 für Version 1.10.2 des `tobii-research`, wie oben gezeigt). Dies ist am einfachsten mit Anaconda zu erledigen, wie [hier](%url:download%) beschrieben. Installieren Sie abschließend das `tobii-research` Paket in dieser Python-Umgebung.

```
!pip install tobii-research
```


Für weitere Informationen, siehe:

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>