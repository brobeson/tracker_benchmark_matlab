# tracker_benchmark_matlab

A "fork" of the Matlab version of the [Visual Tracker
Benchmark](http://cvlab.hanyang.ac.kr/tracker_benchmark/index.html).

## Omitted Files

Binary files are omitted from this repository. To acquire them, [download the
original benchmark](http://cvlab.hanyang.ac.kr/tracker_benchmark/index.html)
and copy them here. These are the directories you need to copy:

- *results/*
- *tmp/*
- *trackers/*

⚠️ Some of the files in *results* cannot be found by the benchmark if you run it
on Linux. The benchmark was written, and apparently only tested, on Windows.
Linux file systems are case sensitive. You can fix this by running the Python
script [*util/fix_results.py*](util/fix_results.py): `python3
util/fix_results.py`

## Running the Benchmark

⚠️ I am only testing this with [GNU
Octave](https://www.gnu.org/software/octave/). I don't have Matlab installed and
have intention of paying for a license.

### Running Trackers

### Generating Performance Graphs

1. Run the [perfPlot.m](perfPlot.m) script: `octave perfPlot.m`

### Generating Imagery with Bounding Boxes
