title: WebGazer.js

Requires OSWeb v1.4.6.1
{:.page-notification}

[TOC]


## About WebGazer

WebGazer.js is an eye-tracking library written in JavaScript. You can include it with OSWeb to perform eye tracking in online experiments.

- <https://webgazer.cs.brown.edu/>


## Including WebGazer.js in the experiment

WebGazer.js is not bundled with OSWeb by default. However, you can include it as an external library by entering a link to `webgazer.js` under External JavaScript libraries. Currently, a functional link is:

```
https://webgazer.cs.brown.edu/webgazer.js
```

See also:

- %link:manual/osweb/osweb%


## Example experiment

Below you can download an example experiment that uses WebGazer.js. Participants are first asked to click on and look at a set of dots; this will cause WebGazer.js to automatically perform something akin to a calibration procedure. Next, the experiment shows a simple screen to test the accuracy of gaze-position recording. In general, fine-grained eye tracking is not feasible, but you can tell which quadrant of the screen a participant is looking at. To run this experiment, you need include WebGazer.js in the experiment, as described above. 

- %static:attachments/webgazer.osexp%

You can also launch the experiment directly in the browser:

- <https://jatos.mindprobe.eu/publix/BowSAFY2VWl>
