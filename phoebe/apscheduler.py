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

from .config import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from .callables import *

##########################################################################
# Classes
##########################################################################

class APSchedulerApp(object):
    """
    The phoebe application is a manager process that routinely enqueues jobs
    """

    def __init__(self):
        self.schedule = BackgroundScheduler({
            'apscheduler.executors.default': {
                # 'class': 'apscheduler.executors.pool:ProcessPoolExecutor',
                'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
                'max_workers': '4'
            },
            'apscheduler.job_defaults.coalesce': 'false',
            'apscheduler.timezone': 'UTC',
        })
        self.logger = logging.getLogger("phoebe")

    def tattle(self):
        """

        """
        self.logger.debug("Phoebe Job Schedule:")
        for item in self.schedule.get_jobs():
            self.logger.debug(item)
        # import pdb; pdb.set_trace()

    def run(self):
        """
        """
        # Start the application
        self.start()
        counter = 0

        # Run pending and handle results
        while True:
            try:
                time.sleep(1)

                counter += 1
                if counter > 15:
                    self.tattle()
                    counter = 0

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
            "starting phoebe service (apscheduler)"
        )

        self.schedule.start()

        self.schedule.add_job(task_schedule, 'interval', seconds=5)
        self.schedule.add_listener(self.result, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

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

    @staticmethod
    def result(event):
        print(event.retval)
        
        # import pdb; pdb.set_trace()

        # result = event.retval
        # if result is not None:
        #     available = globals()
        #     if result.get('success', True):
        #
        #         # if result contains items to enqueue then do so here.
        #         if 'tasks' in result:
        #             for sig in result['tasks']:
        #                 if sig['klass'] in available:
        #                     task = available[sig['klass']]
        #                     self.schedule.add_job(task)
        #
        #         self.logger.info(
        #             "{type} {taskid} completed by proc {pid}".format(**result)
        #         )
        #     else:
        #         error = result['result']
        #         error['task'] = result['type']
        #         error['taskid'] = result['taskid']
        #
        #         self.logger.error(
        #             "{task} {taskid} errored {type}: {error}".format(**error)
        #         )
##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
