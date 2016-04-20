<div class="ClassDoc YAMLDoc" id="items" markdown="1">

# class __items__

The `items` object provides dict-like access to the items. It's mainly
useful for programatically executing items.

In addition to the functions listed below, the following semantics are
supported:

__Example__:

~~~ .python
# Programmatically prepare and run a sketchpad item.
items.execute(u'my_sketchpad')
# Check if an item exists
if u'my_sketchpad' in items:
        print(u'my_sketchpad exists')
# Delete an item
del items[u'my_sketchpad']
# Walk through all item names
for item_name in items:
        print(item_name)
~~~

<div class="FunctionDoc YAMLDoc" id="items-execute" markdown="1">

## function __items\.execute__\(name\)

Executes the run and prepare phases of an item, and updates the item stack.

__Arguments:__

- `name` -- An item name.
	- Type: str

</div>

[items.execute]: #items-execute
[execute]: #items-execute

<div class="PropertyDoc YAMLDoc" id="items-items" markdown="1">

## property __items.items__

Returns a list of (item name, item object) tuples.

</div>

[items.items]: #items-items
[items]: #items-items

<div class="PropertyDoc YAMLDoc" id="items-keys" markdown="1">

## property __items.keys__

Returns a list of item names.

</div>

[items.keys]: #items-keys
[keys]: #items-keys

<div class="FunctionDoc YAMLDoc" id="items-new" markdown="1">

## function __items\.new__\(\_type, name=None, script=None\)

Creates a new item.

__Example:__

~~~ .python
items.new(u'sketchpad', name=u'my_sketchpad')
items[u'my_sketchpad'].prepare()
items[u'my_sketchpad'].run()
~~~

__Arguments:__

- `_type` -- The item type.
	- Type: unicode

__Keywords:__

- `name` -- The item name, or None to choose a unique name based on the item type.
	- Type: unicode, NoneType
	- Default: None
- `script` -- A definition script, or None to start with a blank item.
	- Type: unicode, NoneType
	- Default: None

__Returns:__

The newly generated item.

- Type: item

</div>

[items.new]: #items-new
[new]: #items-new

<div class="FunctionDoc YAMLDoc" id="items-prepare" markdown="1">

## function __items\.prepare__\(name\)

Executes the prepare phase of an item, and updates the item stack.

__Arguments:__

- `name` -- An item name.
	- Type: str

</div>

[items.prepare]: #items-prepare
[prepare]: #items-prepare

<div class="FunctionDoc YAMLDoc" id="items-run" markdown="1">

## function __items\.run__\(name\)

Executes the run phase of an item, and updates the item stack.

__Arguments:__

- `name` -- An item name.
	- Type: str

</div>

[items.run]: #items-run
[run]: #items-run

<div class="FunctionDoc YAMLDoc" id="items-valid_name" markdown="1">

## function __items\.valid\_name__\(item\_type, suggestion=None\)

Generates a unique name that is valid and resembles the desired name.

__Arguments:__

- `item_type` -- The type of the item to suggest a name for.
	- Type: unicode

__Keywords:__

- `suggestion` -- The desired name, or None to choose a name based on the item's type.
	- Type: unicode, NoneType
	- Default: None

__Returns:__

A unique name.

- Type: unicode

</div>

[items.valid_name]: #items-valid_name
[valid_name]: #items-valid_name

<div class="PropertyDoc YAMLDoc" id="items-values" markdown="1">

## property __items.values__

Returns a list of `item` objects.

</div>

[items.values]: #items-values
[values]: #items-values

</div>

[items]: #items

