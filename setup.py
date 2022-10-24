#!/bin/env python

#######################################################################
# Copyright (C) 2022 Julian Dosch
#
# This file is part of fas_disorder_addon.
#
#  fas_disorder_addon is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  fas_disorder_addon is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with fas_disorder_addon.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################


from setuptools import setup, find_packages

with open("README.md", "r") as input:
    long_description = input.read()

setup(
    name="FAS Disorder Addon",
    version="1.0",
    python_requires='>=3.9.0',
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Julian Dosch",
    author_email="Dosch@bio.uni-frankfurt.de",
    url="",
    packages=find_packages(),
    package_data={'': ['*']},
    install_requires=[
        'biopython',
        'tqdm',
        'GitPython',
        'pathlib',
    ],
    entry_points={
        'console_scripts': ["fas.DisPred.predict = fas_disorder_addon.predict_disorder:main",
                            "fas.DisPred.setup = fas_disorder_addon.install_aucpred:main"
                            ],
    },
    license="GPL-3.0",
    classifiers=[
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
