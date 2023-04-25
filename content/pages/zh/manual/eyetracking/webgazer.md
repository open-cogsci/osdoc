title: WebGazer.js
hash: 47ee55649881bcf2ff92c750daeac0bdea5feb3a8719e0e99c5309e49686ecc6
locale: zh
language: Chinese

要求 OSWeb v1.4.6.1
{:.page-notification}

[TOC]

## 关于 WebGazer

WebGazer.js 是用 JavaScript 编写的眼动跟踪库。您可以将其与 OSWeb 配合使用以在在线实验中进行眼动跟踪。

- <https://webgazer.cs.brown.edu/>

## 将 WebGazer.js 包含在实验中

WebGazer.js 默认不与 OSWeb 绑定。但是，您可以在外部 JavaScript 库下输入指向 `webgazer.js` 的链接将其作为外部库包含。目前，一个可用的链接是：

```
https://webgazer.cs.brown.edu/webgazer.js
```

另请参见：

- %link:manual/osweb/osweb%

## 示例实验

以下您可以下载一个使用 WebGazer.js 的示例实验。首先要求参与者单击并查看一组点；这将导致 WebGazer.js 自动执行类似于校准过程的操作。接下来，实验展示了一个简单的屏幕以测试凝视位置记录的准确性。一般来说，进行细粒度的眼动跟踪是不切实际的，但您可以判断参与者正在看屏幕的哪个象限。要运行此实验，您需要如上所述将 WebGazer.js 包含在实验中。

- %static:attachments/webgazer.osexp%

您还可以在浏览器中直接启动实验：

- <https://jatos.mindprobe.eu/publix/BowSAFY2VWl>