# -*- coding: gbk -*-

import wx


class BitmapButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Bitmap Button Example',
                          size=(800, 600))
        panel = wx.Panel(self, -1)
        bmp = wx.Image("bitmap.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, bmp, pos=(10, 20))
        self.Bind(wx.EVT_BUTTON, self.on_click, self.button)
        self.button.SetDefault()
        self.button2 = wx.BitmapButton(panel, -1, bmp, pos=(410, 220),
                                       style=0)
        self.Bind(wx.EVT_BUTTON, self.on_click, self.button2)

    def on_click(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = BitmapButtonFrame()
    frame.Show()
    app.MainLoop()
