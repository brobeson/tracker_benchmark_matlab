"""
Fix results filenames.

The results files were written on Windows, which is case insensitive. The
filenames are a mix of upper and lower case. This script fixes known
erroneous filenames to be entirely uppercase. Without this fix, the benchmark
fails to find some of the results on Linux. This causes the benchmark to fail
outright.
"""

import argparse
import glob
import os
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument("results_path", default="./results", nargs="?")
arguments = parser.parse_args()
arguments.results_path = os.path.abspath(os.path.expanduser(arguments.results_path))

# List the trackers that have names in lower case. These need to be converted to upper case.
trackers = ["bsbt", "cpf", "ivt", "sbt", "sms"]
for tracker in trackers:
    files = glob.glob(
        os.path.join(arguments.results_path, f"**/*{tracker}.mat"), recursive=True
    )
    capital_tracker = tracker.upper()
    for f in files:
        os.rename(f, f.replace(f"_{tracker}.mat", f"_{capital_tracker}.mat"))
