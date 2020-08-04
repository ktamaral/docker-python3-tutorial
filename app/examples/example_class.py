#!/usr/bin/env python3

import os, sys
sys.path.append('./utils')
import json
import logging
logger = logging.getLogger('root')
import csv
from datetime import datetime
from progressbar import ProgressBar
pbar = ProgressBar()

class ExampleClass(object):

  """ Initiator function """
  def __init__(
    self,
    hostname,
    max_rows
    ):

    # Initialize instance variables
    self.hostname = hostname
    self.max_rows = max_rows

  def example_class_function(self):

    print('EXAMPLE CLASS FUNCTION')
    logger.info('HOSTNAME: {}'.format(self.hostname))
    logger.info('MAX ROWS: {} '.format(self.max_rows))
