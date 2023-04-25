title: OpenSesameRun（无图形界面）
hash: 435d6b0358c5bdd011dbe66206d56d78258410aadf1b385e46d7c8fedd2aecb2
locale: zh
language: Chinese

## 关于

`opensesamerun` 是一个简单的工具，允许你用最小的图形用户界面执行 OpenSesame 实验，或者直接通过命令行指定所有必要的选项。如果没有指定所有命令行选项，特别是实验文件、受试者编号和日志文件，将自动显示最小的图形用户界面。

~~~
用法: opensesamerun [experiment] [options]

选项:
  --version             显示程序的版本号并退出
  -h, --help            显示帮助信息并退出

  受试者和日志文件选项:
    -s SUBJECT, --subject=SUBJECT
                        受试者编号
    -l LOGFILE, --logfile=LOGFILE
                        日志文件

  显示选项:
    -f, --fullscreen    全屏运行
    -c, --custom_resolution
                        不使用实验文件中指定的显示分辨率
    -w WIDTH, --width=WIDTH
                        显示宽度
    -e HEIGHT, --height=HEIGHT
                        显示高度

  杂项选项:
    -d, --debug         将大量调试信息打印到标准输出
    --stack             打印堆栈信息

  杂项选项:
    --pylink            在 PyGame 之前加载 PyLink（在非虚拟模式下使用 Eyelink 插件所必需）
~~~

## 示例

假设你想要运行凝视线索示例实验，对于受试者＃1，并将日志文件保存在你的文档文件夹中（此示例假设为 Linux，但在其他平台上也类似地工作）：

~~~
opensesamerun /usr/share/opensesame/examples/gaze_cuing.opensesame.tar.gz -s 1 -l /home/sebastiaan/Documents/subject1.tsv -f 
~~~


## 替代的 `libopensesame`

您还可以通过 `libopensesame` Python 模块在不使用 GUI 的情况下启动实验:

- %link:manual/python/nogui%