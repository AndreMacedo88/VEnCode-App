import wx


class GetVencodeFantom(wx.Button):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, e):
        print('Get Fantom5')


class GetVencodeCustom(wx.Button):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, e):
        print('Get Custom')
