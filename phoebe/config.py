# package.module
# module description
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  timestamp
#
# Copyright (C) 2017 Allen Leis
# For license information, see LICENSE
#
# ID: filename.py [] allen.leis@gmail.com $

"""
module description
"""

##########################################################################
# Imports
##########################################################################

import logging
import logging.config

##########################################################################
# Variables
##########################################################################

ISO8601_DATETIME = "%Y-%m-%dT%H:%M:%S%z"
BASE_LOG_LEVEL = "DEBUG"

##########################################################################
## Logging configuration
##########################################################################

configuration = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple': {
            'format': '%(name)s %(process)d %(levelname)s [%(asctime)s] %(message)s',
            'datefmt': ISO8601_DATETIME,
        }
    },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },

        'console': {
            'level': BASE_LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },

        'logfile': {
            'level': BASE_LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "" or '/dev/null',
            'maxBytes': 536870912, # 512 MB
            'formatter': 'simple',
        },
    },

    'loggers': {
        'phoebe': {
            'level': BASE_LOG_LEVEL,
            'handlers': ['logfile'] if "" else ['console'],
            'propagate': True,
        },
    },
}

logging.config.dictConfigClass(configuration).configure()
# if not settings.debug: logging.captureWarnings(True)

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
