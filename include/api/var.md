<div class="ClassDoc YAMLDoc" id="var" markdown="1">

# instance __var__

The `var` object provides access to experimental variables.
Experimental variables are the variables that live in the GUI, and are
commonly set as independent variables in the LOOP item, referred
to using the square-bracket (`[my_variable]`) notation, and logged by
the LOGGER item.

A `var` object is created automatically when the experiment starts.

In addition to the functions listed below, the following semantics are
supported:

__Example__:

~~~ .python
# Set an experimental variable
var.my_variable = u'my_value'
# Get an experimental variable
print(u'Subject nr = %d' % var.subject_nr)
# Delete (unset) an experimental variable
del var.my_variable
# Check if an experimental variable exists
if u'my_variable' in var:
    print(u'my_variable exists!')
# Loop through all experimental variables
for var_name in var:
        print(u'variable found: %s' % var_name)
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="var-clear" markdown="1">

## function __var\.clear__\(preserve=\[\]\)

*New in 3.1.2*

Clears all experimentals variables.

__Example:__

~~~ .python
var.clear()
~~~

__Keywords:__

- `preserve` -- A list of variable names that shouldn't be cleared.
	- Type: list
	- Default: []

</div>

<div class="FunctionDoc YAMLDoc" id="var-get" markdown="1">

## function __var\.get__\(var, default=None, \_eval=True, valid=None\)

Gets an experimental variable.

__Example:__

~~~ .python
print('my_variable = %s' % var.get(u'my_variable'))
# Equivalent to:
print('my_variable = %s' % var.my_variable)
# But if you want to pass keyword arguments you need to use `get()`:
var.get(u'my_variable', default=u'a_default_value')
~~~

__Arguments:__

- `var` -- The variable to retrieve.
	- Type: str, unicode

__Keywords:__

- `default` -- A default value in case the variable doesn't exist, or `None` for no default value.
	- Type: any
	- Default: None
- `_eval` -- Determines whether the returned should be evaluated for variable references.
	- Type: bool
	- Default: True
- `valid` -- A list of valid values, or `None` to allow all values.
	- Type: NoneType, list
	- Default: None

</div>

<div class="FunctionDoc YAMLDoc" id="var-has" markdown="1">

## function __var\.has__\(var\)

Checks if an experimental variable exists.

__Example:__

~~~ .python
if var.has(u'my_variable'):
        print(u'my_variable has been defined!')
# Equivalent to:
if u'my_variable' in var:
        print(u'my_variable has been defined!')
~~~

__Arguments:__

- `var` -- The variable to check.
	- Type: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="var-items" markdown="1">

## function __var\.items__\(\)

Returns a list of (variable_name, value) tuples. See [vars] for a note about the non-exhaustiveness of this function.

__Example:__

~~~ .python
for varname, value in var.items():
        print(varname, value)
~~~

__Returns:__

A list of (variable_name, value) tuples.

- Type: list

</div>

<div class="FunctionDoc YAMLDoc" id="var-set" markdown="1">

## function __var\.set__\(var, val\)

Sets and experimental variable.

__Example:__

~~~ .python
var.set(u'my_variable', u'my_value')
# Equivalent to
var.my_variable = u'my_value'
~~~

__Arguments:__

- `var` -- The variable to assign.
	- Type: str, unicode
- `val` -- The value to assign.
	- Type: any

</div>

<div class="FunctionDoc YAMLDoc" id="var-unset" markdown="1">

## function __var\.unset__\(var\)

Deletes a variable.

__Example:__

~~~ .python
var.unset(u'my_variable')
# Equivalent to:
del var.my_variable
~~~

__Arguments:__

- `var` -- The variable to delete.
	- Type: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="var-vars" markdown="1">

## function __var\.vars__\(\)

Returns a list of experimental variables. Because experimental variables can be stored in multiple places, this list may not be exhaustive. That is, `u'my_var' in var` may return `True`, while u'my_var' is not in the list of variables as returned by this function.

__Example:__

~~~ .python
for varname in var.vars():
        print(varname)
~~~

__Returns:__

A list of variable names.

- Type: list

</div>

</div>

