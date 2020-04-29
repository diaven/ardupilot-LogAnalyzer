# ardupilot LogAnalyzer for python 3.x

this is a port of [this](https://github.com/ArduPilot/ardupilot/tree/master/Tools/LogAnalyzer) LogAnalyzer by ardupilot to support python 3.x (tested with python 3.6).

I just adapted the features I need, so I might have missed something.

## how to use

this is how I use it...
```python
from LogAnalyzer.DataflashLog import DataflashLog

logdata = DataflashLog("path_to_log_file.BIN", format='bin', ignoreBadlines=True)
```
