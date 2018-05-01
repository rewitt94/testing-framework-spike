import os
import drs
import tests

Doc = drs.DrS()

for x in dir(tests):
    if x[-5:] == '_test':
        module = getattr(tests, x)
        for y in dir(module):
            if y[0:5] == 'test_':
                function = getattr(module, y)
                Doc.collect_test(function)

Doc.run_tests()
