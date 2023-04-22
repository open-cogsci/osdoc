title: Tobii

PyGaze offers *experimental* support for Tobii eye trackers. The `tobii-research` package can be installed through `pip`, but at the time of writing it requires a specific version of Python—and *which* version of Python it requires varies from release to release. Therefore, the first step is to find out which version of Python you need. You can do that by visiting the `tobii-research` on PyPi and clicking on 'Download files':

- <https://pypi.org/project/tobii-research/#files>

From the file names, you can tell which version of Python you need; for example, the `cp310` in the name 
`tobii_research-1.10.2-cp310-cp310-win_amd64.whl` means that you need Python 3.10 (`cp` stands for C-Python).

Next, install OpenSesame in a Python environment of the correct version (so Python 3.10 for version 1.10.2 of `tobii-research` as shown above). This most easily done using Anaconda, as described [here](%url:download%). Finally, install the `tobii-research` package into this Python environment.

```
!pip install tobii-research
```


For more information, see:

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>
