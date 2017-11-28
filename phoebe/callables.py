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

def task1():
    logger = logging.getLogger("phoebe")
    logger.info("task1: execution at {}".format(datetime.now()))

def task2():
    logger = logging.getLogger("phoebe")
    logger.info("task2: execution at {}".format(datetime.now()))


##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
