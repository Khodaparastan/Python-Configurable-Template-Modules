## Example Usase in main module


```python
from logger_module import setup_logger

# Set up the logger using the configuration file
logger = setup_logger('path/to/logging_config.json')

# Use the logger as needed
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')

```

