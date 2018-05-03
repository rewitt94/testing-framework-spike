import drs
import tests
import emoji

Doc = drs.DrS()

count = 0

for x in dir(tests):
    if x[-4:] == '_drs':
        module = getattr(tests, x)
        for y in dir(module):
            if y[0:5] == 'test_':
                count = count + 1
                function = getattr(module, y)
                Doc.collect_test({ "name": f"{count}: {y}", "function": function })

Doc.run_tests()
