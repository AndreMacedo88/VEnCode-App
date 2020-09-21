import wx

from VEnCode import common_variables as cv

import grids
import binds
import helpers
import buttons


class PanelMain(wx.Panel):
    """ Main App panel """

    def __init__(self, parent):
        # Create outer Panel
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundColour('#4f5049')
        binds.PanelBinds(parent, self)
        self.SetFocus()
        # Create a sizer inside the panel to fill with stuff
        sizer_main = wx.GridBagSizer(0, 0)
        # Create another panel, this time to put boxes/grids (sizers) inside the outer panel and sizer
        panel_mid = wx.Panel(self)
        panel_mid.SetBackgroundColour('#ededed')
        binds.PanelBinds(parent, panel_mid)
        # Create section to click to get VEnCodes
        sizer_mid = grids.GetVencodesGrid(parent, panel_mid)
        panel_mid.SetSizer(sizer_mid)
        helpers.panel_normal_layout(panel_mid)
        # Add the middle panel to the outer sizer and set the outer sizer as the main outer panel sizer
        sizer_main.Add(panel_mid, pos=(0, 0), flag=wx.ALL, border=20)
        self.SetSizer(sizer_main)
        helpers.panel_normal_layout(self)


class PanelVencodeSettings(wx.Panel):
    """ Panel for getting VEnCodes from FANTOM5 """

    def __init__(self, parent):
        # Create outer Panel
        wx.Panel.__init__(self, parent=parent)
        binds.PanelBinds(parent, self)
        self.SetFocus()

        # Create variables
        list_re = ("Promoters", "Enhancers")
        cell_types = cv.primary_cell_list

        self.data_type = list_re[0].lower()
        self.cell_type = cell_types[0]
        self.n = None
        self.k = None

        # Create main grid
        sizer_main = wx.GridBagSizer(10, 10)

        # Choose between VEnCodes made of promoters or enhancers
        self.rbx = wx.RadioBox(self, label='Type of regulatory element', choices=list_re,
                               majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.rbx.Bind(wx.EVT_RADIOBOX, self.on_radio_box)
        sizer_main.Add(self.rbx, pos=(0, 0), span=(3, 1), flag=wx.TOP | wx.LEFT, border=30)

        # Choose cell type to get VEnCodes
        sbx1 = wx.StaticBox(self, label='Cell type to get VEnCode')
        sizer_box = wx.StaticBoxSizer(sbx1, wx.VERTICAL)
        cb = wx.ComboBox(self, choices=cell_types, value=cell_types[0], style=wx.CB_READONLY)
        cb.Bind(wx.EVT_COMBOBOX, self.on_combo_box)
        sizer_box.Add(cb, 0, flag=wx.EXPAND)
        sizer_box_main = wx.BoxSizer()
        sizer_box_main.Add(sizer_box, 1, wx.EXPAND)
        sizer_main.Add(sizer_box_main, pos=(0, 1), span=(1, 2), flag=wx.TOP | wx.RIGHT, border=30)

        # Choose the number of VEnCodes
        sbx2 = wx.StaticBox(self, label='Number of VEnCodes')
        sizer_box_2 = wx.StaticBoxSizer(sbx2, wx.VERTICAL)
        self.sc = wx.SpinCtrl(self, value='1')
        self.sc.SetRange(1, 1000)
        sizer_box_2.Add(self.sc, 0, flag=wx.EXPAND)
        sizer_box_main_2 = wx.BoxSizer()
        sizer_box_main_2.Add(sizer_box_2, 1, wx.EXPAND)
        sizer_main.Add(sizer_box_main_2, pos=(1, 1), flag=wx.RIGHT, border=30)

        # Choose k
        sbx3 = wx.StaticBox(self, label='Number of VEnCodes')
        sizer_box_3 = wx.StaticBoxSizer(sbx3, wx.VERTICAL)
        self.sc_2 = wx.SpinCtrl(self, value='4')
        self.sc_2.SetRange(1, 15)
        sizer_box_3.Add(self.sc_2, 0, flag=wx.EXPAND)
        sizer_box_main_3 = wx.BoxSizer()
        sizer_box_main_3.Add(sizer_box_3, 1, wx.EXPAND)
        sizer_main.Add(sizer_box_main_3, pos=(1, 2), flag=wx.RIGHT, border=30)

        # Add Get VEnCodes button
        button_compute = buttons.ComputeVencode(self, label='Find VEnCodes')
        button_compute.SetFocus()
        sizer_main.Add(button_compute, pos=(3, 0), flag=wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT, border=30)

        # Add Back button
        button_back = buttons.BackToMain(self, label='Back')
        sizer_main.Add(button_back, pos=(3, 2), flag=wx.ALIGN_CENTER | wx.BOTTOM | wx.RIGHT, border=30)

        # Add the main grid to the panel
        self.SetSizer(sizer_main)
        helpers.panel_normal_layout(self)

    def on_radio_box(self, e):
        self.data_type = self.rbx.GetStringSelection().lower()

    def on_combo_box(self, e):
        self.cell_type = e.GetString()
