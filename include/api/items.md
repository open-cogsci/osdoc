<div class="ClassDoc YAMLDoc" markdown="1">

# instance __items__

The `items` object provides dict-like access to the items. It's mainly
useful for programmatically executing items.

An `items` object is created automatically when the experiment starts.

In addition to the functions listed below, the following semantics are
supported:

__Example__

~~~ .python
# Programmatically prepare and run a sketchpad item.
items.execute('my_sketchpad')
# Check if an item exists
if 'my_sketchpad' in items:
    print('my_sketchpad exists')
# Delete an item
del items['my_sketchpad']
# Walk through all item names
for item_name in items:
    print(item_name)
~~~

[TOC]

## execute(name)

Executes the run and prepare phases of an item, and updates the
item stack.


__Parameters__

- **name**: An item name.

__Example__

~~~ .python
items.execute('target_sketchpad')
~~~



## new(_type, name=None, script=None, allow_rename=True)

Creates a new item.


__Parameters__

- **_type**: The item type.
- **name**: The item name, or None to choose a unique name based on the item
type.
- **script**: A definition script, or None to start with a blank item.
- **allow_rename**: Indicates whether OpenSesame can use a different name from the one
that is provided as `name` to avoid duplicate names etc.

__Returns__

- The newly generated item.

__Example__

~~~ .python
items.new('sketchpad', name='my_sketchpad')
items['my_sketchpad'].prepare()
items['my_sketchpad'].run()
~~~



## prepare(name)

Executes the prepare phase of an item, and updates the item stack.


__Parameters__

- **name**: An item name.

__Example__

~~~ .python
items.prepare('target_sketchpad')
items.run('target_sketchpad')
~~~



## run(name)

Executes the run phase of an item, and updates the item stack.


__Parameters__

- **name**: An item name.

__Example__

~~~ .python
items.prepare('target_sketchpad')
items.run('target_sketchpad')
~~~



## valid_name(item_type, suggestion=None)

Generates a unique name that is valid and resembles the desired
name.


__Parameters__

- **item_type**: The type of the item to suggest a name for.
- **suggestion**: The desired name, or None to choose a name based on the item's
type.

__Returns__

- A unique name.

__Example__

~~~ .python
valid_name = items.valid_name('sketchpad', 'an invalid name')
~~~



</div>

