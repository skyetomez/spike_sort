from extractor import get_ephys_data
import spikeinterface.spikeinterface.extractors as se

# Sources/Rhythm FPGA <- refers to the hardware used for data collection

# ----- preprocessing of signal ---
# Get ephys data

LOWER_CF = 
UPPER_CF = 
TMP = ""

recording = get_ephys_data(TMP)


def clean_ephys_data(raw_recording):
    # Filters/Channel Map <- get channels

    # AVAI: Filters/Common Avg Ref <- Gain applied to selected channels. channels are selected to compute average and this is applied to other channels
    averaged = se.common_reference(raw_recording, operator="average", reference="global")

    # Utilities/Splitter <- paraprocessing e.g. HPF for spike detect, LPF local field pot.

    # AVAI: Filters/Bandpass Filter <- range for filter
    se.bandpass_filter(averaged, freq_min = LOWER_CF, freq_max= UPPER_CF )

    # Utilities/Splitter <- repeat
    return recording


# Sinks/LFP Viewer <- local field potential viewer

# Filters/Spike Detector <- Detects spikes in continuous data and packages in events

# Sinks/Spike Viewer <- local field potential viewer

# Filters/Spike Detector <- Detects spikes in continuous data and packages in events


# RAWBINARY RECORD ENGINE buffer 1024


if __name__ == "__main__":
    pass
