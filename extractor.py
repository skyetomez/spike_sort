import pathlib

import spikeinterface.extractor as se

path = "/home/skylerthomas_umass_edu/work/current_projects/spike_sort/CPWI15_2019-06-19_14-17-39_LRRL 220uA"
path = pathlib.Path(path)


def get_ephys_data(path):
    """
    This will probably return the original "Open Ephys" data format
    """
    recording_oe = se.read_openephys(file_path=path)


if __name__ == "__main__":
    x = get_ephys_data(path)
    print(type(x))
    print(x)
