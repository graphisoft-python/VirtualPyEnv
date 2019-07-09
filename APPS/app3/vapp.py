
from threading import *
import time
import sys

class vMain(object):
    def __init__(self):
        print "__init__"

    def RegisterInterface(self):
        def td_func():
            while self.isRun:
                print "vAppName:"+sys.vAppName
                time.sleep(3)    
        
        self.isRun=True
        self.td=Thread(target=td_func)
        print 'RegisterInterface'

    def Initialize(self):
        self.td.start()
        print 'Initialize'

    def FreeData(self):
        self.isRun=False
        #self.td.join()
        self.td=None
        print 'FreeData'
