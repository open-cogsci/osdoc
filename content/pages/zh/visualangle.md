title: 视角度
hash: b9febd85c8491dfed24e738cf632d1d0051f391ed1835b760f8fbf04f7846eef
locale: zh
language: Chinese

您经常会看到视觉刺激的大小用视觉角度（°）表示。视觉角度表示从刺激端点到眼睛晶状体的直线之间的角度。因此，视觉角度与刺激在视网膜上的大小有关，但这种关系是间接的：它是从眼睛晶状体处测量的角度，如 %FigEye 所示。

[TOC]

figure:
 id: FigEye
 source: fig-eye.png
 caption: 视觉角度示意图。 (图片改编自 [WikiMedia Commons](http://commons.wikimedia.org/wiki/File:Schematic_diagram_of_the_human_eye.svg).)

使用这种有些奇怪的大小度量方法的原因是它反映了刺激的感知大小，这在心理学实验中通常比实际大小更重要。例如，如果在显示器上呈现宽度为100像素的图片，视觉角度可能对应3°。 如果将显示器移得更远一些，图片的视觉角度将减少到，例如，2°。 视觉角度因此反映了刺激与观察者之间的距离很重要。

参见 ：

- <http://en.wikipedia.org/wiki/Visual_angle>

## 将像素转换为视觉角度

要将像素转换为视觉角度，您需要了解三件事：

- `h` 是以厘米为单位的显示器高度，您可以用尺子测量。 (例如，25cm)
- `d` 是以厘米为单位的参与者与监视器之间的距离，您可以用尺子测量。 (例如，60cm)
- `r` 是以像素为单位的监视器的垂直分辨率，您可以在操作系统的显示设置中找到 (例如，768 px)

您可以按照下面的步骤计算刺激的角大小。您可以在OpenSesame调试窗口中执行此脚本。当然，您需要替换所有值，以使它们与您的设置相对应。请注意，一个视觉度通常对应于30 - 60像素，具体取决于距离和显示器的大小。相反，单个像素通常对应于0.01至0.03视觉度。如果您获得的值远离这个范围，那么您可能犯了错误。

```python
from math import atan2, degrees

h = 25           # 显示器高度（厘米）
d = 60           # 显示器与参与者之间的距离（厘米）
r = 768          # 显示器的垂直分辨率
size_in_px = 100 # 刺激尺寸（像素）
# 计算每个像素对应的度数。这通常是一个非常小的值，例如0.03。
deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
print(f'单个像素对应的角度为 {deg_per_px}度')
# 计算刺激的度数大小
size_in_deg = size_in_px * deg_per_px
print(f'刺激的尺寸是 {size_in_px} 像素和 {size_in_deg} 视觉度')
```

## 将视觉角度转换为像素

将视觉角度转换为像素只是上述过程的逆过程，可以按照以下步骤进行：

```python
from math import atan2, degrees
h = 25           # 显示器高度（厘米）
d = 60           # 显示器与参与者之间的距离（厘米）
r = 768          # 显示器的垂直分辨率
size_in_deg = 3. # 刺激尺寸（像素）
# 计算每个像素对应的度数。这通常是一个非常小的值，例如0.03。
deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
print(f'单个像素对应的角度为 {deg_per_px}度')
# 计算刺激的像素大小
size_in_px = size_in_deg / deg_per_px
print(f'刺激的尺寸是 {size_in_px} 像素和 {size_in_deg} 视觉度')
```
