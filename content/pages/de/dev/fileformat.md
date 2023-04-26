title: Dateiformat (.osexp)
hash: 310dc6efe4055dac4dd14eda896adcf8c98e4a4f1950bb613ed0c1fd461c5ebc
locale: de
language: German

[TOC]

## Das .osexp Format

OpenSesame Experimente werden im `.osexp` Format gespeichert. Was eine `.osexp` Datei ist, hängt davon ab, ob Dateien im Experiment enthalten sind, also ob der Datei-Pool leer ist oder nicht.

## Wenn der Datei-Pool leer ist

Wenn der Datei-Pool leer ist, wird das Experiment als reine Textdatei gespeichert. Diese Datei ist utf-8 kodiert und verwendet Unix-artige Zeilenumbrüche. Sie können diese Datei in den meisten Texteditoren bearbeiten und anzeigen.

Die OpenSesame-Script-Syntax wird hier beschrieben:

- %link:opensesame-script%

## Wenn der Datei-Pool nicht leer ist

Wenn Dateien im Datei-Pool vorhanden sind, wird das Experiment als `.tar.gz` Datei gespeichert, ein `.zip`-ähnliches Dateiformat. Innerhalb dieser Datei finden Sie Folgendes:

- `script.opensesame` ist das experimentelle Skript, im gleichen Format wie oben beschrieben
- `pool/` ist ein Ordner, der alle Dateien im Datei-Pool enthält. Nicht-ASCII-Zeichen in den Dateinamen werden durch `U+XXXX` Strings ersetzt.

## Was ist mit den .opensesame und .opensesame.tar.gz Formaten passiert?

Sie können das `.opensesame` und `.opensesame.tar.gz` Format, das für OpenSesame <= 2.9.X verwendet wurde, weiterhin öffnen. Es ist jedoch nicht mehr möglich, Experimente in diesem Format zu speichern.