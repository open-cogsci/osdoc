title: Tobii
hash: a383da57d44200882bf0aa52f84f681e06fecc7982e5a785150b5372d2d75259
locale: zh
language: Chinese

PyGaze为Tobii眼球追踪器提供*试验性*支持。

`tobii-research`是支持Tobii的Python库。截至2023年7月，`tobii-research`需要Python 3.10，而OpenSesame默认使用Python 3.11。因此，在`tobii-research`升级至Python 3.11之前，通过Anaconda构建Python 3.10环境来安装含有Tobii支持的OpenSesame是最简单的方法。

这听起来很复杂，但实际上并不难。首先，阅读在下载页面上描述的通过Anaconda安装OpenSesame的一般步骤：

- %link:download%

接下来，理解了一般步骤后，开始创建一个Python 3.10环境，继续按照下载页面的说明进行，然后安装`tobii-research`：

```
# 首先，创建一个Python 3.10环境
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# 现在按照下载页面的说明进行
# ...
# 然后安装Tobii支持
pip install tobii-research
# 现在启动OpenSesame！
opensesame
```

若想获得更多信息，请参见：

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>