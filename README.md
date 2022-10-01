# HACKATHON: NASA SPACE APPS 2022
## Challenge: Save the Earth from another Carrington Event.

If a major space weather event like the Carrington Event of 1859 were to occur today, the impacts to society could be devastating. Your challenge is to develop a machine learning algorithm or neural network pipeline to correctly track changes in the peak solar wind speed and provide an early warning of the next potential Carrington-like event.

## Objectives
Your challenge is to develop a machine learning (ML) algorithm or neural network pipeline for the DSCOVR spacecraft's FC instrument to track and follow the changes in the peak solar wind speed so that DSCOVR can continue to provide early warnings of the next potential Carrington-like event that could adversely impact life and property on Earth. You can access historical solar wind data from DSCOVR and other missions to use to train your ML algorithm to correctly detect and track these solar wind peaks.

## Potential Considerations
As you develop your designs, you may (but are not required to) consider the following:
 - Read a notional DSCOVR Faraday Cup instrument “calibration” and data analysis procedure.
## Resources
```python
import cdflib
import spacepy
from spacepy import pycdf
import matplotlib.ploty as plt
import numpy as np
import wget
```
