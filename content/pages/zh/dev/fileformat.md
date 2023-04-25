title: 文件格式 (.osexp)
hash: 310dc6efe4055dac4dd14eda896adcf8c98e4a4f1950bb613ed0c1fd461c5ebc
locale: zh
language: Chinese

[TOC]

## .osexp 格式

OpenSesame 实验以 `.osexp` 格式保存。 `.osexp` 文件的内容取决于实验中是否包含文件，即文件池是否为空。

## 如果文件池为空

如果文件池为空，实验将以纯文本文件的形式保存。此文件为 utf-8 编码并使用 Unix 风格的换行符。您可以在大多数文本编辑器中编辑和查看此文件。

OpenSesame 脚本语法在此处描述：

- %link:opensesame-script%

## 如果文件池不为空

如果文件池中有文件，实验将以 `.tar.gz` 格式保存，这是一种类似于 `.zip` 的文件格式。在此文件中，您会发现以下内容：

- `script.opensesame` 是实验脚本，格式与上述相同
- `pool/` 是一个文件夹，其中包含文件池中的所有文件。文件名中的任何非 ascii 字符都将替换为 `U+XXXX` 字符串。

## .opensesame 和 .opensesame.tar.gz 格式发生了什么？

您仍然可以打开 `.opensesame` 和 `.opensesame.tar.gz` 格式，这是 OpenSesame <= 2.9.X 使用的格式。但是，您不能再将实验保存为此格式。