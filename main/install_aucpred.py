#!/bin/env python

#######################################################################
# Copyright (C) 2022 Julian Dosch
#
# This file is part of disorder_wrapper.
#
#  disorder_wrapper is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PathwayTrace is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with disorder_wrapper.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################


import os
import sys
from sys import platform
from pathlib import Path
import shutil
import subprocess
import argparse
import gnureadline
import glob
from os.path import expanduser
import ssl
import urllib.request
import time


home = expanduser('~')


def download_progress(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    if percent > 100:
        percent = 100
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                     (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


def download_file(url, file):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    download_file = urllib.request.URLopener(context=ctx)
    print('Downloading %s' % (url + '/' + file))
    download_file.retrieve(url + '/' + file, file, download_progress)
    print(' ... done!')


def main():
    parser = argparse.ArgumentParser(epilog="Annotates intrinsically disordered region for a multifasta file using AUCpred and puts it in the FAS json format.")
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument("-p", "--path", default='.', type=str, required=True,
                          help="install path for PredictProperty")
    required.add_argument("-o", "--outPath", default='.', type=str, required=True,
                          help="path to output directory. File will be named after fasta file")
    optional.add_argument("-t", "--tmp", default='.', type=str, required=False,
                          help="Path to a temporary directory.")
    optional.add_argument("--cpus", default=1, type=int, required=False,
                          help="number of cpus used")
    optional.add_argument("-a", "--aucpred", default=None, type=str, required=False,
                          help="Path to aucpred")
    args = parser.parse_args()
    run_anno(args.input, args.outPath, args.tmp, args.cpus, args.aucpred)


if __name__ == '__main__':
    main()
