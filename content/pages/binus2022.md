title: Binus University 2022 workshop


[TOC]


## Practical information

- Host: Binus University
- Location: online
- Dates: 
    - Day 1: Friday, April 1st, 2022, 08:00-12:00 CEST, 13:00 - 17:00 Jakarta
    - Day 2: Wednesday, April 20th, 2022, 08:00-12:00 CEST, 13:00 - 17:00 Jakarta
    - Day 3: Thursday, April 21st, 2022, 08:00-12:00 CEST, 13:00 - 17:00 Jakarta
    - Day 4: Wednesday, April 27th, 2022, 08:00-12:00 CEST, 13:00 - 17:00 Jakarta
- Presenter: Sebastiaan Mathôt
- [Spreadsheet with participant overview](https://binusianorg.sharepoint.com/sites/WyLab/_layouts/15/guestaccess.aspx?guestaccesstoken=wvSvcpJoabwkk99w%2BuZhpJX58EgC6O4ug%2FgWYbN4H%2BI%3D&docid=2_15f25248401074bb79187e333dcb63088&rev=1&e=iPtB1U)


## Description

In this four-day, hands-on, online workshop, you will learn how to implement psychological experiments with the open-source software OpenSesame. You will learn:

- How to run experiments online as well as in a traditional laboratory set-up.
- The limitations and advantages of online and laboratory-based experiments.
- How to include eye tracking in laboratory-based experiments. (And a sneak-peak at eye-tracking in online experiments!)
- How to analyze data collected from online and laboratory-based experiments.

Finally, using the skills that you will learn during the workshop, you will design and implement an experiment for your own research, of course with assistance from us! For this purpose, please already think about what kind of experiment you'd like to create, and indicate this in the [participant spreadsheet](https://binusianorg.sharepoint.com/sites/WyLab/_layouts/15/guestaccess.aspx?guestaccesstoken=wvSvcpJoabwkk99w%2BuZhpJX58EgC6O4ug%2FgWYbN4H%2BI%3D&docid=2_15f25248401074bb79187e333dcb63088&rev=1&e=iPtB1U). If you're unsure what kind of experiment you'd like to create, take a look a the list of suggested experiments below.

Please install OpenSesame on your computer before the workshop. You can download OpenSesame for free from <https://osdoc.cogsci.nl/>. No prior experience with OpenSesame, Python, or JavaScript is required.

I’m looking forward to meeting you all!

— Sebastiaan


## Day 1: Introduction (April 1)

Slides: %static:attachments/binus2022/binus-day-1.pdf%

- 13:00 – 14:30: __Introduction to OpenSesame__. A general introduction to the software OpenSesame, followed by a hands-on tutorial in which you will learn the basic concepts of the software.
- Break
- 15:00 – 16:00: __Introduction to OpenSesame (continued)__.
- 16:00 – 17:00: __Free time to develop your own experiment__. What kind of experiment would you like to build for your own research? You will draft a design for your own experiment, which you will continue to work on during the rest of the workshop.


## Day 2: Online experiments (April 20)

Slides: %static:attachments/binus2022/binus-day-2.pdf%

- 13:00 – 14:30: __Building an online task (cats, dogs, and capybaras)__. We will start this session with a general introduction to online experiments. This is followed by a hands-on tutorial in which you will implement a task that is suitable for running online. The tutorial includes various assignments of different difficulty levels.
- Break
- 15:00 – 16:00: __Using <https://mindprobe.eu> (a JATOS server) to run experiments online__. In this session, you will learn how to use mindprobe.eu, which is a free server that runs the open-source software JATOS, to actually run an experiment online. A mindprobe.eu account will be provided to each participant.
- 16:00 – 17:00: __Free time to develop your own experiment__. During this session, you will continue to work on your own experiment.


## Day 3 : Eye-tracking experiments (April 21)

Slides: %static:attachments/binus2022/binus-day-3.pdf%

- 13:00 – 14:30: __Building a self-paced reading task with eye-tracking__. We will start this session with a general introduction to eye tracking. This is followed by a hands-on tutorial in which you will implement a self-paced reading task with basic eye tracking. We will focus on using the EyeLink, which is a specific eye tracker. However, concepts and techniques are largely also applicable to other eye trackers. We will also briefly look at eye tracking in online experiment with WebGazer.js.
- Break
- 15:00 – 16:00: __Gaze-contingent eye-tracking.__ You will learn how to implement experiments that react to the eye movements of the participant, that is, gaze-contingent experiments.
- 16:00 – 17:00: __Free time to develop your own experiment.__ During this session, you will continue to work on your own experiment.


## Day 4: Data analysis (April 27)

Slides: %static:attachments/binus2022/binus-day-4.pdf%

- 13:00 – 14:30: __Getting data ready for analysis.__ We will start this session with a general explanation of how data is structured, both for experiments that are conducted online and for experiments that are conducted in a traditional laboratory set-up. Next, we will see how to transform this data into a format that lends itself to statistical analysis in the free statistical software JASP. Specifically, we will learn how data from multiple participants can be merged into a single .csv spreadsheet; we will also learn how data from an online experiment can be downloaded from JATOS and converted to a .csv spreadsheet; finally, we will learn how to create a so-called ‘pivot table’, which lends itself to analysis in JASP.
- Break
- 15:00 – 16:30: __Conducting a statistical analysis__. We will use the open-source software JASP to perform statistical tests.
- 16:30 – 17:00: __Q&A__. We will close the workshop with time for questions and remarks.


## Suggested experiments

A list of experiments that are easy to implement, with references to papers that contain a clear results section.

- Attention network task (ANT)
    - Fan, J., McCandliss, B. D., Sommer, T., Raz, A., & Posner, M. I. (2002). Testing the efficiency and independence of attentional networks. *Journal of cognitive neuroscience*, *14*(3), 340-347.
- Posner cueing task
    - For a version that focuses specifically on inhibition of return (IOR), see: Klein, R. M. (2000). Inhibition of return. *Trends in cognitive sciences*, *4*(4), 138-147.
- Implicit association test (IAT)
    - For a replication study, see Johnson, D. J., Ampofo, D., Erbas, S. A., Robey, A., Calvert, H., Garriques, V., ... & Dougherty, M. (2021). Cognitive Control and the Implicit Association Test: A Replication of Siegel, Dougherty, and Huber (2012). *Collabra: Psychology*, *7*(1), 27356.
    - See also <https://osdoc.cogsci.nl/3.3/tutorials/iat>
- Color categorization, a test for the Sapir-Whorf hypothesis. Note that stimulus creation might be challenging
    - Brown, A. M., Lindsey, D. T., & Guckes, K. M. (2011). Color names, color categories, and color-cued visual search: Sometimes, color perception is not categorical. *Journal of vision*, *11*(12), 2-2.
- Cognitive reflection task
    - Sirota, M., & Juanchich, M. (2018). Effect of response format on cognitive reflection: Validating a two-and four-option multiple choice question version of the Cognitive Reflection Test. *Behavior Research Methods*, *50*(6), 2511-2522.
- Attentional capture task.
    - Theeuwes, J. (1992). Perceptual selectivity for color and form. *Perception & Psychophysics*, *51*(6), 599–606. <https://doi.org/10.3758/BF03211656>
- Visual-search task.
    - Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, *12*(1), 97–136. <https://doi.org/10.1016/0010-0285(80)90005-5>
    - See also <https://osdoc.cogsci.nl/3.3/tutorials/intermediate-javascript>
