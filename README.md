# VirtualPyEnv

## About

VirtualPyEnv is a plugin for the Python runtime environment in ARCHICAD. VirtualPyEnv uses a multi-interpreter working mode to provide a relatively independent python runtime environment for each vapp (virtual application) of the APPS directory project.

## Supported

* Archciad 22 (Windows)

## Install

* [youtube video](https://www.youtube.com/watch?v=A6ZU1-Rs7Hg)

## Environment Variable

* sys.vAppInfo -> APPInfo

## Internal Module

### ContextMenu

* [Menu](./docs/ContextMenu/Menu.md)
* [MenuItem](./docs/ContextMenu/MenuItem.md)
* [MenuSeparatorItem](./docs/ContextMenu/MenuSeparatorItem.md)
* [MenuPopupItem](./docs/ContextMenu/MenuPopupItem.md)
* [MenuSimpleItemBase](./docs/ContextMenu/MenuSimpleItemBase.md)
* [MenuSimpleItem](./docs/ContextMenu/MenuSimpleItem.md)
* [ToolsContextMenuRequestedEvent](./docs/ContextMenu/ToolsContextMenuRequestedEvent.md)

#### StaticMethods
```
ContextMenu.Invoke(Menu,DGLib.Point) -> unicode
```

### iTerm

* [Logger](./docs/Logger.md)
* [APPInfo](./docs/APPInfo.md)

### ACAPI

* [NotifyEventID](./docs/ACAPI/NotifyEventID.md)


## vMain
```python
import ACAPI
import ContextMenu
class vMain(object):
    def __init__(self):
        # single notifyProject mask set
        # self.notifyProjectMask=ACAPI.NotifyEventID.Open
        # mulite notifyProject mask set
        # self.notifyProjectMask=ACAPI.NotifyEventID.Open|ACAPI.NotifyEventID.Close
        pass

    # AC tools context menu request
    # def ToolsContextMenuRequested(self,ev):
    #     print ev.Invoke([u"L1888823",u"-","K456789",u"M789"]) 

    # AC Plugin hook
    # def RegisterInterface(self):
    #     pass

    # AC Plugin hook
    # def Initialize(self):
    #     pass

    # AC Plugin hook
    # def FreeData(self):
    #     pass

    # AC notify project event hook
    # def OnNotifyProjectEvent(self,notifId):
    #     if notifId == ACAPI.NotifyEventID.Open:
    #         pass
    #     pass

```

## Feature

[x] python 2.7 env

[x] multi-thread

[x] reboot vapp(virtual application)

[x] tools context menu

[x] auto install python2.7 runtime

[ ] auto install requirements

[ ] auto update vapp(virtual application)

[ ] vapp(virtual application) market

## Directories

* `ACLibs`:Archicad Python APIs
* `APPS`:vapp(virtual application) install dirs
* `Env`:python2.7 installer 

## Group

* [graphisoft-python](https://github.com/graphisoft-python)


## Archicad Modules

* [GSRoot](https://github.com/graphisoft-python/GSRoot)
* [DGLib](https://github.com/graphisoft-python/DGLib)
* [Graphix](https://github.com/graphisoft-python/Graphix)
* [ACTextEngine](https://github.com/graphisoft-python/ACTextEngine)
* [ACDGGraphix](https://github.com/graphisoft-python/ACDGGraphix)
* [ACEnvironment](https://github.com/graphisoft-python/ACEnvironment)

## Archicad Export

* [ACExport](https://github.com/graphisoft-python/ACExport)
