import pathlib
import matplotlib.pyplot as plt

import spikeinterface.widgets as sw  # type: ignore


# SAVE_DIR = pathlib.Path("/work/skylerthomas_umass_edu/current_projects/spike_sort/graphs")
# plt.rcParams["figure.figsize"] = (20, 12)


def get_time_series(recording, window: tuple, name) -> None:
    plt.style.use("ggplot")
    fig = plt.figure(figsize=(12, 5), dpi=200)
    ax = fig.gca()

    tmp = sw.plot_timeseries(
        recording=recording,
        time_range=window,
        figure=fig,
    )

    fig.savefig(
        name, dpi="figure", format="jpg", pad_inches=0.1, orientation="landscape"
    )

    return None


def get_probe_map(recording, name) -> None:
    probe_map = sw.plot_probe_map(recording)
    plt.savefig(fname=name)
    return None
