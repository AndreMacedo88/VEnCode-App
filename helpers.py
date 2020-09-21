import wx


def question_exit_safely(frame):
    question = wx.MessageBox('Are you sure you want to quit?', 'Exit VEnCode',
                             wx.YES_NO | wx.NO_DEFAULT, frame)
    if question == wx.YES:
        frame.Close()


def panel_normal_layout(panel):
    panel.SetAutoLayout(True)
    panel.Layout()
    panel.Fit()
