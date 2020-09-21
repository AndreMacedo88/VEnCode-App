import wx


import menus
import panels


class AppWindow(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='VEnCode App', size=(1000, 600))

        self.SetIcon(wx.Icon('resources/main_icon.ico', wx.BITMAP_TYPE_ANY))
        self.init_menu()
        self.main_panel = None
        self.init_ui()
        self.Centre()

    def init_menu(self):
        menubar = wx.MenuBar()
        menu_file = menus.FileMenu(self)
        menu_help = menus.HelpMenu()
        menubar.Append(menu_file, '&File')
        menubar.Append(menu_help, '&Help')
        self.SetMenuBar(menubar)

    def init_ui(self):
        self.main_panel = panels.PanelMain(self)


def main():
    app = wx.App(False)
    window = AppWindow()
    window.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
