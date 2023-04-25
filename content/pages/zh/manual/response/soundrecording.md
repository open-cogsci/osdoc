title: 声音录制
hash: 541c85146b0c2948e62bcae0056f831ddb9cf3e2d2a3025254b3d54dac2e5f46
locale: zh
language: Chinese

[TOC]


## 音频低延迟插件

音频低延迟插件是由Bob Rosbag开发的，推荐用来记录音频输入。这套插件的主要目标是以最小和可预测的延迟播放和记录音频，以达到高精度和高准确性。使用Linux ALSA音频系统的`PyAlsaAudio`软件包在Python中提供了最佳结果。`PortAudio`和`sounddevice`是跨平台的，可以在Windows和Linux上运行。

这些插件默认不会被安装，但可以通过pip安装:

```bash
pip install opensesame-plugin-audio-low-latency
```

参考：

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>


## 音频记录插件

音频记录插件是由Daniel Schreij开发的，已经不再进行积极的开发，因此不再被推荐使用。关于这套插件的更多信息可以在本页面的之前版本中找到：

- <https://osdoc.cogsci.nl/3.2/manual/response/soundrecording/>