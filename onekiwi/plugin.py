import pcbnew
import os
from .controller.controller import Controller

class LengthMatchingAction(pcbnew.ActionPlugin):
	def defaults(self):
		self.name = "Length Matching"
		self.category = "Read PCB"
		self.description = "Fill a selected copper area with a pattern of vias"
		self.show_toolbar_button = True # Optional, defaults to False
		self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') # Optional

	def Run(self):
		# The entry function of the plugin that is executed on user action
		board = pcbnew.GetBoard()
		controller = Controller(board)
		controller.Show()
		pcbnew.UpdateUserInterface()
       
