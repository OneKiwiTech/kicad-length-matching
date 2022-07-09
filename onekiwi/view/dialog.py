# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class LengthMatchingDialog
###########################################################################

class LengthMatchingDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Length Matching", pos = wx.DefaultPosition, size = wx.Size( 798,532 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer4.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.textStatus = wx.StaticText( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textStatus.Wrap( -1 )

		bSizer5.Add( self.textStatus, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnDialogClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnDialogClose( self, event ):
		event.Skip()


###########################################################################
## Class NetPanel
###########################################################################
class NetPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 798,532 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.textClass = wx.StaticText( self, wx.ID_ANY, u"Net Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textClass.Wrap( -1 )

		bSizer2.Add( self.textClass, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		comboClassChoices = []
		self.comboClass = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboClassChoices, 0 )
		bSizer2.Add( self.comboClass, 2, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonLoad = wx.Button( self, wx.ID_ANY, u"Load Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.buttonLoad, 0, wx.ALL, 5 )

		self.buttonSave = wx.Button( self, wx.ID_ANY, u"Save Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.buttonSave, 0, wx.ALL|wx.EXPAND, 5 )

		self.buttonUpdate = wx.Button( self, wx.ID_ANY, u"Update Track Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.buttonUpdate, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.textLength = wx.StaticText( self, wx.ID_ANY, u"Total Length = Track Length + Via Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textLength.Wrap( -1 )

		bSizer6.Add( self.textLength, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonClearHighlight = wx.Button( self, wx.ID_ANY, u"Clear Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.buttonClearHighlight, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )

		self.gridNet = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridNet.CreateGrid( 0, 7 )
		self.gridNet.EnableEditing( True )
		self.gridNet.EnableGridLines( True )
		self.gridNet.EnableDragGridSize( False )
		self.gridNet.SetMargins( 0, 0 )

		# Columns
		self.gridNet.SetColSize( 0, 100 )
		self.gridNet.SetColSize( 1, 100 )
		self.gridNet.SetColSize( 2, 100 )
		self.gridNet.SetColSize( 3, 100 )
		self.gridNet.SetColSize( 4, 100 )
		self.gridNet.SetColSize( 5, 100 )
		self.gridNet.SetColSize( 6, 100 )
		self.gridNet.EnableDragColMove( False )
		self.gridNet.EnableDragColSize( True )
		self.gridNet.SetColLabelValue( 0, u"Net Name" )
		self.gridNet.SetColLabelValue( 1, u"Pad Start" )
		self.gridNet.SetColLabelValue( 2, u"Pad End" )
		self.gridNet.SetColLabelValue( 3, u"Via Count" )
		self.gridNet.SetColLabelValue( 4, u"Via Length" )
		self.gridNet.SetColLabelValue( 5, u"Track Length" )
		self.gridNet.SetColLabelValue( 6, u"Total Length" )
		self.gridNet.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridNet.EnableDragRowSize( True )
		self.gridNet.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridNet.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.gridNet, 1, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class InfoPanel
###########################################################################
class InfoPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class xNetPanel
###########################################################################
class xNetPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.textComing = wx.StaticText( self, wx.ID_ANY, u"Coming Soon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textComing.Wrap( -1 )

		bSizer3.Add( self.textComing, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

	def __del__( self ):
		pass
