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

from phoebe import ScheduleApp, APSchedulerApp

##########################################################################
# Classes
##########################################################################

def test_schedule():
    app = ScheduleApp()
    app.run()

def test_apscheduler():
    app = APSchedulerApp()
    app.run()

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    test_apscheduler()
