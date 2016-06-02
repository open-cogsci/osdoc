## Timeout

The *Timeout* field indicates a timeout value in milliseconds, or 'infinite' for no timeout. When a timeout occurs, the following happens:

- `response_time` is set to the timeout value, or rather to the time it takes for a timeout to be registered, which may deviate slightly from the timeout value.
- `response` is set to 'None'. This means that you can specify 'None' for the correct response a timeout should occur; this can be useful, for example, in a go/no-go task, when the participant should withold a response on no-go trials.
