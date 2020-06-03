# -*- coding: utf-8 -*-

import GSRoot
import DGLib
import Graphix
import sys

class vMain(object):
    def __init__(self):
        print "__init__"

    def RegisterInterface(self):
        self.pnlid=GSRoot.Guid()
        self.pnl=DGLib.Palette(
            GSRoot.Point(
                0,
                0
            ),
            600,
            800,
            self.pnlid,
            DGLib.Dialog.GrowType.HVGrow
        )

        self.pnl.BeginEventProcessing()
        self.pnl.Show()

        pic=DGLib.Icon("./c.jpg")
        self.img=DGLib.IconItem(
            self.pnl,
            GSRoot.Rect(
                GSRoot.Point(4,4),
                414,
                122
            )
        )
        self.img.SetIcon(pic)
        self.img.Show()
        

        self.pnlobs=DGLib.PanelObserver(self.pnl)
        self.pnlobs.PanelResizing=self.pnl_resize
        self.pnlobs.PanelTopStatusLost=self.pnl_lost
        self.pnl.SetTitle(u"python图片测试")
        #self.pnl.EnableIdleEvent()
        #help(DGLib.PanelObserver)
        print 'RegisterInterface'

    def Initialize(self):
        print 'Initialize'

    def FreeData(self):
        print 'FreeData'

    def pnl_resize(self,ev):
        print "--pnl_resize--"
        print "H:"+str(ev.GetHorizontalChange())+",V:"+str(ev.GetVerticalChange())
        print sys.vAppInfo.GetName()

    def pnl_lost(self,ev):
        print "--pnl_lost--"
        print sys.vAppInfo.GetName()

    def ToolsContextMenuRequested(self,ev):
        print ev.Invoke([u"L1888823",u"-","K456789",u"M789"])
