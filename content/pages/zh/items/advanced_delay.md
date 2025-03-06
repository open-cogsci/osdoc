title: Advanced_delay
hash: 54879490fe7472c89ac95be6dc21911ffcdddabbe58ec3de0baf4b660ad5dc89
locale: zh
language: Chinese

`advanced_delay` 插件将实验延迟一个预先指定的平均持续时间加上一个随机的浮动。

- *Duration* 是延迟的平均持续时间，以毫秒为单位。
- *Jitter* 是延迟变化的幅度，以毫秒为单位。
- *Jitter mode* 是定义浮动的方式：
  - *Standard deviation*将从一个以Jitter为标准差的高斯分布中提取值。
  - *Uniform* 将从一个以Duration为中心的均匀分布中提取值，Jitter为宽度。