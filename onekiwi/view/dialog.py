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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Length Matching", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP|wx.BORDER_DEFAULT )

		bSizer1.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonLoadSetting = wx.Button( self, wx.ID_ANY, u"Load Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.buttonLoadSetting, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonSaveSetting = wx.Button( self, wx.ID_ANY, u"Save Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.buttonSaveSetting, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonUpdateLength = wx.Button( self, wx.ID_ANY, u"Update Track Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.buttonUpdateLength, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonClearHighlight = wx.Button( self, wx.ID_ANY, u"Clear Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.buttonClearHighlight, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.staticline, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.textLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer10.Add( self.textLog, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.buttonClearLog = wx.Button( self, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.buttonClearLog, 0, wx.ALL|wx.EXPAND, 5 )

		self.buttonCopyLog = wx.Button( self, wx.ID_ANY, u"Copy Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.buttonCopyLog, 0, wx.ALL|wx.EXPAND, 5 )

		self.buttonExit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.buttonExit, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( bSizer11, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer10, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class ClassPanel
###########################################################################
class ClassPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Create Class:" ), wx.HORIZONTAL )

		self.textName = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textName.Wrap( -1 )

		sbSizer1.Add( self.textName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editClass = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.editClass, 1, wx.ALL, 5 )

		self.buttonAddClass = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Add Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.buttonAddClass, 0, wx.ALL, 5 )


		bSizer5.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Edit Class:" ), wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.textClass = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textClass.Wrap( -1 )

		bSizer9.Add( self.textClass, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceClassChoices = []
		self.choiceClass = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceClassChoices, 0 )
		self.choiceClass.SetSelection( 0 )
		bSizer9.Add( self.choiceClass, 0, wx.ALL, 5 )

		self.textFrom = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"From Reference:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textFrom.Wrap( -1 )

		bSizer9.Add( self.textFrom, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		filtterFromChoices = []
		self.filtterFrom = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, filtterFromChoices, 0 )
		self.filtterFrom.SetSelection( 0 )
		bSizer9.Add( self.filtterFrom, 1, wx.ALL|wx.EXPAND, 5 )

		self.textTo = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"To Reference:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textTo.Wrap( -1 )

		bSizer9.Add( self.textTo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		filtterToChoices = []
		self.filtterTo = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, filtterToChoices, 0 )
		self.filtterTo.SetSelection( 0 )
		bSizer9.Add( self.filtterTo, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonUpdateNet = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Update Net", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.buttonUpdateNet, 0, wx.ALL, 5 )


		sbSizer2.Add( bSizer9, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		listNetChoices = []
		self.listNet = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listNetChoices, 0 )
		bSizer10.Add( self.listNet, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonAddAll = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.buttonAddAll, 0, wx.ALL, 5 )

		self.buttonAddSelected = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.buttonAddSelected, 0, wx.ALL, 5 )

		self.buttonRemoveSelected = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.buttonRemoveSelected, 0, wx.ALL, 5 )

		self.buttonRemoveAll = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.buttonRemoveAll, 0, wx.ALL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer10.Add( bSizer11, 0, wx.ALL|wx.EXPAND, 5 )

		listNetClassChoices = []
		self.listNetClass = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listNetClassChoices, 0 )
		bSizer10.Add( self.listNetClass, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer10, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.textRemane = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Edit Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textRemane.Wrap( -1 )

		bSizer12.Add( self.textRemane, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.editRename = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.editRename, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonRenameClass = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Rename Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonRenameClass, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonRemoveClass = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Remove Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonRemoveClass, 0, wx.ALL|wx.EXPAND, 5 )

		self.buttonUpdateClass = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Update Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonUpdateClass, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer12, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( sbSizer2, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()
		bSizer5.Fit( self )

	def __del__( self ):
		pass



###########################################################################
## Class ExtendedNetPanel
###########################################################################

class ExtendedNetPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


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
