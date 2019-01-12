#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
from io import open
from argparse import ArgumentParser, FileType, ArgumentDefaultsHelpFormatter
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import logging

from six import text_type as unicode
from six import iteritems
from six.moves import range

LOGFORMAT = "%(asctime).19s %(levelname)s %(filename)s Line %(lineno)s: %(message)s"
logging.basicConfig(format=LOGFORMAT)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
