import os
import sys
import pathlib

from viz import get_time_series
from extractor import get_ephys_data

"""
Names: ['Channel_Map-108_100.0', 'Common_Avg_Ref-113_100.0']
IDs: ['0', '1']. 
"""


# ------ hyperparameteres -------#
SORTER = "kilosort3"
STREAM_NAMES = "Common_Avg_Ref-113_100.0"
STREAM_IDS = "1"
# WORK_DIR = os.getenv("LOAD")
WORK_DIR = pathlib.Path(
    "/work/pi_moorman_umass_edu/ephys_chris/CPWI15_2019_06_19_14_17_39_LRRL_220uA"
)
# SAVE_DIR = os.getenv("SAVE")
SAVE_DIR = pathlib.Path(
    "/work/skylerthomas_umass_edu/current_projects/spike_sort/graphs"
)


# -----------------------------------#

name = SAVE_DIR / "test.jpg"
# WORK_DIR /= "experiment1"
recording = get_ephys_data(WORK_DIR, STREAM_NAMES, STREAM_IDS)
get_time_series(recording, (0, 4), name)
