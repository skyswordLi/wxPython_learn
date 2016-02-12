import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Grid Demo')
        sizer = wx.GridSizer(rows=2, cols=2, hgap=20, vgap=20)
        label = ['c', 'java', 'php', 'ruby']
        style = {'c': wx.ALIGN_CENTER, 'java': wx.ALIGN_BOTTOM,
                 'php': wx.ALIGN_LEFT, 'ruby': wx.EXPAND}
        for item in label:
            bt = wx.Button(self, -1, item)
            flag = style.get(item, 0)
            sizer.Add(bt, 0, flag)
        self.SetSizer(sizer)
        self.Fit()

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
