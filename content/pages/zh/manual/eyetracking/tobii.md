title: Tobii
hash: b29e3b34f4a2f2600b95bc2d17497c21e352fb3a5834b0f4061bd6cd27e4e3dd
locale: zh
language: Chinese

## 安装 Tobii research

`tobii-research` 是用于 Tobii 支持的 Python 库。目前，`tobii-research` 仅支持 Python 3.10 及更早版本，而 OpenSesame 的标准软件包是基于 Python 3.13 构建的。因此，你必须使用来自 [GitHub releases](https://github.com/open-cogsci/OpenSesame/releases) 的 OpenSesame Python 3.10（或更早版本）软件包。

接下来，可以安装 `tobii-research`：

```
pip install tobii-research
```

更多信息，请参见：

- <http://www.tobii.com/en/eye-tracking-research/global/>


## PyGaze

安装完 `tobii-research` 后，你就可以在 PyGaze 中使用 Tobii 了！参见：

- %link:pygaze%


## Titta 眼动追踪插件

Bob Rosbag、Diederick C. Niehorster 和 Marcus Nyström 为 OpenSesame 开发了他们自己的 Tobii 插件。这些插件在某种程度上与 PyGaze 插件类似，但提供了 PyGaze 中不具备的一些功能，并且可能更为稳定。要安装这些插件，请运行：

```
pip install opensesame-plugin-titta-eyetracking
```

更多信息，请访问：

- <https://github.com/dev-jam/opensesame-plugin-titta_eyetracking>
