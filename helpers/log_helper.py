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
        log_fh = open(filename, "w", encoding=config.FILE_ENCODING)
        logging.basicConfig(
            level=logging.DEBUG,
            format=config.FORMAT)

        formatter = logging.Formatter(config.FORMAT)
        _log_stream_handler = logging.StreamHandler(log_fh)
        _log_stream_handler.setLevel(logging.DEBUG)
        _log_stream_handler.setFormatter(formatter)

        log = logging.getLogger("MAIN")
        log.addHandler(_log_stream_handler)
        _LOGGER = log
    return _LOGGER

#
# end of script
#
