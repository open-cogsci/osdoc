<div class="ClassDoc YAMLDoc" id="responses" markdown="1">

# class __responses__

The `responses` object contains the history of the responses that were
collected during the experiment.

In addition to the functions listed below, the following semantics are
supported:

__Example__:

~~~ .python
# Loop through all responses, where last-given responses come first
# Each response has correct, response, response_time, item, and feedback
# attributes.
for response in responses:
        print(response.correct)
# Print the two last-given respones
print('last_two responses:')
print(responses[:2])
~~~

[TOC]

<div class="PropertyDoc YAMLDoc" id="responses-acc" markdown="1">

## property __responses.acc__

The percentage of correct responses for all responses that are included in feedback. If there are no responses to give feedback on, 'undefined' is returned.

</div>

[responses.acc]: #responses-acc
[acc]: #responses-acc

<div class="FunctionDoc YAMLDoc" id="responses-add" markdown="1">

## function __responses\.add__\(response=None, correct=None, response\_time=None, item=None, feedback=True\)

Adds a response.

__Example:__

~~~ .python
responses.add(response_time=500, correct=1, response='left')
~~~

__Keywords:__

- `response` -- The response value, for example, 'space' for the spacebar, 0 for joystick button 0, etc.
	- Default: None
- `correct` -- The correctness of the response.
	- Type: bool, int, None
	- Default: None
- `response_time` -- The response_time.
	- Type: float, int, None
	- Default: None
- `item` -- The item that collected the response.
	- Type: str, None
	- Default: None
- `feedback` -- Indicates whether the response should be included in feedback on accuracy and average response time.
	- Type: bool
	- Default: True

</div>

[responses.add]: #responses-add
[add]: #responses-add

<div class="PropertyDoc YAMLDoc" id="responses-avg_rt" markdown="1">

## property __responses.avg_rt__

The average response time for all responses that are included in feedback. If there are no responses to give feedback on, 'undefined' is returned.

</div>

[responses.avg_rt]: #responses-avg_rt
[avg_rt]: #responses-avg_rt

<div class="FunctionDoc YAMLDoc" id="responses-clear" markdown="1">

## function __responses\.clear__\(\)

Clears all responses.

__Example:__

~~~ .python
responses.clear()
~~~

</div>

[responses.clear]: #responses-clear
[clear]: #responses-clear

<div class="PropertyDoc YAMLDoc" id="responses-correct" markdown="1">

## property __responses.correct__

A list of all correct (0, 1, or None) values.

</div>

[responses.correct]: #responses-correct
[correct]: #responses-correct

<div class="PropertyDoc YAMLDoc" id="responses-feedback" markdown="1">

## property __responses.feedback__

A list of the feedback status (True or False) associated with each response.

</div>

[responses.feedback]: #responses-feedback
[feedback]: #responses-feedback

<div class="PropertyDoc YAMLDoc" id="responses-item" markdown="1">

## property __responses.item__

A list of all item names (str or None) associated with each response.

</div>

[responses.item]: #responses-item
[item]: #responses-item

<div class="FunctionDoc YAMLDoc" id="responses-reset_feedback" markdown="1">

## function __responses\.reset\_feedback__\(\)

Sets the feedback status of all responses to False, so that only new responses will be included in feedback.

__Example:__

~~~ .python
responses.reset_feedback()
~~~

</div>

[responses.reset_feedback]: #responses-reset_feedback
[reset_feedback]: #responses-reset_feedback

<div class="PropertyDoc YAMLDoc" id="responses-response" markdown="1">

## property __responses.response__

A list of all response values. (I.e. not response objects, but actual response keys, buttons, etc.)

</div>

[responses.response]: #responses-response
[response]: #responses-response

<div class="PropertyDoc YAMLDoc" id="responses-response_time" markdown="1">

## property __responses.response_time

A list of all response times (float or None).

</div>

[responses.response_time]: #responses-response_time
[response_time]: #responses-response_time

</div>

[responses]: #responses

