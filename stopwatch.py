import time

class stopwatch:
    def __init__(self,) -> None:
        self.startTime=time.time()
    def elapsed(self):
        endTime=time.time()
        return endTime-self.startTime