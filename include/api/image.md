<div class="ClassDoc YAMLDoc" markdown="1">

## alpha_composite(im1, im2)

Alpha composite im2 over im1.

:param im1: The first image. Must have mode RGBA.
:param im2: The second image.  Must have mode RGBA, and the same size as
   the first image.
:returns: An :py:class:`~PIL.Image.Image` object.



## blend(im1, im2, alpha)

Creates a new image by interpolating between two input images, using
a constant alpha::

    out = image1 * (1.0 - alpha) + image2 * alpha

:param im1: The first image.
:param im2: The second image.  Must have the same mode and size as
   the first image.
:param alpha: The interpolation alpha factor.  If alpha is 0.0, a
   copy of the first image is returned. If alpha is 1.0, a copy of
   the second image is returned. There are no restrictions on the
   alpha value. If necessary, the result is clipped to fit into
   the allowed output range.
:returns: An :py:class:`~PIL.Image.Image` object.



## composite(image1, image2, mask)

Create composite image by blending images using a transparency mask.

:param image1: The first image.
:param image2: The second image.  Must have the same mode and
   size as the first image.
:param mask: A mask image.  This image can have mode
   "1", "L", or "RGBA", and must have the same size as the
   other two images.



## deprecate(deprecated: 'str', when: 'int | None', replacement: 'str | None' = None, \*, action: 'str | None' = None, plural: 'bool' = False) -> 'None'

Deprecations helper.

:param deprecated: Name of thing to be deprecated.
:param when: Pillow major version to be removed in.
:param replacement: Name of replacement.
:param action: Instead of "replacement", give a custom call to action
    e.g. "Upgrade to new thing".
:param plural: if the deprecated thing is plural, needing "are" instead of "is".

Usually of the form:

    "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd).
    Use [replacement] instead."

You can leave out the replacement sentence:

    "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd)"

Or with another call to action:

    "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd).
    [action]."



## effect_mandelbrot(size, extent, quality)

Generate a Mandelbrot set covering the given extent.

:param size: The requested size in pixels, as a 2-tuple:
   (width, height).
:param extent: The extent to cover, as a 4-tuple:
   (x0, y0, x1, y1).
:param quality: Quality.



## effect_noise(size, sigma)

Generate Gaussian noise centered around 128.

:param size: The requested size in pixels, as a 2-tuple:
   (width, height).
:param sigma: Standard deviation of noise.



## eval(image, \*args)

Applies the function (which should take one argument) to each pixel
in the given image. If the image has more than one band, the same
function is applied to each band. Note that the function is
evaluated once for each possible pixel value, so you cannot use
random components or other generators.

:param image: The input image.
:param function: A function object, taking one integer argument.
:returns: An :py:class:`~PIL.Image.Image` object.



## fromarray(obj, mode=None)

Creates an image memory from an object exporting the array interface
(using the buffer protocol).

If ``obj`` is not contiguous, then the ``tobytes`` method is called
and :py:func:`~PIL.Image.frombuffer` is used.

If you have an image in NumPy::

  from PIL import Image
  import numpy as np
  im = Image.open("hopper.jpg")
  a = np.asarray(im)

Then this can be used to convert it to a Pillow image::

  im = Image.fromarray(a)

:param obj: Object with array interface
:param mode: Optional mode to use when reading ``obj``. Will be determined from
  type if ``None``.

  This will not be used to convert the data after reading, but will be used to
  change how the data is read::

    from PIL import Image
    import numpy as np
    a = np.full((1, 1), 300)
    im = Image.fromarray(a, mode="L")
    im.getpixel((0, 0))  # 44
    im = Image.fromarray(a, mode="RGB")
    im.getpixel((0, 0))  # (44, 1, 0)

  See: :ref:`concept-modes` for general information about modes.
:returns: An image object.

.. versionadded:: 1.1.6



## frombuffer(mode, size, data, decoder_name='raw', \*args)

Creates an image memory referencing pixel data in a byte buffer.

This function is similar to :py:func:`~PIL.Image.frombytes`, but uses data
in the byte buffer, where possible.  This means that changes to the
original buffer object are reflected in this image).  Not all modes can
share memory; supported modes include "L", "RGBX", "RGBA", and "CMYK".

Note that this function decodes pixel data only, not entire images.
If you have an entire image file in a string, wrap it in a
:py:class:`~io.BytesIO` object, and use :py:func:`~PIL.Image.open` to load it.

In the current version, the default parameters used for the "raw" decoder
differs from that used for :py:func:`~PIL.Image.frombytes`.  This is a
bug, and will probably be fixed in a future release.  The current release
issues a warning if you do this; to disable the warning, you should provide
the full set of parameters.  See below for details.

:param mode: The image mode. See: :ref:`concept-modes`.
:param size: The image size.
:param data: A bytes or other buffer object containing raw
    data for the given mode.
:param decoder_name: What decoder to use.
:param args: Additional parameters for the given decoder.  For the
    default encoder ("raw"), it's recommended that you provide the
    full set of parameters::

        frombuffer(mode, size, data, "raw", mode, 0, 1)

:returns: An :py:class:`~PIL.Image.Image` object.

.. versionadded:: 1.1.4



## frombytes(mode, size, data, decoder_name='raw', \*args)

Creates a copy of an image memory from pixel data in a buffer.

In its simplest form, this function takes three arguments
(mode, size, and unpacked pixel data).

You can also use any pixel decoder supported by PIL. For more
information on available decoders, see the section
:ref:`Writing Your Own File Codec <file-codecs>`.

Note that this function decodes pixel data only, not entire images.
If you have an entire image in a string, wrap it in a
:py:class:`~io.BytesIO` object, and use :py:func:`~PIL.Image.open` to load
it.

:param mode: The image mode. See: :ref:`concept-modes`.
:param size: The image size.
:param data: A byte buffer containing raw data for the given mode.
:param decoder_name: What decoder to use.
:param args: Additional parameters for the given decoder.
:returns: An :py:class:`~PIL.Image.Image` object.



## fromqimage(im)

Creates an image instance from a QImage image




## fromqpixmap(im)

Creates an image instance from a QPixmap image




## getmodebandnames(mode)

Gets a list of individual band names.  Given a mode, this function returns
a tuple containing the names of individual bands (use
:py:method:`~PIL.Image.getmodetype` to get the mode used to store each
individual band.

:param mode: Input mode.
:returns: A tuple containing band names.  The length of the tuple
    gives the number of bands in an image of the given mode.
:exception KeyError: If the input mode was not a standard mode.



## getmodebands(mode)

Gets the number of individual bands for this mode.

:param mode: Input mode.
:returns: The number of bands in this mode.
:exception KeyError: If the input mode was not a standard mode.



## getmodebase(mode)

Gets the "base" mode for given mode.  This function returns "L" for
images that contain grayscale data, and "RGB" for images that
contain color data.

:param mode: Input mode.
:returns: "L" or "RGB".
:exception KeyError: If the input mode was not a standard mode.



## getmodetype(mode)

Gets the storage type mode.  Given a mode, this function returns a
single-layer mode suitable for storing individual bands.

:param mode: Input mode.
:returns: "L", "I", or "F".
:exception KeyError: If the input mode was not a standard mode.



## i32le(c, o=0)

Converts a 4-bytes (32 bits) string to an unsigned integer.

:param c: string containing bytes to convert
:param o: offset of bytes to convert in string



## init()

Explicitly initializes the Python Imaging Library. This function
loads all available file format drivers.




## isImageType(t)

Checks if an object is an image object.

.. warning::

   This function is for internal use only.

:param t: object to check if it's an image
:returns: True if the object is an image



## linear_gradient(mode)

Generate 256x256 linear gradient from black to white, top to bottom.

:param mode: Input mode.



## merge(mode, bands)

Merge a set of single band images into a new multiband image.

:param mode: The mode to use for the output image. See:
    :ref:`concept-modes`.
:param bands: A sequence containing one single-band image for
    each band in the output image.  All bands must have the
    same size.
:returns: An :py:class:`~PIL.Image.Image` object.



## new(mode, size, color=0)

Creates a new image with the given mode and size.

:param mode: The mode to use for the new image. See:
   :ref:`concept-modes`.
:param size: A 2-tuple, containing (width, height) in pixels.
:param color: What color to use for the image.  Default is black.
   If given, this should be a single integer or floating point value
   for single-band modes, and a tuple for multi-band modes (one value
   per band).  When creating RGB images, you can also use color
   strings as supported by the ImageColor module.  If the color is
   None, the image is not initialised.
:returns: An :py:class:`~PIL.Image.Image` object.



## open(fp, mode='r', formats=None)

Opens and identifies the given image file.

This is a lazy operation; this function identifies the file, but
the file remains open and the actual image data is not read from
the file until you try to process the data (or call the
:py:meth:`~PIL.Image.Image.load` method).  See
:py:func:`~PIL.Image.new`. See :ref:`file-handling`.

:param fp: A filename (string), pathlib.Path object or a file object.
   The file object must implement ``file.read``,
   ``file.seek``, and ``file.tell`` methods,
   and be opened in binary mode.
:param mode: The mode.  If given, this argument must be "r".
:param formats: A list or tuple of formats to attempt to load the file in.
   This can be used to restrict the set of formats checked.
   Pass ``None`` to try all supported formats. You can print the set of
   available formats by running ``python3 -m PIL`` or using
   the :py:func:`PIL.features.pilinfo` function.
:returns: An :py:class:`~PIL.Image.Image` object.
:exception FileNotFoundError: If the file cannot be found.
:exception PIL.UnidentifiedImageError: If the image cannot be opened and
   identified.
:exception ValueError: If the ``mode`` is not "r", or if a ``StringIO``
   instance is used for ``fp``.
:exception TypeError: If ``formats`` is not ``None``, a list or a tuple.



## preinit()

Explicitly load standard file format drivers.




## radial_gradient(mode)

Generate 256x256 radial gradient from black to white, centre to edge.

:param mode: Input mode.



## register_decoder(name, decoder)

Registers an image decoder.  This function should not be
used in application code.

:param name: The name of the decoder
:param decoder: A callable(mode, args) that returns an
                ImageFile.PyDecoder object

.. versionadded:: 4.1.0



## register_encoder(name, encoder)

Registers an image encoder.  This function should not be
used in application code.

:param name: The name of the encoder
:param encoder: A callable(mode, args) that returns an
                ImageFile.PyEncoder object

.. versionadded:: 4.1.0



## register_extension(id, extension)

Registers an image extension.  This function should not be
used in application code.

:param id: An image format identifier.
:param extension: An extension used for this format.



## register_extensions(id, extensions)

Registers image extensions.  This function should not be
used in application code.

:param id: An image format identifier.
:param extensions: A list of extensions used for this format.



## register_mime(id, mimetype)

Registers an image MIME type.  This function should not be used
in application code.

:param id: An image format identifier.
:param mimetype: The image MIME type for this format.



## register_open(id, factory, accept=None)

Register an image file plugin.  This function should not be used
in application code.

:param id: An image format identifier.
:param factory: An image file factory method.
:param accept: An optional function that can be used to quickly
   reject images having another format.



## register_save(id, driver)

Registers an image save function.  This function should not be
used in application code.

:param id: An image format identifier.
:param driver: A function to save images in this format.



## register_save_all(id, driver)

Registers an image function to save all the frames
of a multiframe format.  This function should not be
used in application code.

:param id: An image format identifier.
:param driver: A function to save images in this format.



## registered_extensions()

Returns a dictionary containing all file extensions belonging
to registered plugins




</div>

