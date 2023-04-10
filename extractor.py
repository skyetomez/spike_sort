import spikeinterface.extractors as se  # type:ignore
from preprocess import clean_ephys_data

"""
Path has same stem across systems only the parent directories vary. 
"""


def get_ephys_data(path, stream_names, stream_ids):
    """
    This will probably return the original "Open Ephys" data format
    """
    recording_oe = se.read_openephys(
        folder_path=path, stream_id=stream_ids, stream_name=stream_names
    )
    return clean_ephys_data(recording_oe)


if __name__ == "__main__":
    pass
