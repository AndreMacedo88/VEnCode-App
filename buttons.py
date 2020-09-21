import wx
import panels


class GetVencodeFantom(wx.Button):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, e):
        self.Parent.Parent.Hide()
        panels.PanelVencodeSettings(self.Parent.Parent.Parent)


class GetVencodeCustom(wx.Button):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, e):
        print('Get Custom')


class ComputeVencode(wx.Button):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, e):
        print(self.Parent.data_type, self.Parent.cell_type, self.Parent.sc.GetValue(), self.Parent.sc_2.GetValue())


class BackToMain(wx.Button):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, e):
        self.Parent.Parent.main_panel.Show()
        self.Parent.Destroy()
