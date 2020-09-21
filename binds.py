import wx
import menus
import helpers


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
            helpers.question_exit_safely(self.parent)
