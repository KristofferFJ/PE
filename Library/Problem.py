# Template for Project Euler problems

import time


class Problem:

    def __init__(self, number):
        self.number = number
        self.start_time = time.time()
        self.result = 0

    def run(self):
        print("Answer to problem %s is %s" % (self.number, self.result))
        print("Found in %s seconds of computing" % (time.time() - self.start_time))
