from __future__ import absolute_import
from __future__ import division

import math
import os

from io import BytesIO

import numpy as np

from PIL import Image


def saver(
    filename, output_dir, pred, ground=None, flag=None,
):
    """Write output predictions to file

    Parameters
    ----------
    filename : string
        Input filename.
    output_dir : string
        Output directory
    pred : string
        Predicted output.
    pad_width : int
        Padded image width in pixels used as model input.
    pad_height : int
        Padded image height in pixels used as model input.
    ground : string or None, optional (default=None)
        Ground truth label.
    flag : bool or None, optional (default=None)
        Incorrect prediction flag.

    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(f"{output_dir}/outputs.txt", "a") as f:
        f.write(filename, " ", pred, " ", ground)
        f.write("\n")
