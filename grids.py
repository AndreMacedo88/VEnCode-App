import wx
import buttons


class GetVencodesGrid(wx.GridBagSizer):
    def __init__(self, parent, panel):
        super().__init__(0, 0)

        self.parent = parent

        image_pre = wx.Bitmap("resources/dna-strings.jpg").ConvertToImage()
        image_pre = image_pre.Scale(430, 215, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(image_pre)
        image_final = wx.StaticBitmap(panel, wx.ID_ANY, bitmap)
        self.Add(image_final, pos=(0, 0), span=(1, 2))

        b1 = buttons.GetVencodeFantom(panel, label='Get VEnCodes from FANTOM5 data')
        b2 = buttons.GetVencodeCustom(panel, label='Get VEnCodes from custom data')
        self.Add(b1, pos=(1, 0), span=(2, 1), flag=wx.EXPAND)
        self.Add(b2, pos=(1, 1), span=(2, 1), flag=wx.EXPAND)

