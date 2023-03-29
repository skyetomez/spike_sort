import pathlib
import spikeinterface.extractor as se


"""
Path has same stem across systems only the parent directories vary. 
"""

path_stem = "CPWI15_2019_06-19_14-17-39_LRRL_220uA"

work_dir = "/home/skylerthomas_umass_edu/work/current_projects/spike_sort/"
work_dir = pathlib.Path(work_dir)
path = work_dir / path_stem


def get_ephys_data(path):
    """
    This will probably return the original "Open Ephys" data format
    """
    recording_oe = se.read_openephys(file_path=path)




if __name__ == "__main__":
    x = get_ephys_data(path)
    print(type(x))
    print(x)
