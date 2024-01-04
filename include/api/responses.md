<div class="ClassDoc YAMLDoc" markdown="1">

# instance __responses__

The `responses` object contains the history of the responses that were
collected during the experiment.

A `responses` object is created automatically when the experiment starts.

In addition to the functions listed below, the following semantics are
supported:

__Example__

~~~ .python
# Loop through all responses, where last-given responses come first
# Each response has correct, response, response_time, item, and feedback
# attributes.
for response in responses:
    print(response.correct)
# Print the two last-given responses
print('last_two responses:')
print(responses[:2])
~~~

[TOC]

## add(response=None, correct=None, response_time=None, item=None, feedback=True)

Adds a response.


__Parameters__

- **response    The response value, for example, 'space' for the spacebar, 0 for**: joystick button 0, etc.
- **correct**: The correctness of the response.
- **response_time**: The response_time.
- **item**: The item that collected the response.
- **feedback**: Indicates whether the response should be included in feedback on
accuracy and average response time.

__Example__

~~~ .python
responses.add(response_time=500, correct=1, response='left')
~~~



## clear()

Clears all responses.



__Example__

~~~ .python
responses.clear()
~~~



## reset_feedback()

Sets the feedback status of all responses to False, so that only
new responses will be included in feedback.



__Example__

~~~ .python
responses.reset_feedback()
~~~



</div>

