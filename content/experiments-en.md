---
layout: osdoc
title: Experiments
group: General
permalink: /experiments/
---

This page contains a list of paid experiments for which we are recruiting participants.

*[Voir cette page en française](/experiences)*

Overview
--------

- [General instructions](#instructions)
	- [Requirements](#requirements)
	- [Downloading and running an experiment](#download)
	- [Savind and sending the data files](#data)
	- [Payment](#payment)
- [Available experiments](#experiments)
- [Troubleshooting](#troubleshooting)

General instructions {#instructions}
--------------------

### Requirements {#requirements}

- Participants must be students of Aix-Marseille Université.
- The instructions below are for Windows XP / 7.
- If you are running Linux, please send an e-mail to <experiments@cogsci.nl> to receive instructions.
- Mac OS is currently not supported.

### Downloading and running an experiment {#download}

- First, send an e-mail to <experiments@cogsci.nl> to indicate that you want to participate in the experiment. Please mention the experiment code (e.g. *0001A1*) and your student number. You will receive a confirmation.
- Download the experiment (a `.zip` file) using the links provided under [Available experiments](#experiments).
- Extract the `.zip` file to a location of your choice.
- Open the experiment folder (e.g., `experiment-0001A1`).
- To start one session, double-click on `RUN_SESSION.BAT`.
- Carefully read the instructions on the screen.
- If the experiment consists of multiple sessions, you need to run `RUN_SESSION.BAT` multiple times. For example, if the number of sessions is 3, you need to start `RUN_SESSION.BAT` three times.

### Saving and sending the data {#data}

- Once you have completed a session, your data will be saved as `my_data.csv`.
- Rename `my_data.csv` so that it includes your name and the session number (e.g. `sebastiaan_01.csv`). 
- Once you have completed all sessions, send all data files by e-mail to <experiments@cogsci.nl>. If an experiment consists of multiple sessions, you need to send all data files (`sebastiaan_01.csv`, `sebastiaan_02.csv`, etc.).

## Payment {#payment}

You can receive the payment by bank transfer or appointment. You will only receive payment if all data has been successfully received before the deadline of the experiment.

### By bank transfer (no appointment necessary)

Sign in the receipt (*formulaire de paiement*) and consent (*formulaire de consentement*) form that are included with the experiment (you can request them via <experiments@cogsci.nl> if they are not included), and send a scan or high-quality photograph of both forms to <experiments@cogsci.nl>. Please also include your banking details. The payment will be transferred as soon as the forms have been received,

### By appointment

When sending the data, indicate that you would like to make an appointment for collecting the payment. This will be at the St. Charles campus of the Aix-Marseille university. Please bring your social security number, which is required for the receipt.

Available experiments {#experiments}
---------------------

{% include experiments %}

Troubleshooting {#troubleshooting}
---------------

If you run into trouble, please first check [the instructions](#instructions) outlined above. If you cannot resolve your problem, please send an email to <experiments@cogsci.nl> with a clear description of the problem, including any error message.

- *Known issue:* You may run into the error message `Error: 'ascii' codec can't decode byte [...] in position [...]` if the experiment is placed in a folder that contains special character ('é', 'ça', etc.). For example, the folder `c:\Documents and Settings\Name with special châractérès\My documents\experiment` results in an error. To resolve this issue, place the folder in a location that does not contain any special characters, such as `c:\experiment`.

