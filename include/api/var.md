<div class="ClassDoc YAMLDoc" markdown="1">

# instance __var__

__New in 4.0.0__: As of OpenSesame 4.0, all experimental variables are
also available in the Python workspace. This means that you therefore 
don't need the `var` object anymore.

The `var` object provides access to experimental variables.
Experimental variables are the variables that live in the GUI, and are
commonly set as independent variables in the LOOP item, referred
to using the curly-braces (`{my_variable}`) notation, and logged by
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
# Delete (unset) an experimental
variable
del var.my_variable
# Check if an experimental variable exists
if
u'my_variable' in var:
    print(u'my_variable exists!')
# Loop through all
experimental variables
for var_name in var:
        print(u'variable found:
%s' % var_name)
~~~

[TOC]

## clear(preserve=[])

*New in 3.1.2*

Clears all experimentals variables.

__Parameters__

- **preserve**: A list of variable names that shouldn't be cleared.

__Example__

~~~ .python
var.clear()
~~~



## get(var, default=None, _eval=True, valid=None)

Gets an experimental variable.


__Parameters__

- **var**: The variable to retrieve.
- **default**: A default value in case the variable doesn't exist, or `None` for
no default value.
- **_eval**: Determines whether the returned should be evaluated for variable
references.
- **valid**: A list of valid values, or `None` to allow all values.

__Example__

~~~ .python
print('my_variable = %s' % var.get(u'my_variable'))
# Equivalent to:
print('my_variable = %s' % var.my_variable)
# But if you want to pass keyword arguments you need to use `get()`:
var.get(u'my_variable', default=u'a_default_value')
~~~



## has(var)

Checks if an experimental variable exists.


__Parameters__

- **var**: The variable to check.

__Example__

~~~ .python
if var.has(u'my_variable'):
        print(u'my_variable has been defined!')
# Equivalent to:
if u'my_variable' in var:
        print(u'my_variable has been defined!')
~~~



## inspect(self)

Generates a description of all experimental variables, both alive
and hypothetical.



__Returns__

- A dict where variable names are keys, and values are dicts with
source, value, and alive keys.


## items(self)

Returns a list of (variable_name, value) tuples. See `var.vars()`
for a note about the non-exhaustiveness of this function.



__Returns__

- A list of (variable_name, value) tuples.

__Example__

~~~ .python
for varname, value in var.items():
        print(varname, value)
~~~



## set(var, val)

Sets and experimental variable.


__Parameters__

- **var**: The variable to assign.
- **val**: The value to assign.

__Example__

~~~ .python
var.set(u'my_variable', u'my_value')
# Equivalent to
var.my_variable = u'my_value'
~~~



## unset(var)

Deletes a variable.


__Parameters__

- **var**: The variable to delete.

__Example__

~~~ .python
var.unset(u'my_variable')
# Equivalent to:
del var.my_variable
~~~



## vars(self)

Returns a list of experimental variables. Because experimental
variables can be stored in multiple places, this list may not be
exhaustive. That is, `u'my_var' in var` may return `True`, while
u'my_var' is not in the list of variables as returned by this function.



__Returns__

- A list of variable names.

__Example__

~~~ .python
for varname in var.vars():
        print(varname)
~~~



</div>
