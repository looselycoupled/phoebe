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

from config import logging
from datetime import datetime
import time

import schedule

##########################################################################
# Classes
##########################################################################

def task():
    logger = logging.getLogger("phoebe")
    logger.info("task: execution at {}".format(datetime.now()))


class PhoebeApp(object):
    """
    The phoebe application is a manager process that routinely enqueues jobs
    """

    def __init__(self):
        self.schedule = schedule.Scheduler()
        self.logger = logging.getLogger("phoebe")

    def run(self):
        """
        """
        # Start the application
        self.start()

        # Run pending and handle results
        while True:
            try:
                self.schedule.run_pending()
                time.sleep(1)
            except (KeyboardInterrupt, SystemExit):
                return self.shutdown()
            except Exception as e:
                return self.terminate(str(e))

    def start(self):
        """
        Called once on startup from the ``run()`` method, this function
        starts all processes and schedules requested routines.
        """
        # Log the startup
        self.logger.info(
            "starting phoebe service"
        )

        # self.schedule.every().minute.do(task)
        self.schedule.every().monday.at("11:38").do(task)

    def shutdown(self):
        """
        Called on graceful shutdown to clean up and close processes and
        cancel any running tasks that haven't completed yet.
        """
        # Log the shutdown
        self.logger.info("graceful shutdown of phoebe insight service")

    def terminate(self, error):
        """
        Called to hard terminate the phoebe service, stopping before any
        queued jobs have a chance to complete and exiting with an error.
        """
        self.logger.critical(error)
        self.logger.critical("hard termination of phoebe insight service")



##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    app = PhoebeApp()
    app.run()
