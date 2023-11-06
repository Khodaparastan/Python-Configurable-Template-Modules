import logging
from logging.handlers import RotatingFileHandler
import os
import json

def setup_logger(config_path='logging_config.json'):
    # Read configuration from JSON file
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)['handlers']

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Capture all logs, regardless of level

    # File Handler Configuration
    if config['file']['enabled']:
        # Ensure the directory for the log file exists
        log_dir = os.path.dirname(config['file']['filename'])
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_handler = RotatingFileHandler(
            config['file']['filename'],
            maxBytes=config['file']['max_bytes'],
            backupCount=config['file']['backup_count']
        )
        file_formatter = logging.Formatter(
            config['file']['formatter'],
            datefmt=config['file']['datefmt']
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(getattr(logging, config['file']['level'].upper()))
        logger.addHandler(file_handler)

    # Console Handler Configuration
    if config['console']['enabled']:
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter(
            config['console']['formatter'],
            datefmt=config['console']['datefmt']
        )
        stream_handler.setFormatter(stream_formatter)
        stream_handler.setLevel(getattr(logging, config['console']['level'].upper()))
        logger.addHandler(stream_handler)

    return logger
