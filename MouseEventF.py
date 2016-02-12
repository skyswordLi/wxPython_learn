import wx


class MouseEventFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Frame with Button', size=(300, 100))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label='Not Over', pos=(100, 15))
        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.on_enter_window)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave_window)

    def on_button_click(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()

    def on_enter_window(self, event):
        self.button.SetLabel('Over Me!')
        event.Skip()

    def on_leave_window(self, event):
        self.button.SetLabel('Not Over Me!')
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = MouseEventFrame()
    frame.Show()
    app.MainLoop()
