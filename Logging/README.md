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

```markdown
# Logging Levels

Logging levels are used to categorize the urgency and type of logs. They help in filtering logs based on their severity which is crucial for both development and production diagnostics. Below are the standard logging levels in Python's `logging` module, sorted from the least to the most severe:

## DEBUG
Value: 10  
Description:  
- Detailed information, typically of interest only when diagnosing problems.
- Use for tracing program execution, variable values, or processing paths.

## INFO
Value: 20  
Description:
- Confirmation that things are working as expected.
- General messages that confirm the program is functioning as expected.

## WARNING
Value: 30  
Description:
- An indication that something unexpected happened or may happen in the near future.
- The software is still working as expected, but the condition should be monitored.

## ERROR
Value: 40  
Description:
- The software has not been able to perform some function due to a more serious problem.
- Indicates a failure in the application's functionality that should be investigated.

## CRITICAL
Value: 50  
Description:
- A serious error indicating that the program itself may be unable to continue running.
- Represents a critical issue that typically requires immediate attention.

When configuring logging, you can set the logging level to determine the minimum severity of messages that will be logged. For example, setting the level to `INFO` will log messages classified as `INFO`, `WARNING`, `ERROR`, and `CRITICAL`, but will exclude `DEBUG` messages.

```
