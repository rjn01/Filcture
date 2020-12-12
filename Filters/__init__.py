'''import os

__all__ = []

for i in os.listdir('./Filters'):
  a = i.split('.')
  print(a)
  if a[1] == 'py':
    __all__.append(a[0])
  
'''
import os
from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname('./Filcture/Filters'), "*.py"))
m = os.listdir('./Filters')

__all__ = [ f[:-3] for f in m if isfile(f) and not f.endswith('__init__.py')]
print(__all__)
