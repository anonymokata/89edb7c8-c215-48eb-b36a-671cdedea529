import os
import logging
import etc.config as config

__author__ = 'Ken Langer'
_LOGGER = None


def format_log(classname='UNKNOWN', method='UNKNOWN', msg=''):
    return f"[{classname}:{method}] {msg}"


def get_logger(filename=None):
    global _LOGGER
    if _LOGGER:
        pass
    else:
        directory = os.path.dirname(filename)
        create_logger_directory(directory)
        log_fh = open(filename, "w", encoding=config.FILE_ENCODING)
        logging.basicConfig(
            level=config.LOG_LEVEL,
            format=config.FORMAT)

        formatter = logging.Formatter(config.FORMAT)
        _log_stream_handler = logging.StreamHandler(log_fh)
        _log_stream_handler.setLevel(config.LOG_LEVEL)
        _log_stream_handler.setFormatter(formatter)

        log = logging.getLogger("MAIN")
        log.addHandler(_log_stream_handler)
        _LOGGER = log
    return _LOGGER


def create_logger_directory(directory=None):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return

#
# end of script
#
