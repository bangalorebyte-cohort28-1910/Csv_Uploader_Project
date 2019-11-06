# Logging in Python

## What is Logging?

Logging is a means of tracking events that happen when some software runs.

Logs provide developers with an extra set of eyes that are constantly looking at the flow that an application is going through. 

## Why do we need to Log?

Logging is important for software developing, debugging and running. 
If you don’t have any logging record and your program crashes, there are very little chances that you detect the cause of the problem. And if you detect the cause, it will consume a lot of time. 
With logging, you can leave a trail of breadcrumbs so that if something goes wrong, we can determine the cause of the problem.

They can store information, like which user or IP accessed the application. If an error occurs, then they can provide more insights than a stack trace by telling you what the state of the program was before it arrived at the line of code where the error occurred.

## The Logging Module

Python has a built-in module logging which allows writing status messages to a file or any other output streams.

The logging module in Python is a ready-to-use and powerful module that is designed to meet the needs of beginners as well as enterprise teams.

## Levels of Log Message

There are few built-in levels of the log message.

> Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
> Info : These are used to Confirm that things are working as expected
> Warning : These are used an indication that something unexpected happened, or indicative of some problem in the near future
> Error : This tells that due to a more serious problem, the software has not been able to perform some function
> Critical : This tells serious error, indicating that the program itself may be unable to continue running

If required, developers have the option to create more levels but these are sufficient enough to handle every possible situation. Each built-in level has been assigned its numeric value.

10 - Debug 
20 - Info
30 - Warning
40 - Error
50 - Critical

Logging module is packed with several features. It has several constants, classes, and methods. The items with all caps are constant, the capitalize items are classes and the items which start with lowercase letters are methods.

There are several logger objects offered by the module itself.

    Logger.info(msg) : This will log a message with level INFO on this logger.
    Logger.warning(msg) : This will log a message with level WARNING on this logger.
    Logger.error(msg) : This will log a message with level ERROR on this logger.
    Logger.critical(msg) : This will log a message with level CRITICAL on this logger.
    Logger.log(lvl,msg) : This will Logs a message with integer level lvl on this logger.
    Logger.exception(msg) : This will log a message with level ERROR on this logger.
    Logger.setLevel(lvl) : This function sets the threshold of this logger to lvl. This means that all the messages below this level will be ignored.
    Logger.addFilter(filt) : This adds a specific filter filt to the to this logger.
    Logger.removeFilter(filt) : This removes a specific filter filt to the to this logger.
    Logger.filter(record) : This method applies the logger’s filter to the record provided and returns True if record is to be processed. Else, it will return False.
    Logger.addHandler(hdlr) : This adds a specific handler hdlr to the to this logger.
    Logger.removeHandler(hdlr) : This removes a specific handler hdlr to the to this logger.
    Logger.hasHandlers() : This checks if the logger has any handler configured or not.


## Let's Start [Adding logging to your Python program]

First step would be

```
import logging
```

```
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

    Output of above ::

        WARNING:root:This is a warning message
        ERROR:root:This is an error message
        CRITICAL:root:This is a critical message

The output shows the severity level before each message along with root, which is the name the logging module gives to its default logger. (Loggers are discussed in detail in later sections.) 
This format, which shows the level, name, and message separated by a colon (:), is the <strong>default output format</strong> that can be configured to include things like timestamp, line number, and other details.

Notice that the debug() and info() messages didn’t get logged. This is because, by default, the logging module logs the messages with a severity level of WARNING or above.


## Basic Configurations

Some of the commonly used parameters for basicConfig() are the following:

> level: The root logger will be set to the specified severity level.
> filename: This specifies the file.
> filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
> format: This is the format of the log message.

    ### Level

    By using the level parameter, you can set what level of log messages you want to record.

    ```
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.debug('This will get logged')
    ```

    All events at or above DEBUG level will now get logged.

        Output :: DEBUG:root:This will get logged

    ### filename | filemode | format

    Similarly, for logging to a file rather than the console, filename and filemode can be used, and you can decide the format of the message using format. The following example shows the usage of all three:

    ```
    import logging

    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')
    ```

        Output :: root - ERROR - This will get logged to a file

    The message will look like this but will be written to a file named app.log instead of the console. The filemode is set to w, which means the log file is opened in “write mode” each time basicConfig() is called, and each run of the program will rewrite the file. The default configuration for filemode is a, which is append.


More about basicConfig() can be found from here :

https://docs.python.org/3/library/logging.html#logging.basicConfig


debug(), info(), warning(), error(), and critical() also call basicConfig() without arguments automatically if it has not been called before. This means that after the first time one of the above functions is called, you can no longer configure the root logger because they would have called the basicConfig() function internally.

The default setting in basicConfig() is to set the logger to write to the console in the following format:

    ERROR:root:This is an error message






## logging.shutdown()

Informs the logging system to perform an orderly shutdown by flushing and closing all handlers. 
This should be called at application exit and no further use of the logging system should be made after this call.


# Sources ::

https://realpython.com/python-logging/

https://docs.python.org/3/library/logging.html