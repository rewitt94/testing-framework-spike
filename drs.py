import sys
import os
import traceback
from termcolor import colored

class DrS:
    def __init__(self):
        self.tests = []

    def collect_test(self, test):
        self.tests.append(test)

    def run_tests(self):
        for x in self.tests:
            try:
                print(colored('PASSED','green')) if x()['result'] else print(colored(f"FAILED: {x()['reason']}", 'red'))
            except BaseException as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print(colored(f"{e}",'green'))
                print(traceback.format_list(traceback.extract_tb(exc_tb))[-1])
