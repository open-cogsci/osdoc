---
layout: osdoc
title: Languages
group: General
permalink: /lang/
singleton: true
---

## Available languages

- [English (en)](#lang-en)
- [Français (fr)](#lang-fr)

{% for lang in site.langs %}

## {{ lang }} {#lang-{{ lang }}}

{% include sitemap %}

{% endfor %}
