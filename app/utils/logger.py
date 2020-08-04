import logging
import logging.handlers
import os

hostname = os.uname().nodename

def setup_custom_logger(name):
    # Logger config
    log_file = '/home/logs/{}.log'.format(hostname)
    log_file_max_size = 1024 * 1024 * 20 # megabytes
    log_num_backups = 3
    log_format = '%(asctime)s [%(levelname)s]: %(filename)s(%(funcName)s:%(lineno)s) >> %(message)s'
    log_date_format = '%m/%d/%Y %I:%M:%S %p'
    log_filemode = 'a'

    # Initialize config
    logging.basicConfig(
      filename=log_file,
      format=log_format,
      filemode=log_filemode,
      level=logging.DEBUG
    )
    # Configure file rotation
    rotate_file = logging.handlers.RotatingFileHandler(
      log_file, maxBytes=log_file_max_size, backupCount=log_num_backups
    )
    # Get logger
    logger = logging.getLogger(name)
    # Add file rotation handler
    logger.addHandler(rotate_file)

    # Console log messages
    consoleHandler = logging.StreamHandler()
    # Configure console log formatter
    logFormatter = logging.Formatter(log_format)
    # Add console log formatter
    consoleHandler.setFormatter(logFormatter)
    # Add console log handler
    logger.addHandler(consoleHandler)

    return logger