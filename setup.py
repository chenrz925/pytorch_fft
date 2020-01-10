import os
import sys

from setuptools import setup, find_packages

import build

this_file = os.path.dirname(__file__)

setup(
    name="pytorch_fft_waterch",
    version="0.15",
    description="A PyTorch wrapper for CUDA FFTs modified by Runze Chen to adapt PyTorch upper than 1.0.1",
    url="https://github.com/chenrz925/pytorch_fft",
    author="Runze Chen",
    author_email="chen.runze@ieee.org",
    # Require cffi.
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    # Exclude the build files.
    packages=find_packages(exclude=["build"]),
    # Package where to put the extensions. Has to be a prefix of build.py.
    ext_package="",
    # Extensions to compile.
    cffi_modules=[
        os.path.join(this_file, "build.py:ffi")
    ],
)