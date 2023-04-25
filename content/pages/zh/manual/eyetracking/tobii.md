title: Tobii
hash: 91075c11d390d9162057a382ddc27a006029b42c7c7c79882ad81ff5e90f4430
locale: zh
language: Chinese

PyGaze 为 Tobii 眼动跟踪器提供*实验性*支持。可以通过`pip`安装`tobii-research`包，但在撰写本文时，它需要特定版本的Python——需要*哪个*版本的Python因发布版本而异。因此，第一步是找出你需要哪个版本的Python。你可以通过访问PyPi上的`tobii-research`并点击“下载文件”来实现这一点：

- <https://pypi.org/project/tobii-research/#files>

从文件名中，你可以知道需要哪个版本的Python；例如，在名称中的`cp310`代表你需要Python 3.10（`cp`代表C-Python）。

接下来，在正确版本的Python环境中安装OpenSesame（如上所示，对于`tobii-research`的1.10.2版本，需要Python 3.10）。这可以使用Anaconda轻松完成，如[此处](%url:download%)所述。最后，将`tobii-research`包安装到这个Python环境中。

```
!pip install tobii-research
```


更多信息请查看：

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>