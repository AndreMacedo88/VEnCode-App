import wx
import wx.adv
import helpers
import VEnCode


class FileMenu(wx.Menu):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.Append(wx.ID_NEW, '&New')
        self.Append(wx.ID_OPEN, '&Open')
        self.Append(wx.ID_SAVE, '&Save')
        self.AppendSeparator()
        self.Append(wx.ID_EXIT, '&Quit', 'Quit application')

        self.Bind(wx.EVT_MENU, self.on_quit, id=wx.ID_EXIT)

    def on_quit(self, e):
        helpers.question_exit_safely(self.parent)


class MainPopupMenu(wx.Menu):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        minimize = wx.MenuItem(self, wx.ID_ANY, 'Minimize')
        self.Append(minimize)
        self.Bind(wx.EVT_MENU, self.on_minimize, minimize)

        maximize = wx.MenuItem(self, wx.ID_ANY, 'Maximize')
        self.Append(maximize)
        self.Bind(wx.EVT_MENU, self.on_maximize, maximize)

        close = wx.MenuItem(self, wx.ID_ANY, 'Close')
        self.Append(close)
        self.Bind(wx.EVT_MENU, self.on_close, close)

    def on_minimize(self, e):
        self.parent.Iconize()

    def on_maximize(self, e):
        self.parent.Maximize()

    def on_close(self, e):
        helpers.question_exit_safely(self.parent)


class HelpMenu(wx.Menu):
    def __init__(self):
        super().__init__()

        self.Append(wx.ID_ANY, '&About')
        self.Bind(wx.EVT_MENU, self.on_about_box)

    @staticmethod
    def on_about_box(e):
        info = wx.adv.AboutDialogInfo()

        info.SetIcon(wx.Icon('resources/main_icon.ico', wx.BITMAP_TYPE_ANY))
        info.SetName("VEnCode App")
        info.SetVersion('0.1')
        info.SetDescription(VEnCode.__doc__)
        info.SetCopyright(f'(C) 2020 {VEnCode.__author__}')
        info.SetWebSite('https://github.com/AndreMacedo88/VEnCode')
        with open("LICENSE", "r") as file:
            license_ = "".join(file.readlines())
            info.SetLicence(license_)
        info.AddDeveloper('André Macedo')

        wx.adv.AboutBox(info)
