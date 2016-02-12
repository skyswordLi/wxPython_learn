# -*- coding: gbk -*-

import wx


class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Button Example',
                          size=(300, 100))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, "Hello", pos=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.on_click, self.button)
        self.button.SetDefault()

    def on_click(self, event):
        if self.button.GetLabel() == "Hello":
            self.button.SetLabel("Clicked")
        else:
            self.button.SetLabel("Hello")


if __name__ == '__main__':
    app = wx.App()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()
