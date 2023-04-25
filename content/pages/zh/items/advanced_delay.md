title: Advanced_delay
hash: 05d5215072bc5c76e2fd177cc099d6281a44d87cde42c43e79a945b2ac83b98f
locale: zh
language: Chinese

`advanced_delay`插件会使实验延迟一个预先指定的平均持续时间加上一个随机范围。

- *Duration* 是延迟的平均持续时间，以毫秒为单位。
- *Jitter* 是延迟变化的大小，以毫秒为单位。
- *Jitter mode* 是计算抖动的方式：
	- *Standard deviation* 会从具有Jitter作为标准差的高斯分布中抽取变化。
	- *Uniform* 将从均匀分布中抽取持续时间的变化。