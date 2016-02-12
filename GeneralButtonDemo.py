# -*- coding: gbk -*-

import wx
import wx.lib.buttons as buttons


class GenericButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Generic Button Example',
                          size=(500, 350))
        panel = wx.Panel(self, -1)

        sizer = wx.FlexGridSizer(4, 3, 20, 20)
        btn = wx.Button(panel, -1, "A wx.Button")
        btn.SetDefault()
        sizer.Add(btn)

        btn = wx.Button(panel, -1, "Non-default wx.Button")
        sizer.Add(btn)
        sizer.Add((10, 10))

        btn = buttons.GenButton(panel, -1, 'Generic Button')  # ������ͨ�ð�ť
        sizer.Add(btn)

        btn = buttons.GenButton(panel, -1, 'Disabled Generic')  # ��Ч��ͨ�ð�ť
        btn.Enable(False)
        sizer.Add(btn)

        btn = buttons.GenButton(panel, -1, 'Bigger')  # �Զ���ߴ����ɫ�İ�ť
        btn.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        btn.SetBezelWidth(5)
        btn.SetBackgroundColour("Navy")
        btn.SetForegroundColour("White")
        btn.SetToolTipString("This is a BIG button...")
        sizer.Add(btn)

        bmp = wx.Image("bitmap.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        btn = buttons.GenBitmapButton(panel, -1, bmp)  # ͨ��λͼ��ť
        sizer.Add(btn)

        btn = buttons.GenBitmapToggleButton(panel, -1, bmp)  # ͨ��λͼ���ذ�ť
        sizer.Add(btn)

        btn = buttons.GenBitmapTextButton(panel, -1, bmp, "Bitmap Text",
                                          size=(175, 75))  # λͼ�ı���ť
        btn.SetUseFocusIndicator(False)
        sizer.Add(btn)

        btn = buttons.GenToggleButton(panel, -1, "Toggle Button")  # ͨ�ÿ��ذ�ť
        sizer.Add(btn)

        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App()
    frame = GenericButtonFrame()
    frame.Show()
    app.MainLoop()
