import os
import drs

# def remove_file_extention(file_name):
#     return file_name[0:-3]

Doc = drs.DrS()

def add_directory_to_path(file_name):
    return './tests/' + file_name

__all__ = os.listdir('./tests');
# __all__ = list(map(remove_file_extention, __all__))
__all__ = list(map(add_directory_to_path, __all__))

print(__all__)

for x in __all__:
    file = open(x, 'r')
    exec(file.read())

Doc.run_tests()
