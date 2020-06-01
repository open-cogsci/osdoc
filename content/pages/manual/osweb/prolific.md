title:Prolific


[TOC]


## About Prolific

[Prolific](https://prolific.co/) is a commercial tool for recruiting participants for research. To run OSWeb experiments on Prolific, you need to follow the steps explained below.

See also:

- <http://www.jatos.org/Use-Prolific.html>


## Create a study on JATOS

First, import your experiment into JATOS, as described above. Next, go the Worker & Batch Manager, activate the General Multiple Worker, get a URL by clicking on Get Link, and copy it (%FigJatosURL).


%--
figure:
 id: FigJatosURL
 source: jatos-url.png
 caption: Get a study URL from JATOS.
--%



## Create a study on Prolific

Next, create a study on Prolific. Under Study Details (%FigProlific), insert the JATOS study URL in the field labeled "What is the URL of your study?". This will tell Prolific how to start the experiment. Importantly, add the following to the end of the URL (this will pass important information from Prolific to your experiment):

```
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```

When the experiment is finished, Prolific needs to know about it. For this purpose, Prolific uses an End Redirect URL, which is listed in the field labeled "To prove that participants have completed your study …". Copy this End Redirect URL. Also check the box labeled "I've set up my study to redirect to this url at the end".

%--
figure:
 id: FigProlific
 source: prolific.png
 caption: Study details on Prolific.
--%



## Set an End Redirect URL in JATOS

Now go back to JATOS, and open the Properties of your study (%FigJatosProperties). There, paste the End Redirect URL that you have copied from Prolific in the field labeled "End Redirect URL". This will tell JATOS that the participant should be redirected back to Prolific when the experiment is finished, so that Prolific knows that the participant completed the experiment.


%--
figure:
 id: FigJatosProperties
 source: jatos-properties.png
 caption: Set the End Redirect URL in JATOS.
--%


## Register Prolific information in your experiment

Every participant from Prolific is identified by a unique ID. It's important to log this ID in your experiment, because this allows you to tell which participant from Prolific corresponds to which entry in the JATOS results. You can do this by adding the script below in the Prepare phase of an `inline_javascript` item at the very start of your experiment.

When running the experiment through Prolific, this will make the Prolific ID available as the experimental variable `prolific_participant_id`. When the running the experiment in any other way (e.g. during testing), the variable `prolific_participant_id` will be set to -1. The same logic applied to the Prolific Study ID (`prolific_study_id`) and the Prolific Session ID (`prolific_session_id`).


```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('Prolific information is available')
    vars.prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    vars.prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    vars.prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('Prolific information is not available (setting values to -1)')
    vars.prolific_participant_id = -1
    vars.prolific_study_id = -1
    vars.prolific_session_id = -1
}
console.log('prolific_participant_id = ' + vars.prolific_participant_id)
console.log('prolific_study_id = ' + vars.prolific_study_id)
console.log('prolific_session_id = ' + vars.prolific_session_id)
```


## Test the study

Go back to the Study Details page on Prolific. At the bottom of the page, there is a Preview button. This allows you to test the experiment by acting as a participant yourself. Don't forget to check the JATOS results to make sure that the experiment has successfully finished, and that all the necessary information (including the Prolific information) has been logged!
