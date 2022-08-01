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
from combofilter import FilterCombo

###########################################################################
## Class ComboFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Combo Test", pos = wx.DefaultPosition, size = wx.Size( 750,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizerMain = wx.BoxSizer( wx.HORIZONTAL )

		sizerList = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Combo List" ), wx.VERTICAL )

		comboListChoices = []
		self.comboList = wx.ComboBox( sizerList.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboListChoices, 0 )
		sizerList.Add( self.comboList, 0, wx.ALL|wx.EXPAND, 5 )


		sizerMain.Add( sizerList, 1, wx.EXPAND, 5 )

		sizerCheck = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Combo Check" ), wx.VERTICAL )

		comboCheckChoices = []
		self.comboCheck = wx.ComboBox( sizerCheck.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboCheckChoices, 0 )
		sizerCheck.Add( self.comboCheck, 0, wx.ALL|wx.EXPAND, 5 )


		sizerMain.Add( sizerCheck, 1, wx.EXPAND, 5 )

		sizerFilter = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Combo Filter" ), wx.VERTICAL )

		comboFilterChoices = []
		#self.comboFilter = wx.ComboBox( sizerFilter.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboFilterChoices, 0 )
		self.comboFilter = FilterCombo(self, -1, comboFilterChoices, style = wx.CB_DROPDOWN|wx.CB_READONLY)
		sizerFilter.Add( self.comboFilter, 0, wx.ALL|wx.EXPAND, 5 )


		sizerMain.Add( sizerFilter, 1, wx.EXPAND, 5 )


		self.SetSizer( sizerMain )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass