# -*- coding: gbk -*-
from __future__ import division
import math
import wx


class PosValidator(wx.PyValidator):  # 创建坐标输入验证器
    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        """
         Note that every validator must implement the Clone() method.
         """
        return PosValidator()

    def Validate(self, win):
        text_ctrl = self.GetWindow()
        text = text_ctrl.GetValue()

        if len(text) == 0:
            wx.MessageBox("必须同时输入经度和纬度值!", "错误")
            text_ctrl.SetBackgroundColour("pink")
            text_ctrl.SetFocus()
            text_ctrl.Refresh()
            return False
        else:
            try:
                float(text)
                text_ctrl.SetBackgroundColour(
                    wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                text_ctrl.Refresh()
                return True
            except:
                wx.MessageBox("输入的数字含非法字符，必须是正确的数值", "错误")
                return False
        return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True


class PosConverter:
    def __init__(self):
        self.inputs = []

    def add_input(self, text_ctrl):
        self.inputs.append(text_ctrl)

    def get_input(self, i):
        return self.inputs[i]

    def get_input_value(self, i):
        return str(self.inputs[i].GetValue())

    def set_result_value(self, i, value):
        self.inputs[i].SetValue(str(value))

    def lat_lon_convert(self, source, destination, input_index, output_index):
        if source == destination:
            self.set_result_value(output_index, self.get_input_value(input_index))
        else:
            lat_lon_value = float(self.get_input_value(input_index))
            if source == 'sc_type: int':
                if destination == 's_type: float':
                    lat_lon = self.sc_pos_2_s_pos(lat_lon_value)
                elif destination == 'type: double':
                    lat_lon = self.sc_pos_2_pos(lat_lon_value)
            elif source == 's_type: float':
                if destination == 'sc_type: int':
                    lat_lon = int(self.s_pos_2_sc_pos(lat_lon_value))
                elif destination == 'type: double':
                    lat_lon = self.s_pos_2_pos(lat_lon_value)
            elif source == 'type: double':
                if destination == 'sc_type: int':
                    lat_lon = int(self.pos_2_sc_pos(lat_lon_value))
                elif destination == 's_type: float':
                    lat_lon = self.pos_2_s_pos(lat_lon_value)
            self.set_result_value(output_index, lat_lon)

    def lat_convert(self, source, destination):
        self.lat_lon_convert(source, destination, 0, 2)

    def lon_convert(self, source, destination):
        self.lat_lon_convert(source, destination, 1, 3)

    @staticmethod
    def sc_pos_2_s_pos(sc_pos):
        return sc_pos / pow(2, 31) * 180

    @staticmethod
    def sc_pos_2_pos(sc_pos):
        return sc_pos / pow(2, 31) * math.pi

    @staticmethod
    def s_pos_2_sc_pos(s_pos):
        return s_pos / 180 * pow(2, 31)

    @staticmethod
    def s_pos_2_pos(s_pos):
        return s_pos / 180 * math.pi

    @staticmethod
    def pos_2_sc_pos(pos):
        return pos / math.pi * pow(2, 31)

    @staticmethod
    def pos_2_s_pos(pos):
        return pos / math.pi * 180


class PosTransDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "坐标转换", size=(450, 300))
        self.pos_converter = PosConverter()

        panel = wx.Panel(self, -1)
        position_type_list = ['sc_type: int', 's_type: float', 'type: double']
        self.original_radio = wx.RadioBox(panel, -1, "选择源坐标类型", (10, 1), wx.DefaultSize,
                                          position_type_list, 2, wx.RA_SPECIFY_COLS)
        self.target_radio = wx.RadioBox(panel, -1, "选择目标坐标类型", (230, 1), wx.DefaultSize,
                                        position_type_list, 2, wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.on_radio_box, self.original_radio)
        self.Bind(wx.EVT_RADIOBOX, self.on_radio_box, self.target_radio)

        wx.StaticText(panel, -1, "输入原坐标:", pos=(20, 100))
        wx.StaticText(panel, -1, "纬度:", pos=(30, 130))
        wx.StaticText(panel, -1, "经度:", pos=(30, 170))
        original_lat_input = wx.TextCtrl(panel, pos=(70, 130), validator=PosValidator())
        original_lon_input = wx.TextCtrl(panel, pos=(70, 170), validator=PosValidator())
        original_lat_input.SetInsertionPoint(0)
        original_lon_input.SetInsertionPoint(0)
        self.Bind(wx.EVT_TEXT, self.on_input_position, original_lat_input)
        self.Bind(wx.EVT_TEXT, self.on_input_position, original_lon_input)

        wx.StaticText(panel, -1, "输出目标坐标:", pos=(240, 100))
        wx.StaticText(panel, -1, "纬度:", pos=(250, 130))
        wx.StaticText(panel, -1, "经度:", pos=(250, 170))
        target_lat_input = wx.TextCtrl(panel, pos=(290, 130))
        target_lon_input = wx.TextCtrl(panel, pos=(290, 170))
        target_lat_input.SetInsertionPoint(0)
        target_lon_input.SetInsertionPoint(0)

        self.pos_converter.add_input(original_lat_input)
        self.pos_converter.add_input(original_lon_input)
        self.pos_converter.add_input(target_lat_input)
        self.pos_converter.add_input(target_lon_input)

        trans = wx.Button(panel, label="转换", pos=(80, 220), size=(125, 30))
        trans.SetDefault()
        panel.Bind(wx.EVT_BUTTON, self.on_trans, trans)
        clean = wx.Button(panel, label="清空", pos=(240, 220), size=(125, 30))
        panel.Bind(wx.EVT_BUTTON, self.on_clean, clean)

    def on_trans(self, event):
        if self.pos_converter.get_input(0).GetValidator().Validate(self.pos_converter.get_input(0)) and \
                self.pos_converter.get_input(1).GetValidator().Validate(self.pos_converter.get_input(1)):
            self.do_convert(self.pos_converter)

    def on_clean(self, event):
        for item in self.pos_converter.inputs:
            if item.GetValue() != '':
                item.Clear()

    def on_radio_box(self, event):
        self.react_to_input_or_radio()

    def on_input_position(self, event):
        self.react_to_input_or_radio()

    def react_to_input_or_radio(self):
        if self.pos_converter.get_input(0).GetValue() != '':
            self.do_lat_convert(self.pos_converter)
        if self.pos_converter.get_input(1).GetValue() != '':
            self.do_lon_convert(self.pos_converter)

    def do_lat_convert(self, converter):
        original_select = self.get_select_items()[0]
        target_select = self.get_select_items()[1]
        converter.lat_convert(original_select, target_select)

    def do_lon_convert(self, converter):
        original_select = self.get_select_items()[0]
        target_select = self.get_select_items()[1]
        converter.lon_convert(original_select, target_select)

    def get_select_items(self):
        return [self.original_radio.GetStringSelection().encode('ascii', 'ignore'),
                self.target_radio.GetStringSelection().encode('ascii', 'ignore')]

if __name__ == "__main__":
    app = wx.App()
    dlg = PosTransDialog()
    dlg.ShowModal()
    dlg.Destroy()
    app.MainLoop()
