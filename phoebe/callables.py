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

from datetime import datetime

from .config import logging

##########################################################################
# Functions
##########################################################################

def task1(*args, **kwargs):
    logger = logging.getLogger("phoebe")
    logger.info("task1: execution at {}".format(datetime.now()))
    logger.info("task1: arguments: {}, {}".format(args, kwargs))

def task2(*args, **kwargs):
    logger = logging.getLogger("phoebe")
    logger.info("task2: execution at {}".format(datetime.now()))
    logger.info("task2: arguments: {}, {}".format(args, kwargs))

def task_schedule():
    logger = logging.getLogger("phoebe")
    logger.info("task_schedule: execution at {}".format(datetime.now()))
    return {
        "success": True,
        "tasks" : [
            {
                "klass": "task1",
                "args": 1,
                "kwargs": {"days": ["2017-11-28"]},
                "result": None,
                "type": "task1_schedule",
                "task_id": "999",

            }
        ]
    }


##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
