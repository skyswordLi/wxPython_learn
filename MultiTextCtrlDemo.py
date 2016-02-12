# -*- coding: gbk -*-

import wx


class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',
                          size=(300, 250))
        panel = wx.Panel(self, -1)
        multi_label = wx.StaticText(panel, -1, "Multi-line")
        multi_text = wx.TextCtrl(panel, -1,
                                 "Here is a looooooooooooooong line of text set in the control.\n\n"
                                 "See that it wrapped, and that this line is after a blank",
                                 size=(200, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)  # ����һ���ı��ؼ�
        multi_text.SetInsertionPoint(0)  # ���ò����

        rich_label = wx.StaticText(panel, -1, "Rich Text")
        rich_text = wx.TextCtrl(panel, -1,
                                "If supported by the native control, this is reversed, and this is a different font.\
                                http://www.baidu.com",
                                size=(200, 100), style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_AUTO_URL)  # �����ḻ�ı��ؼ�
        rich_text.SetInsertionPoint(0)
        rich_text.SetStyle(44, 52, wx.TextAttr("red", "black"))  # �����ı���ʽ
        points = rich_text.GetFont().GetPointSize()
        f = wx.Font(points + 3, wx.SCRIPT, wx.ITALIC, wx.BOLD, True)  # ����һ������
        rich_text.SetStyle(68, 82, wx.TextAttr("blue", wx.NullColour, f))  # ��������������ʽ
        rich_text.SetStyle(83, 102, wx.TextAttr("red", wx.NullColour, f))

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multi_label, multi_text, rich_label, rich_text])
        panel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()
