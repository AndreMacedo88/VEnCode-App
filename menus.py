import wx


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
        self.parent.Close()


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
        self.parent.Close()
