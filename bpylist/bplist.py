import os
import sys
from ctypes import *

if sys.platform == 'win32':
    bplist = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "bplist.cp37-win_amd64.pyd"))
elif sys.platform.startswith('linux'):
    bplist = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "bplist.cpython-36m-x86_64-linux-gnu.so"))
else : # mac os
    bplist = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "bplist.cpython-37m-darwin.so"))
    
def parse(buffer):
    bplist.parse(buffer)

def generate(d2) -> bytes:
    return bplist.generate(d2)