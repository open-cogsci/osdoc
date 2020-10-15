title: Sona Systems


[TOC]


## About Sona Systems

Sona Systems is an online tool that many universities use for recruiting participants, granting course credit to student participants, etc.

See also:

- <https://www.sona-systems.com/help/integration_test.aspx>


## Create a study on JATOS

First, import your experiment into JATOS, as described above. Next, go the Worker & Batch Manager, activate the General Multiple Worker, get a URL by clicking on Get Link, and copy it.


## Create a study on Sona Systems

Next, create a study on Sona Systems. Insert the JATOS study URL in the field labeled "Study URL". This will tell Sona Systems how to start the experiment. Importantly, add the following to the end of the URL (this will pass the participant's Sona ID to your experiment):

```
&SONA_ID=%SURVEY_CODE% 
```

Sona Systems does not use a Redirect URL. This means that Sona Systems will not automatically know whether or not the participant finished the study.


## Register the Sona ID in your experiment

Every participant from Sona is identified by a unique ID. It's important to log this ID in your experiment, because this allows you to tell which participant from Sona corresponds to which entry in the JATOS results. You can do this by adding the script below in the Prepare phase of an `inline_javascript` item at the very start of your experiment.

When running the experiment through Sona, this will make the Sona ID available as the experimental variable `sona_participant_id`. When the running the experiment in any other way (e.g. during testing), the variable `sona_participant_id` will be set to -1. 


```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('Sona information is available')
    vars.sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('Sona information is not available (setting value to -1)')
    vars.sona_participant_id = -1
}
console.log('sona_participant_id = ' + vars.sona_participant_id)
```
