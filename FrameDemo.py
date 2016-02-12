# -*- coding: gbk -*-

import wx


class ShapedFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Shaped Window", style=wx.FRAME_SHAPED)
        self.hasShape = False
        self.delta = wx.Point(0, 0)
        self.bmp = wx.Image(r'.\bitmap.bmp').ConvertToBitmap()
        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)
        self.set_window_shape()
        self.Bind(wx.EVT_LEFT_DCLICK, self.on_double_click)

        # 1 新事件
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)

        self.Bind(wx.EVT_RIGHT_UP, self.on_exit)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def set_window_shape(self, evt=None):
        r = wx.RegionFromBitmap(self.bmp)
        self.hasShape = self.SetShape(r)

    def on_double_click(self, evt):
        if self.hasShape:
            self.SetShape(wx.Region())
            self.hasShape = False
        else:
            self.set_window_shape()

    def on_paint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)

    def on_exit(self, evt):
        self.Close()

    def on_left_down(self, evt):  # 2 鼠标按下
        self.CaptureMouse()
        pos = self.ClientToScreen(evt.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)

    def on_mouse_move(self, evt):  # 3 鼠标移动
        if evt.Dragging() and evt.LeftIsDown():
            pos = self.ClientToScreen(evt.GetPosition())
            new_pos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(new_pos)

    def on_left_up(self, evt):  # 4 鼠标释放
        if self.HasCapture():
            self.ReleaseMouse()


if __name__ == '__main__':
    app = wx.App()
    frame = ShapedFrame()
    frame.Show()
    app.MainLoop()
