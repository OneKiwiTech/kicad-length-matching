import logging
import pcbnew
import os
from .simple_plugin_gui import SimplePluginFrame

class SimplePlugin(SimplePluginFrame):

    def __init__(self):
        super(SimplePlugin, self).__init__(None)
    
    def OnShow(self, event):
        file_name = pcbnew.GetBoard().GetFileName()
        base = os.path.basename(file_name)
        self.text.LabelText = base
        logging.debug('init done')

    def OnButtonPress(self, event):
        logging.debug('button pressed')
        txt = self.edit.GetValue()
        if txt == '':
            self.text.LabelText = 'Please input text'
        else:
            self.text.LabelText = txt
            self.edit.SetValue('')
