import spikeinterface.preprocessing as sp  # type: ignore

# import spikeinterface.toolkit as st  # type: ignore

""" 
CPWI17_2019_10_19_20_19_260uA_RLLRRL

Is parallel processing enabled by default? 
Channel 67 assumed for the CAR 
Channels 64-67 recorded individually and seprately (@ CHANNEL MAP) had behavioral event occur. 
(?)Acceleramoter channels. 
Lowpass = 300, Highpass = 6000
Good example on 19,20 38,45,49,53,55

29-32 TAN very cool; good exampe. 


"""

# think about visual output for this


# Sources/Rhythm FPGA <- refers to the hardware used for data collection

# ------------ preprocessing of signal -------------
# Get ephys data

LOWER_CF = 300
UPPER_CF = 6000


# Filters/Channel Map <- get channels
def get_channels():
    """
    This is how the channels are grouped together;
    """
    pass


# Sinks/Spike Viewer <- local field potential viewer
# def get_LFP(recording, resample_rate: int = 1000):
#     return st.preprocessing.resample(recording, resample_rate=resample_rate)


# def get_MUA(recording, resample_rate: int = 1000):
#     tmp = st.preprocessing.rectify(recording)
#     tmp = st.preprocessing.resample(tmp, resample_rate)
#     return tmp


def clean_ephys_data(raw_recording):
    # Utilities/Splitter <- paraprocessing e.g. HPF for spike detect, LPF local field pot.
    # AVAI: Filters/Bandpass Filter <- range for filter
    filtered = sp.bandpass_filter(raw_recording, freq_min=LOWER_CF, freq_max=UPPER_CF)
    # Utilities/Splitter <- repeat
    return filtered


# RAWBINARY RECORD ENGINE buffer 1024


if __name__ == "__main__":
    pass
