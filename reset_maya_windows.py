"""
Description: Resets maya windows to default location, handy if windows are lost when switching from screen to single screens.
"""
__author__ = "Shane Marks"

import maya.cmds as cmds
windows = cmds.lsUI (windows = True)
for window in windows:
    if window != "CommandWindow" and window != "ConsoleWindow" and window != "MayaWindow" and window != "ColorEditor":
        cmds.deleteUI(window)

cmds.windowPref("outlinerPanel1Window", topLeftCorner = (250,200), widthHeight = (700,400), maximized = False, parentMain = True) 

cmds.windowPref("hyperGraphPanel1Window", topLeftCorner = (250,200), widthHeight = (660,400), maximized = False, parentMain = True) 

cmds.windowPref("graphEditor1Window", topLeftCorner = (250,200), widthHeight = (660,400), maximized = False, parentMain = True) 

cmds.windowPref("dopeSheetPanel1Window", topLeftCorner = (250,200), widthHeight = (660,400), maximized = False, parentMain = True) 

cmds.windowPref("clipEditorPanel1Window", topLeftCorner = (250,200), widthHeight = (660,400), maximized = False, parentMain = True) 

cmds.windowPref("devicePanel1Window", topLeftCorner = (250,200), widthHeight = (524,470), maximized = False, parentMain = True) 

cmds.windowPref("hyperShadePanel1Window", topLeftCorner = (250,200), widthHeight = (700,400), maximized = False, parentMain = True) 

cmds.windowPref("dynPaintScriptedPanelWindow", topLeftCorner = (250,200), widthHeight = (700,400), maximized = False, parentMain = True) 

cmds.windowPref("blindDataEditor1Window", topLeftCorner = (250,200), widthHeight = (550,562), maximized = False, parentMain = True) 

cmds.windowPref("scriptEditorPanel1Window", topLeftCorner = (250,200), widthHeight = (475,325), maximized = False, parentMain = True) 

cmds.windowPref("polyTexturePlacementPanel1Window", topLeftCorner = (250,200), widthHeight = (475,325), maximized = False, parentMain = True) 

cmds.windowPref("MayaWindow", topLeftCorner = (0,0), widthHeight = (1280,1024), maximized = False, parentMain = True) 

cmds.windowPref("NewFeatureHighlightWnd", topLeftCorner = (497,762), widthHeight = (450,320), maximized = False, parentMain = True) 

cmds.windowPref("learningMoviesLaunchWnd", topLeftCorner = (452,1271), widthHeight = (694,595), maximized = False, parentMain = True) 

