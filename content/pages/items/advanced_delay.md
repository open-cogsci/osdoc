title: Advanced_delay

The `advanced_delay` plug-in delays the experiment for a pre-specified average duration plus a random margin.

- *Duration* is the average duration of the delay in milliseconds.
- *Jitter* is the size of the variation in the delay in milliseconds.
- *Jitter mode* is how the jitter is defined:
	- *Standard deviation* will draw values from a Gaussian distribution with Jitter as the standard deviation.
	- *Uniform* will draw values from a Uniform distribution centered at Duration, with Jitter as the width.
