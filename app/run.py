#!/usr/bin/env python3

import os, sys
# Append config directory to path
sys.path.append('./config')
# Import config
from config import *
# Append utils directory to path
sys.path.append('./utils')
# Import custom logger configuration
from utils import logger as loggerutils
# Initialize custom logger
logger = loggerutils.setup_custom_logger('root')
from examples.example_class import ExampleClass

# Subclass extended from ExampleClass superclass
class ExampleSubClass(ExampleClass):

  def __init__(self):

    """ Get values from config.py file """
    self.hostname = hostname
    self.max_rows = max_rows

    # Call init method in ExampleClass superclass
    super(ExampleSubClass, self).__init__(
      self.hostname,
      self.max_rows
      )

def main():

  # Initialize class instance
  exampleSubClass = ExampleSubClass()
  exampleSubClass.example_class_function()

if __name__ == "__main__":
  main()