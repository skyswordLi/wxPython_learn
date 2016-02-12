# -*- coding: gbk -*-

import wx


class SplitterExampleFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.make_menu_bar()
        self.min_pane = 0
        self.init_pos = 0
        self.sp = wx.SplitterWindow(self)  # 创建一个分割窗
        self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)  # 创建子面板
        self.p2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p1.SetBackgroundColour("pink")
        self.p2.SetBackgroundColour("sky blue")
        self.p1.Hide()  # 确保备用的子面板被隐藏
        self.p2.Hide()

        self.sp.Initialize(self.p1)  # 初始化分割窗

        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING,
                  self.on_sash_changing, self.sp)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED,
                  self.on_sash_changed, self.sp)

    def make_menu_bar(self):
        menu = wx.Menu()
        item = menu.Append(-1, "Split horizontally")
        self.Bind(wx.EVT_MENU, self.on_split_h, item)
        item = menu.Append(-1, "Split vertically")
        self.Bind(wx.EVT_MENU, self.on_split_v, item)
        item = menu.Append(-1, "Un split")
        self.Bind(wx.EVT_MENU, self.on_un_split, item)

        menu.AppendSeparator()
        item = menu.Append(-1, "Set initial sash position")
        self.Bind(wx.EVT_MENU, self.on_set_pos, item)
        item = menu.Append(-1, "Set minimum pane size")
        self.Bind(wx.EVT_MENU, self.on_set_min, item)

        menu.AppendSeparator()
        item = menu.Append(wx.ID_EXIT, "E ")
        self.Bind(wx.EVT_MENU, self.on_exit, item)

        menu_bar = wx.MenuBar()
        menu_bar.Append(menu, "Splitter")
        self.SetMenuBar(menu_bar)

    @staticmethod
    def on_sash_changing(evt):
        print "on_sash_changing:", evt.GetSashPosition()

    @staticmethod
    def on_sash_changed(evt):
        print "on_sash_changed:", evt.GetSashPosition()

    def on_split_h(self, evt):  # 响应水平分割请求
        self.sp.SplitHorizontally(self.p1, self.p2, self.init_pos)

    def on_split_v(self, evt):  # 响应垂直分割请求
        self.sp.SplitVertically(self.p1, self.p2, self.init_pos)

    def on_un_split(self, evt):
        self.sp.Unsplit()

    def on_set_min(self, evt):
        min_pane = wx.GetNumberFromUser(
            "Enter the minimum pane size",
            "", "Minimum Pane Size", self.min_pane,
            0, 1000, self)
        if min_pane != -1:
            self.min_pane = min_pane
            self.sp.SetMinimumPaneSize(self.min_pane)

    def on_set_pos(self, evt):
        init_pos = wx.GetNumberFromUser(
            "Enter the initial sash position (to be used in the Split call)",
            "", "Initial Sash Position", self.init_pos,
            -1000, 1000, self)
        if init_pos != -1:
            self.init_pos = init_pos

    def on_exit(self, evt):
        self.Close()


if __name__ == '__main__':
    app = wx.App(redirect=True)
    frm = SplitterExampleFrame(None, "Splitter Example")
    frm.SetSize((600, 500))
    frm.Show()
    app.SetTopWindow(frm)
    app.MainLoop()
