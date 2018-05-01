import sys
import os
import traceback

class DrS:
    def __init__(self):
        self.tests = []

    def collect_test(self, test):
        self.tests.append(test)

    def run_tests(self):
        for x in self.tests:
            try:
                print('PASSED') if x() else print('FAILED')
            except BaseException as e:
                tb = sys.last_traceback()
                print(tb)
                # info = sys.exc_info()
                # exc_type, exc_obj, exc_tb = sys.exc_info()
                # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                # print(f"{e} at: {fname} {exc_tb.tb_lineno}")
                # print(f"{info[1]} at: line {info[2].tb_lineno} - {os.path.split(info[2].tb_frame.f_code.co_filename)[1]} ")
