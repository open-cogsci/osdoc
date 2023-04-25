title: repeat_cycle
hash: 8b04755715703af99fbd951772e0c47a5a1abbf7dcaac1e5ab6f9665cd07cb2c
locale: zh
language: Chinese

此插件允许您从 `loop` 重复周期。通常，这将在参与者犯错或反应过慢时重复试验。

例如，要重复所有反应速度慢于3000毫秒的试验，您可以在（通常是）`keyboard_response` 之后添加一个 `repeat_cycle` 项目，并添加以下repeat-if语句：

```bash
[response_time] > 3000
```

您还可以通过在 `inline_script` 中设置变量 `repeat_cycle` 为 1 来强制重复一个周期，如下所示：

```python
var.repeat_cycle = 1
```