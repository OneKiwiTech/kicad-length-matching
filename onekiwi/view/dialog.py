# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LengthMatchingDialog
###########################################################################

class LengthMatchingDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Length Matching", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP )

		bSizer1.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonLoadSetting = wx.Button( self, wx.ID_ANY, u"Load Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.buttonLoadSetting, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonSaveSetting = wx.Button( self, wx.ID_ANY, u"Save Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.buttonSaveSetting, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonUpdateLength = wx.Button( self, wx.ID_ANY, u"Update Track Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.buttonUpdateLength, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonClearHighlight = wx.Button( self, wx.ID_ANY, u"Clear Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.buttonClearHighlight, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer24, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.textLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer25.Add( self.textLog, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.buttonClearLog = wx.Button( self, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.buttonClearLog, 0, wx.ALL|wx.EXPAND, 5 )

		self.buttonCopyLog = wx.Button( self, wx.ID_ANY, u"Copy Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.buttonCopyLog, 0, wx.ALL|wx.EXPAND, 5 )

		self.buttonExit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.buttonExit, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer25.Add( bSizer26, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer25, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

###########################################################################
## Class SettingPanel
###########################################################################

class SettingPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass

###########################################################################
## Class DisplayPanel
###########################################################################

class DisplayPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass

###########################################################################
## Class InfoPanel
###########################################################################

class InfoPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass
