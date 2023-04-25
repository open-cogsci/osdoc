title: 鼠标追踪
hash: 7c506c47bfaddd3f6c3e7feb81897c91d1205de0af1cf2153dfddafcf2b88737
locale: zh
language: Chinese

Mousetrap是一个第三方插件，不由OpenSesame团队维护。
{: .alert .alert-info}

## 关于

Pascal Kieslich和Felix Henninger开发了OpenSesame的[mousetrap插件](https://github.com/PascalKieslich/mousetrap-os)[（Kieslich与Henninger，2017）](https://dx.doi.org/10.3758/s13428-017-0900-z)。这些插件允许您跟踪鼠标光标的移动，这已被用于研究许多心理领域中认知过程的时间进程[(Freeman, Dale, & Farmer, 2011)](https://dx.doi.org/10.3389/fpsyg.2011.00059)。

Mousetrap在OpenSesame中提供了两个鼠标跟踪插件，可以通过拖放将其包含在实验中。
[鼠标捕捉响应插件](https://github.com/PascalKieslich/mousetrap-os/blob/master/plugins/mousetrap_response/mousetrap_response.md)在显示另一个刺激物（例如，素描板）的同时跟踪鼠标移动，类似于键盘或鼠标响应项目。
[鼠标捕捉表单插件](https://github.com/PascalKieslich/mousetrap-os/blob/master/plugins/mousetrap_form/mousetrap_form.md)允许在[自定义表单](％link:manual/forms/custom％)中跟踪鼠标移动。
此外，这两个插件还提供Python类，可以在Python内联脚本中使用以实现最大的定制性。

使用插件收集数据后，可以使用[mousetrap R包](http://pascalkieslich.github.io/mousetrap/)处理、分析和可视化数据。

## 安装

有关如何安装mousetrap插件的信息，请参阅其[GitHub页面](https://github.com/PascalKieslich/mousetrap-os#installation)。[示例文件夹](https://github.com/PascalKieslich/mousetrap-os/tree/master/examples#example-experiments)中提供了演示基本功能的示例实验。


另请参阅：

- <https://rapunzel.cogsci.nl/manual/environment/>