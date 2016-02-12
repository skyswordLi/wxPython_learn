# -*- coding: gbk -*-

import wx


class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',
                          size=(300, 100))

        panel = wx.Panel(self, -1)
        basic_label = wx.StaticText(panel, -1, "Basic Control:")
        basic_text = wx.TextCtrl(panel, -1, "I've entered some text!",
                                 size=(175, -1), style=wx.TE_READONLY)
        basic_text.SetInsertionPoint(0)

        pwd_label = wx.StaticText(panel, -1, "Password:")
        pwd_text = wx.TextCtrl(panel, -1, "password", size=(175, -1),
                               style=wx.TE_PASSWORD)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([basic_label, basic_text, pwd_label, pwd_text])
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()
