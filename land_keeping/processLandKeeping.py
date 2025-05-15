if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../../..")
from src.templates.workerprocess import WorkerProcess
from src.land_keeping.thread.threadLandKeeping import ThreadLandKeeping 
from multiprocessing import Pipe

class processLandKeeping(WorkerProcess):
    """This process handles land keeping (lane detection and steering control)."""
    
    def __init__(self, queueList, logging, debugging=False):
        """Initialize the land keeping process."""
        self.queuesList = queueList
        self.logging = logging
        self.debugging = debugging
        super(processLandKeeping, self).__init__(self.queuesList)
    
    def run(self):
        """Start the land keeping process (thread)."""
        super(processLandKeeping, self).run()

    def _init_threads(self):
        """Initialize the land keeping thread and add it to the list of threads."""
        # Khoi tao thread xu lý gi làn (land keeping)
        LandKeepingThread = ThreadLandKeeping(self.queuesList, self.logging, self.debugging)
        self.threads.append(LandKeepingThread)
