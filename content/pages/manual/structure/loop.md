title: Looping and independent variables

The LOOP item has two important functions:

- It runs another item multiple times.
- It is where you usually define your independent variables; that is, the variables that you manipulate in your experiment.

[TOC]

## The item to run

A LOOP is always connected to a single other item: the item to run. You select the item to run in the box labeled "Run". In most cases, the item to run is a SEQUENCE, which runs multiple items sequentially.

Two common SEQUENCE-LOOP structures are:

- If a SEQUENCE corresponds to a single trial (by convention called *trial_sequence*), then a LOOP that is connected to this sequence corresponds to multiple trials, or a block (by convention called *block_loop*).
- If a SEQUENCE corresponds to a block of trials followed by a feedback display (by convention called *block_sequence*), then a loop that is connected to this sequence corresponds to multiple blocks, or a complete experimental session (by convention called *experimental_loop*).

## Defining independent variables

The loop table is a powerful-yet-simple way to define independent variables. Every column in the table corresponds to a variable; every row corresponds to a cycle, that is, a level of the variable. For example, a simple loop with one variable (`animal`) that has two cycles ("cat" and "dog") looks like this:

animal |
------ |
cat    |
dog    |

The loop has a few important options:

*Repeat* indicates how often each cycle should be executed. In the example above, repeat is set to 2, which means that *trial_sequence* is called twice while the variable `animal` has the value "cat", and twice while `animal` has the value "dog" (so four times in total).

*Order* indicates whether cycles should be executed sequentially or in random order. Randomization is complete, in the sense that the complete list of number-of-cycles × repeat trials is randomized.

## Reading independent variables from file

If you want to read independent variables from file, rather than entering them into the loop table, you can do so as follows:

- Set *Source* to *file*.
- Select an Excel (`.xlsx`) or CSV (`.csv`) file in the *File* entry.

The source file follows the same conventions as the loop table; that is, each column corresponds to a variable, and each row corresponds to a cycle.

CSV files are expected to be in the following format:

- plain-text
- comma-separated
- double-quoted (literal double-quotes are escaped with backward slashes)
- UTF-8 encoded

## Breaking the loop

If you want to break the loop before all cycles have been executed, you can specify a break-if expression. This break-if expression follows the same syntax as other conditional expressions, as described on:

- %link:manual/variables%

For example, the following break-if statement would break the loop as soon as a correct response is given:

```python
{correct} == 1
```

The *Evaluate on first cycle* option indicates whether the break-if statement should be evaluated before the first cycle, in which case no cycles may be executed at all, or only before the second cycle, in which case at least one cycle is always executed. In some cases, the break-if statement will refer to a variable that is only defined after the first cycle, in which case you should disable the 'Evaluate on first cycle' option to avoid a 'Variable does not exist' error.

## Generating a full-factorial design

By clicking on the *Full-factorial design* you open a wizard that allows you to easily generate a full-factorial design, that is, a design in which each combination of factors occurs.

## Pseudorandomization

You can add constraints for pseudorandomization to the script of the loop item. This shuffles the rows, even if Order is set to sequential. (Currently, this is not possible through the GUI.)

Example: Make sure that repetitions of the same word (given by the `word` variable) are separated by at least 4 cycles:

```python
constrain word mindist=4
```

Example: Make sure that the same word is not repeated:

```python
constrain word maxrep=1
```

`constrain` commands must come *after* `setcycle` commands.

## Advanced loop operations

Commands for advanced loop operations must come *after* `constrain` and `setcycle` commands.

### fullfactorial

The `fullfactorial` instruction treats the loop table as the input for a full-factorial design. For example, the following loop table:

cue   | duration
----- | --------
left  | 0
right | 100
      | 200

Would result in:

cue   | duration
----- | --------
left  | 0
left  | 100
left  | 200
right | 0
right | 100
right | 200

### shuffle

`shuffle` without argument randomizes the entire table. When a column name is specified (`shuffle cue`), only that column is randomized.

### shuffle_horiz

`shuffle_horiz` shuffles all columns horizontally. When multiple columns are specified, only those columns are shuffled horizontally.

For example, when `shuffle_horiz word1 word2` is applied to the following table:

word1 | word2 | word3
----- | ----- | -----
cat   | dog   | bunny
cat   | dog   | bunny
cat   | dog   | bunny

The result could be (i.e. values are randomly swapped between `word1` and `word2`, but not `word3`):

word1 | word2 | word3
----- | ----- | -----
dog   | cat   | bunny
dog   | cat   | bunny
cat   | dog   | bunny

### slice

`slice [from] [to]` selects a slice from the loop. It requires a start and an end index, where 0 is the first row, and negative values are counted from the end backwards. (Just like list slicing in Python, in other words.)

For example, when `slice 1 -1` is applied to the following table:

word  |
----- |
cat   |
dog   |
bunny |
horse |

The result would be:

word  |
----- |
dog   |
bunny |

### sort

`sort [column]` sorts a single column, without changing any of the other columns.

### sortby

`sortby [column]` sorts the entire table by a single column.

### reverse

`reverse` reverses the order of the entire table. If a column name is specified (e.g. `reverse word`), only that column is reversed, without changing any of the other columns.

### roll

`roll [value]` rolls the entire table forward (for positive values) or backward (for negative values). If a column name is specified (e.g. `roll 1 word`), only that column is rolled, without changing any of the other columns.

For example, if `roll 1` is applied to the following table:

word  |
----- |
cat   |
dog   |
bunny |
horse |

The result would be:

word  |
----- |
horse |
cat   |
dog   |
bunny |

### weight

`weight [column]` repeats each row by a weighting value specified in a column.

For example, if `weight w` is applied to the following table:

word  | w
----- | -
cat   | 0
dog   | 0
bunny | 2
horse | 1

The result would be:

word  | w
----- | -
bunny | 2
bunny | 2
horse | 1

## Previewing the loop

If you have specified constraints, or have used advanced loop operations, then it is a good idea to check that the result is as expected. To do so, you can generate a preview of the loop table as it will be (or could be, in case of randomization) when you run the experiment.

To generate a preview, click on the *Preview* button.


## Accessing the loop table in Python inline script

The original LOOP table, as you see it in the OpenSesame user interface, is a [`DataMatrix`](http://datamatrix.cogsci.nl/) object called `dm`, and is a property of the LOOP item.

This original LOOP table is usually transformed in various ways; for example, the order of the rows can be randomized, and rows can be repeated multiple times. The transformed LOOP is also a `DataMatrix` object, and is called `live_dm`. `live_dm` is created just before the loop is executed and is set to `None` when the loop is finished; that is, `live_dm` is only available during the *run* phase of the LOOP.

Finally, the index of the current row is stored as the experimental variable `live_row`. That is, `live_row` indicates the currently active row of `live_dm`.

So let's say that we have a LOOP called *block_loop*. We could then access the LOOP table in a Python inline script as follows:

~~~ .python
print('The original loop table:')
print(items['block_loop'].dm)

print('The transformed loop table:')
print(items['block_loop'].live_dm)

print('The current row:')
print(items['block_loop'].live_dm[var.live_row])
~~~

You can even programatically define the LOOP table. You have to do this in the Prepare phase of an INLINE_SCRIPT that precedes the LOOP.

```python
from datamatrix import DataMatrix

items['block_loop'].dm = DataMatrix(length=4)
items['block_loop'].dm.cue_side = 'left', 'right', 'left', 'right'
items['block_loop'].dm.cue_validity = 'valid', 'valid', 'invalid', 'invalid'
```

`DataMatrix` objects are powerful structures for working with tabular data. For more information, see:

- <https://pydatamatrix.eu/>
