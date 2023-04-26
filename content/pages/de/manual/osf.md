title: Integration mit dem Open Science Framework
hash: b86c05caa254209c5f4d161cd5c5a9daffef60ec5e5d5fca41a7aec00643d1f7
locale: de
language: German

[TOC]

## Über

Die OpenScienceFramework-Erweiterung verbindet OpenSesame mit dem [Open Science Framework](https://osf.io) (OSF), einer Webplattform zum Teilen, Verbinden und Vereinfachen wissenschaftlicher Arbeitsprozesse. Um diese Erweiterung zu nutzen, [benötigen Sie ein OSF-Konto](https://osf.io/login/?sign_up=True).

Mit der OpenScienceFramework-Erweiterung können Sie:

- Ihr Experiment automatisch im OSF speichern
- Daten automatisch im OSF hochladen
- Experimente aus dem OSF öffnen
- Ihr Experiment und Daten mit anderen Forschern teilen, indem Sie ihnen Zugang über das OSF geben

## Anmeldung beim OSF

Um sich beim OSF anzumelden:

- Erstellen Sie ein Konto auf <https://osf.io>. (Es ist nicht möglich, ein Konto innerhalb von OpenSesame zu erstellen.)
- Klicken Sie in OpenSesame auf die Schaltfläche "Anmelden" in der Hauptwerkzeugleiste und geben Sie Ihre Anmeldedaten ein.
- Sobald Sie angemeldet sind, können Sie den OSF-Explorer öffnen, indem Sie auf Ihren Namen klicken, wo sich früher die Schaltfläche "Anmelden" befand, und *Explorer anzeigen* auswählen. Der Explorer zeigt eine Übersicht über alle Ihre OSF-Projekte und alle Repositories/Cloud-Dienste, die mit Ihren Projekten verknüpft sind.

## Verknüpfen eines Experiments mit dem OSF

Wenn Sie ein Experiment mit dem OSF verknüpfen, wird jedes Mal, wenn Sie das Experiment in OpenSesame speichern, auch eine neue Version im OSF hochgeladen.

Um ein Experiment zu verknüpfen:

- Speichern Sie das Experiment auf Ihrem Computer.
- Öffnen Sie den OSF-Explorer und wählen Sie einen Ordner oder Repository, in dem Sie Ihr Experiment im OSF speichern möchten. Klicken Sie mit der rechten Maustaste auf diesen Ordner und wählen Sie *Experiment mit diesem Ordner synchronisieren*. Der OSF-Knoten, mit dem das Experiment verknüpft ist, wird oben im Explorer angezeigt.
- Das Experiment wird dann an den ausgewählten Ort hochgeladen.
- Wenn Sie *Immer Experiment beim Speichern hochladen* aktivieren, wird bei jedem Speichern automatisch eine neue Version im OSF gespeichert. Wenn Sie diese Option nicht aktivieren, werden Sie jedes Mal gefragt, ob Sie dies tun möchten oder nicht.

Um die Verknüpfung eines Experiments aufzuheben:

- Öffnen Sie den OSF-Explorer und klicken Sie auf die Schaltfläche *Verknüpfung aufheben* neben dem Link *Experiment verknüpft mit*.

## Verknüpfen von Daten mit dem OSF

Wenn Sie Daten mit dem OSF verknüpfen, wird jedes Mal, wenn Daten gesammelt wurden (normalerweise nach jeder experimentellen Sitzung), auch diese Daten im OSF hochgeladen.

Um Daten mit dem OSF zu verknüpfen:

- Speichern Sie das Experiment auf Ihrem Computer.
- Öffnen Sie den OSF-Explorer, klicken Sie mit der rechten Maustaste auf den Ordner, in den die Daten hochgeladen werden sollen, und wählen Sie *Daten mit diesem Ordner synchronisieren*. Der OSF-Knoten, mit dem die Daten verknüpft sind, wird oben im Explorer angezeigt.
- Wenn Sie *Immer gesammelte Daten hochladen* aktivieren, werden Daten automatisch im OSF gespeichert, nachdem sie gesammelt wurden. Wenn Sie diese Option nicht aktivieren, werden Sie jedes Mal gefragt, ob Sie dies tun möchten oder nicht.

Um die Verknüpfung von Daten mit dem OSF aufzuheben:

- Öffnen Sie den OSF-Explorer und klicken Sie auf die Schaltfläche *Verknüpfung aufheben* neben dem Link *Daten gespeichert in*.

## Öffnen eines im OSF gespeicherten Experiments

Um ein Experiment aus dem OSF zu öffnen:

- Öffnen Sie den OSF-Explorer und suchen Sie das Experiment.
- Klicken Sie mit der rechten Maustaste auf das Experiment und wählen Sie *Experiment öffnen*.
- Speichern Sie das Experiment auf Ihrem Computer.

## Behandlung nicht übereinstimmender Versionen

Wenn Sie ein Experiment auf Ihrem Computer öffnen, das mit dem OSF verknüpft ist, aber von der Version im OSF abweicht, werden Sie gefragt, was Sie tun möchten:

- Verwenden Sie die Version von Ihrem Computer; oder
- Verwenden Sie die Version aus dem OSF. Wenn Sie sich für die Verwendung der Version aus dem OSF entscheiden, wird diese heruntergeladen und überschreibt das Experiment auf Ihrem Computer.

## Installation der OpenScienceFramework-Erweiterung

Die OpenScienceFramework-Erweiterung ist standardmäßig im Windows-Paket von OpenSesame installiert. Wenn die Erweiterung nicht installiert ist, können Sie sie wie folgt installieren:

Aus PyPi:

~~~
pip install opensesame-extension-osf
~~~

In einer Anaconda-Umgebung:

~~~
conda install -c cogsci opensesame-extension-osf
~~~

Der Quellcode der Erweiterung steht auf GitHub zur Verfügung:

- <https://github.com/dschreij/opensesame-extension-osf>

Und für das Modul `python-qosf`, das von der Erweiterung verwendet wird:

- <https://github.com/dschreij/python-qosf>