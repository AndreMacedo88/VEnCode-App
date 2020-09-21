import wx


class VencodeDialog(wx.Dialog):

    def __init__(self, *args, **kw):

        self.vencodes = kw.pop("vencodes")
        super(VencodeDialog, self).__init__(*args, **kw)

        self.init_dialog()
        self.SetSize((300, 200))
        self.SetTitle("VEnCodes")

    def init_dialog(self):
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(pnl, -1, 'Your VEnCodes are ready!')
        hbox.Add(text, flag=wx.ALL, border=10)
        wx.StaticLine(pnl)

        pnl.SetSizer(hbox)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        e_value_button = wx.Button(self, label='Calculate e-values')
        export_button = wx.Button(self, label='Export VEnCodes')

        hbox2.Add(e_value_button)
        hbox2.Add(export_button, flag=wx.LEFT, border=5)

        vbox.Add(pnl, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        e_value_button.Bind(wx.EVT_BUTTON, self.on_e_value)
        export_button.Bind(wx.EVT_BUTTON, self.on_export)

    def on_export(self, e):
        dlg = wx.DirDialog(self, "Please choose the directory to store the data:",
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
        else:
            path = None
        dlg.Destroy()

        if path is not None:
            if self.vencodes.e_values:
                self.vencodes.export("vencodes", "e-values", path=path)
            else:
                self.vencodes.export("vencodes", path=path)
            wx.MessageBox('VEnCodes exported successfully', 'Info',
                          wx.OK | wx.ICON_INFORMATION)
        else:
            self.Destroy()

    def on_e_value(self, e):
        msg = "Computing, please wait..."
        busyDlg = wx.BusyInfo(msg)
        self.vencodes.determine_e_values()
        busyDlg = None
        wx.MessageBox('e-values calculated!', 'Info',
                      wx.OK | wx.ICON_INFORMATION)
