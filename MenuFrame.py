import wx


class MenuEventFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Menus', size=(300, 200))
        menu_bar = wx.MenuBar()
        menu = wx.Menu()
        menu_item = menu.Append(-1, "&Exit...")
        menu_bar.Append(menu, "&File...")
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.on_close_me, menu_item)

    def on_close_me(self, event):
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frame = MenuEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
