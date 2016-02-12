# -*- coding: cp936 -*-

import wx


class QinFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, '琴儿', size=(450, 260))

        panel = wx.Panel(self, -1)
        self.ok_button = wx.Button(panel, -1, '完成', pos=(80, 160), size=(130, 40))
        self.clear_button = wx.Button(panel, -1, '清空', pos=(230, 160), size=(130, 40))
        self.Bind(wx.EVT_BUTTON, self.OkButtonClick, self.ok_button)
        self.Bind(wx.EVT_BUTTON, self.ClearButtonClick, self.clear_button)

        user = wx.StaticText(panel, -1, '账户', (50, 50), (160, 20),
                             wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        user.SetBackgroundColour('pink')
        user.SetForegroundColour('black')
        user.SetFont(wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        user_input = wx.TextCtrl(panel, -1, '请输入账户:', (230, 50), (160, 32))
        user_input.SetInsertionPoint(0)
        user_input.SetFont(wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        password = wx.StaticText(panel, -1, '密码', (50, 100), (160, 20),
                                 wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        password.SetBackgroundColour('pink')
        password.SetForegroundColour('black')
        password.SetFont(wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        password_input = wx.TextCtrl(panel, -1, '请输入密码:', (230, 100), (160, 32), style=wx.TE_PASSWORD )
        password_input.SetInsertionPoint(0)
        password_input.SetFont(wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    @staticmethod
    def OkButtonClick(self):
        print 'Stored'

    @staticmethod
    def ClearButtonClick(self):
        print 'Text Cleared'
        self.user.SetValue('')

    """
    def OnInit(self):
        self.frame = wx.Frame(parent=None, title='Qin\'er', pos=(-1, -1), size=(800, 600))
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    """


app = wx.App()
frame = QinFrame()
frame.Show()
app.MainLoop()
