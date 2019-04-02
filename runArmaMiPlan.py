import wx
from ArmaMiPlan import *

class MainApp(wx.App):
        def OnInit(self):
                mainFrame = MyFrame1(None)
                mainFrame.Show(True)
                return True

if __name__ == '__main__':
        app = MainApp()
        app.MainLoop()
