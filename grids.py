import wx
import buttons


class GetVencodesGrid(wx.GridBagSizer):
    def __init__(self, parent, panel):
        super().__init__(0, 0)

        self.parent = parent

        st1 = wx.StaticText(panel, label='Get VEnCodes')
        self.Add(st1, pos=(0, 0), flag=wx.ALL, border=20)

        b1 = buttons.GetVencodeFantom(panel, label='Get VEnCodes from FANTOM5 data')
        b2 = buttons.GetVencodeCustom(panel, label='Get VEnCodes from custom data')
        self.Add(b1, pos=(1, 0), flag=wx.ALL, border=10)
        self.Add(b2, pos=(1, 1), flag=wx.ALL, border=10)
        self.Add(wx.StaticText(panel), pos=(2, 1))
        self.AddGrowableRow(1)
