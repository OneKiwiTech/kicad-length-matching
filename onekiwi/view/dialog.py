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
## Class ExtendedNetPanel
###########################################################################
class ExtendedNetPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer11.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceClassChoices = []
		self.choiceClass = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceClassChoices, 0 )
		self.choiceClass.SetSelection( 0 )
		bSizer11.Add( self.choiceClass, 0, wx.ALL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button17, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Fillter Ref:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer13.Add( self.m_staticText8, 0, wx.ALL|wx.EXPAND, 5 )

		m_choice5Choices = []
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		bSizer13.Add( self.m_choice5, 0, wx.ALL, 5 )


		bSizer12.Add( bSizer13, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Add to List", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button18, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Remove from List", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button19, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"List Ref", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer15.Add( self.m_staticText7, 0, wx.ALL, 5 )

		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, 0 )
		bSizer15.Add( self.m_listBox4, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer12.Add( bSizer15, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer16.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice6Choices = []
		self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		bSizer16.Add( self.m_choice6, 1, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Net Start:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer16.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice7Choices = []
		self.m_choice7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 0 )
		bSizer16.Add( self.m_choice7, 1, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Net End:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer16.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice8Choices = []
		self.m_choice8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice8Choices, 0 )
		self.m_choice8.SetSelection( 0 )
		bSizer16.Add( self.m_choice8, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer16, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()
		bSizer10.Fit( self )

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
