# -*- coding: utf-8 -*-

import GSRoot
import DGLib
import sys

class vMain(object):
    def __init__(self):
        print "__init__"

    def RegisterInterface(self):
        self.pnlid=GSRoot.Guid()
        self.pnl=DGLib.Palette(
            DGLib.NativePoint(
                DGLib.NativeUnit(0),
                DGLib.NativeUnit(0)
            ),
            400,
            600,
            self.pnlid,
            DGLib.Dialog.GrowType.HVGrow
        )

        self.pnl.BeginEventProcessing()
        self.pnl.Show()
        self.pnlobs=DGLib.PanelObserver(self.pnl,sys.vExport)
        self.pnlobs.PanelResizing=self.pnl_resize
        self.pnlobs.PanelTopStatusLost=self.pnl_lost
        #self.pnl.EnableIdleEvent()
        #help(DGLib.PanelObserver)
        print 'RegisterInterface'

    def Initialize(self):
        print 'Initialize'

    def FreeData(self):
        self.pnlid=None
        self.pnl=None
        self.pnlobs=None
        print 'FreeData'

    def pnl_resize(self,ev):
        print "--pnl_resize--"
        print "H:"+str(ev.GetHorizontalChange())+",V:"+str(ev.GetVerticalChange())
        print sys.vAppName

    def pnl_lost(self,ev):
        print "--pnl_lost--"
        print sys.vAppName
