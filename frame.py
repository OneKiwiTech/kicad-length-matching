# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from combocheck import CheckCombo
from combolist import ListCombo
###########################################################################
## Class ComboFrame
###########################################################################

class ComboFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Combo Control", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"List Combo" ), wx.VERTICAL )

		comboListChoices = []
		#self.comboList = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboListChoices, 0 )
		self.comboList = ListCombo(self)
		sbSizer1.Add( self.comboList, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Checkbox Combo" ), wx.VERTICAL )

		comboCheckChoices = []
		#self.comboCheck = wx.ComboBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboCheckChoices, 0 )
		self.comboCheck = CheckCombo(self)
		sbSizer2.Add( self.comboCheck, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Filter Combo" ), wx.VERTICAL )

		comboFilterChoices = []
		self.comboFilter = wx.ComboBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboFilterChoices, 0 )
		sbSizer3.Add( self.comboFilter, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass