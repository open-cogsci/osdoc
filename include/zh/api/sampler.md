<div class="ClassDoc YAMLDoc" markdown="1">

# 类 __Sampler__

`Sampler` 类提供了播放音频采样的功能。您通常使用`Sampler()`工厂函数创建一个`Sampler`对象，如[创建采样器](#creating-a-sampler)部分所述。

__示例：__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
my_sampler.play()
~~~

[TOC]

## 需要了解的事项

### 创建 Sampler

您通常使用 `Sampler()` 工厂函数创建一个 `Sampler`，该函数将音频文件的完整路径作为第一个参数。

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
~~~

您还可以选择将[播放关键词](#playback-keywords)传递给`Sampler()`以设置默认行为：

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
~~~

### 采样率

如果您发现您的采样播放速度太慢（音高低）或太快（音高高），请确保您的采样的采样率与后端设置中指定的采样器后端的采样率相匹配。

### 支持的文件格式

支持 `.wav`，`.mp3` 和 `.ogg` 格式的音频文件。如果您需要将采样从其他格式转换，可以使用
[Audacity](http://sourceforge.net/projects/audacity/)。

### 播放关键词

接受 `**playback_args` 的函数可采取以下关键词参数：

- `volume` 指定一个 `0.0`（静音）到 `1.0`（最大）之间的音量。
- `pitch` 指定音高（或播放速度），其中大于1的值表示较高的音高，小于1的值表示较低的音高。
- `pan` 指定一个平移，在这个平移上小于0的值表示向左平移，大于0的值表示向右平移。或者，您可以将泛音设置为'left'或'right'以仅播放单个声道。
- `duration` 指定以毫秒为单位的声音持续时间，或设置为 `0` 或 `None` 以播放完整的声音。
- `fade_in` 指定声音的淡入时间（或攻击），或设置为 `0` 或 `None` 以禁用淡入。
- `block` 指示实验是否在播放期间阻塞（`True`）或不阻塞（`False`）。

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.play(volume=.5, pan='left')
~~~

播放关键字仅影响当前操作（创建对象时传递给 `Sampler()` 除外）。要更改所有后续操作的行为，请直接设置播放属性：

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.volume = .5
my_sampler.pan = 'left'
my_sampler.play()
~~~

或者在创建音频对象时将播放关键字传递给`Sampler()`：

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~

## close_sound(experiment)

实验结束后关闭混音器。

__参数__

- **experiment**: 实验对象。

## init_sound(experiment)

实验开始前初始化 pygame 混音器。

__参数__

- **experiment**: 实验对象。

## is_playing(self)

检查当前是否正在播放音效。

__返回__

- 如果正在播放声音，则为 True；否则为 False。

__示例__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
if my_sampler.is_playing():
        print('播放器仍在播放！')
~~~

## pause(self)

暂停播放（如果有）。

__示例__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~

## play(\*arglist, \*\*kwdict)

播放声音。

__参数__

- **\*\*playback_args**： [播放关键词](#playback-keywords)的可选项，将用于此 `Sampler.play()` 调用。这不会影响后续操作。

__示例__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play(pitch=.5, block=True)
~~~

## resume(self)

恢复播放（如有）。



__示例__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~



## set_config(\*\*cfg)

更新可配置项。


__参数__

- **\*\*cfg**: 即将更新的可配置项。


## stop(self)

停止当前正在播放的声音（如果有的话）。



__示例__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.stop()
~~~



## wait(self)

阻止直到声音播放完毕，或者如果没有声音正在播放，则立即返回。



__示例__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
my_sampler.wait()
print('The sampler is finished!')
~~~

</div>
