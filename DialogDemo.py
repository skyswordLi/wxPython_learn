import wx


class XinDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Dialog Demo', size=(300, 200))
        label = wx.StaticText(self, -1, 'Do you want to leave the page?', pos=(50, 20))
        ok_btn = wx.Button(self, wx.ID_OK, 'OK', pos=(20, 60))
        ok_btn.SetDefault()
        cancel_btn = wx.Button(self, wx.ID_CANCEL, 'cancel', pos=(100, 60))
        cancel_btn.SetDefault()

if __name__ == '__main__':
    app = wx.App()
    app.MainLoop()
    dlg = XinDialog()
    result = dlg.ShowModal()
    if result == wx.ID_OK:
        print 'The OK button has been pressed'
    else:
        print 'The Cancel button has been pressed'
    dlg.Destroy()
