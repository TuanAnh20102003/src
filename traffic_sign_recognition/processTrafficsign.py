# processBienBao.py

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../..")

from src.templates.workerprocess import WorkerProcess
from src.traffic_sign_recognition.thread.threadTrafficsign import threadTrafficSign
from multiprocessing import Pipe
class processTrafficSign(WorkerProcess):
    def __init__(self, queueList, logger, debugging=False):
        self.logger = logger
        self.debugging = debugging
        super(processTrafficSign, self).__init__(queueList)

    def run(self):
        super(processTrafficSign, self).run()

    def _init_threads(self):
        threadTrafficsign = threadTrafficsign(
            self.queuesList, self.logger, self.debugging
        )
        self.threads.append(threadTrafficsign)


# ======== Only runs when you call this script directly ========
if __name__ == "__main__":
    from multiprocessing import Queue
    import time
    import logging

    queueList = {
        "Critical": Queue(),
        "Warning": Queue(),
        "General": Queue(),
        "Config": Queue(),
    }

    logging = logging.getLogger()
    process = processTrafficSign(queueList, logging, debugging=True)
    process.daemon = True
    process.start()

    time.sleep(10)  # let it run for a while
    process.stop()

