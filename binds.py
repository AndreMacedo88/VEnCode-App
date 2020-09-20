import wx
import menus


class PanelBinds:
    def __init__(self, parent, panel):

        self.parent = parent

        panel.Bind(wx.EVT_RIGHT_DOWN, self.on_right_down)
        panel.Bind(wx.EVT_KEY_DOWN, self.on_key_down)

    def on_right_down(self, e):
        self.parent.PopupMenu(menus.MainPopupMenu(self.parent), e.GetPosition())

    def on_key_down(self, e):
        key = e.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            question = wx.MessageBox('Are you sure to quit?', 'Question',
                                     wx.YES_NO | wx.NO_DEFAULT, self.parent)
            if question == wx.YES:
                self.parent.Close()
