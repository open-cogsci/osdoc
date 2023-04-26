title: Wiederholungszyklus
hash: 8b04755715703af99fbd951772e0c47a5a1abbf7dcaac1e5ab6f9665cd07cb2c
locale: de
language: German

Dieses Plug-in ermöglicht es Ihnen, Zyklen aus einer `loop` zu wiederholen. Am häufigsten wird dies verwendet, um einen Versuch zu wiederholen, wenn ein Teilnehmer einen Fehler gemacht hat oder zu langsam war.

Um zum Beispiel alle Versuche zu wiederholen, bei denen eine Antwort langsamer als 3000 ms war, können Sie ein `repeat_cycle`-Element nach (typischerweise) dem `keyboard_response` hinzufügen und die folgende Wiederholen-wenn-Aussage hinzufügen:

```bash
[response_time] > 3000
```

Sie können auch erzwingen, dass ein Zyklus wiederholt wird, indem Sie die Variable `repeat_cycle` in einem `inline_script` auf 1 setzen, wie folgt:

```python
var.repeat_cycle = 1
```