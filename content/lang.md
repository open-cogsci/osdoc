---
layout: osdoc
title: Languages
group: General
permalink: /lang/
singleton: true
---

## Available languages

- [Français (fr)](#lang-fr)
- [English (en)](#lang-en)
- [Español (es)](#lang-es)

{% for lang in site.langs %}

## {{ lang }} {#lang-{{ lang }}}

{% include sitemap %}

{% endfor %}
