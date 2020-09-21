import wx
import panels
import algorithms
import dialogs


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
        msg = "Computing, please wait..."
        busyDlg = wx.BusyInfo(msg)
        vencodes = algorithms.GetVencodes(data_type=self.Parent.data_type, algorithm=self.Parent.algorithm,
                                          cell_type=self.Parent.cell_type, k=self.Parent.sc_k.GetValue(),
                                          number_vencodes=self.Parent.sc_number_ven.GetValue())
        busyDlg = None

        cdDialog = dialogs.VencodeDialog(None, vencodes=vencodes.vencodes, title='Your VEnCodes')
        cdDialog.ShowModal()
        cdDialog.Destroy()


class BackToMain(wx.Button):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, e):
        self.Parent.Parent.main_panel.Show()
        self.Parent.Destroy()
