<div class="ClassDoc YAMLDoc" markdown="1">

# instance __pool__

The `pool` object provides dict-like access to the file pool. When
checking whether a file is in the file pool, several folders are
searched.
For more details, see `pool.folders()`.

A `pool` object is created
automatically when the experiment starts.

In addition to the functions
listed below, the following semantics are
supported:

__Examples__

Basic use:

~~~ .python
# Get the full path to a file in the file pool
print(f'The full path to img.png is {pool["img.png"]}')
# Check if a file is in the file pool
if 'img.png' in pool:
    print('img.png is in the file pool')
# Delete a file from the file pool
del pool['img.png']
# Walk through all files in the file pool. This retrieves the full paths.
for path in pool:
    print(path)
# Check the number of files in the file pool
print(f'There are {len(pool)} files in the file pool')
~~~

Get an image from the file pool and use a `Canvas` to show it.

~~~ .python
image_path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(image_path)
my_canvas.show()
~~~

[TOC]

## add(path, new_name=None)

Copies a file to the file pool.


__Parameters__

- **path**: The full path to the file on disk.
- **new_name**: A new name for the file in the pool, or None to use the file's
original name.

__Example__

~~~ .python
pool.add('/home/username/Pictures/my_ing.png')
~~~



## clean_up()

Removes the pool folder.




## fallback_folder()

The full path to the fallback pool folder, which is the
`__pool__` subfolder of the current experiment folder, or
`None` if this folder does not exist. The fallback pool
folder is mostly useful in combination with a versioning
system, such as git, because it allows you to save the
experiment as a plain-text file, even when having files
in the file pool.



__Returns__

- 

__Example__

~~~ .python
if pool.fallback_folder() is not None:
    print('There is a fallback pool folder!')
~~~



## files()

Returns all files in the file pool.



__Returns__

- A list of full paths.

__Example__

~~~ .python
for path in pool.files():
    print(path)
# Equivalent to:
for path in pool:
    print(path)
~~~



## folder()

Gives the full path to the (main) pool folder. This is typically a
temporary folder that is deleted when the experiment is finished.



__Returns__

- The full path to the main pool folder.

__Example__

~~~ .python
print(f'The pool folder is here: {pool.folder()}')
~~~



## folders(include_fallback_folder=True, include_experiment_path=False)

Gives a list of all folders that are searched when retrieving the
full path to a file. These are (in order):

1. The file pool folder
itself, as returned by `pool.folder()`.
2. The folder of the current
experiment (if it exists)
3. The fallback pool folder, as returned by
`pool.fallback_folder()` (if it exists)

__Parameters__

- **include_fallback_folder**: Indicates whether the fallback pool folder should be included if it
exists.
- **include_experiment_path**: Indicates whether the experiment folder should be included if it
exists.

__Returns__

- A list of all folders.

__Example__

~~~ .python
print('The following folders are searched for files:')
for folder in pool.folders():
    print(folder)
~~~



## in_folder(path)

Checks whether path is in the pool folder. This is different from
the `path in pool` syntax in that it only checks the main pool folder,
and not the fallback pool folder and experiment folder.


__Parameters__

- **path**: A file basename to check.

__Returns__

- 

__Example__

~~~ .python
print(pool.in_folder('cue.png'))
~~~



## rename(old_path, new_path)

Renames a file in the pool folder.


__Parameters__

- **old_path**: The old file name.
- **new_path**: The new file name.

__Example__

~~~ .python
pool.rename('my_old_img.png', 'my_new_img.png')
~~~



## size()

Gets the combined size in bytes of all files in the file pool.



__Returns__

- 

__Example__

~~~ .python
print(f'The size of the file pool is {pool.size()} bytes')
~~~



</div>

