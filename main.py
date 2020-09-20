import wx
import menus
import grids
import binds


class AppWindow(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='VEnCode App', size=(1000, 600))

        self.init_menu()
        self.init_ui()
        self.Centre()

    def init_menu(self):
        menubar = wx.MenuBar()
        menu_file = menus.FileMenu(self)
        menubar.Append(menu_file, '&File')
        self.SetMenuBar(menubar)

    def init_ui(self):
        # Create outer Panel
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')
        binds.PanelBinds(self, panel)
        panel.SetFocus()
        # Create a sizer inside the panel to fill with stuff
        sizer_main = wx.GridBagSizer(0, 0)
        # Create another panel, this time to put boxes/grids (sizers) inside the outer panel and sizer
        panel_mid = wx.Panel(panel)
        panel_mid.SetBackgroundColour('#ededed')
        binds.PanelBinds(self, panel_mid)
        # Create section to click to get VEnCodes
        sizer_mid = grids.GetVencodesGrid(self, panel_mid)
        panel_mid.SetSizer(sizer_mid)
        # Add the middle panel to the outer sizer and set the outer sizer as the main outer panel sizer
        sizer_main.Add(panel_mid, pos=(0, 0), flag=wx.ALL, border=20)
        panel.SetSizer(sizer_main)

    # def on_right_down(self, e):
    #     self.PopupMenu(menus.MainPopupMenu(self), e.GetPosition())
    #
    # def OnKeyDown(self, e):
    #
    #     key = e.GetKeyCode()
    #
    #     if key == wx.WXK_ESCAPE:
    #
    #         ret = wx.MessageBox('Are you sure to quit?', 'Question',
    #                             wx.YES_NO | wx.NO_DEFAULT, self)
    #
    #         if ret == wx.YES:
    #             self.Close()


def main():
    app = wx.App(False)
    window = AppWindow()
    window.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
