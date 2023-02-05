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
## Class ClassPanel
###########################################################################

class ClassPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Create Class:" ), wx.HORIZONTAL )

		self.textName = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textName.Wrap( -1 )

		sbSizer1.Add( self.textName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editClass = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.editClass, 1, wx.ALL, 5 )

		self.buttonAddClass = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Add Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.buttonAddClass, 0, wx.ALL, 5 )


		bSizer6.Add( sbSizer1, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Edit Class:" ), wx.VERTICAL )

		gSizer1 = wx.GridSizer( 2, 3, 0, 0 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.textClass = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textClass.Wrap( -1 )

		bSizer14.Add( self.textClass, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceClassChoices = []
		self.choiceClass = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceClassChoices, 0 )
		self.choiceClass.SetSelection( 0 )
		bSizer14.Add( self.choiceClass, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.textFilterFrom = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textFilterFrom.Wrap( -1 )

		bSizer15.Add( self.textFilterFrom, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editFrom = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.editFrom, 1, wx.ALL, 5 )


		gSizer1.Add( bSizer15, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.textFilterTo = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textFilterTo.Wrap( -1 )

		bSizer16.Add( self.textFilterTo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editTo = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.editTo, 1, wx.ALL, 5 )


		gSizer1.Add( bSizer16, 1, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonUpdateNet = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Update Net", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.buttonUpdateNet, 1, wx.ALL, 5 )


		gSizer1.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.textReferenceFrom = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textReferenceFrom.Wrap( -1 )

		bSizer18.Add( self.textReferenceFrom, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceReferenceFromChoices = []
		self.choiceReferenceFrom = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceReferenceFromChoices, 0 )
		self.choiceReferenceFrom.SetSelection( 0 )
		bSizer18.Add( self.choiceReferenceFrom, 1, wx.ALL, 5 )


		gSizer1.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.textReferenceTo = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textReferenceTo.Wrap( -1 )

		bSizer19.Add( self.textReferenceTo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceReferenceToChoices = []
		self.choiceReferenceTo = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceReferenceToChoices, 0 )
		self.choiceReferenceTo.SetSelection( 0 )
		bSizer19.Add( self.choiceReferenceTo, 1, wx.ALL, 5 )


		gSizer1.Add( bSizer19, 1, wx.EXPAND, 5 )


		sbSizer2.Add( gSizer1, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		listNetChoices = []
		self.listNet = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listNetChoices, wx.LB_MULTIPLE )
		bSizer20.Add( self.listNet, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )


		bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonAddAll = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.buttonAddAll, 0, wx.ALL, 5 )

		self.buttonAddSelected = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.buttonAddSelected, 0, wx.ALL, 5 )

		self.buttonRemoveSelected = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.buttonRemoveSelected, 0, wx.ALL, 5 )

		self.buttonRemoveAll = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.buttonRemoveAll, 0, wx.ALL, 5 )


		bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer20.Add( bSizer21, 0, wx.EXPAND, 5 )

		listNetClassChoices = []
		self.listNetClass = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listNetClassChoices, wx.LB_MULTIPLE )
		bSizer20.Add( self.listNetClass, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer20, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer2, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.textRemane = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Edit Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textRemane.Wrap( -1 )

		bSizer22.Add( self.textRemane, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editRename = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.editRename, 0, wx.ALL, 5 )

		self.buttonRenameClass = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Rename Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.buttonRenameClass, 0, wx.ALL, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonRemoveClass = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Remove Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.buttonRemoveClass, 0, wx.ALL, 5 )

		self.buttonUpdateClass = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Update Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.buttonUpdateClass, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer22, 0, wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer6 )
		self.m_scrolledWindow1.Layout()
		bSizer6.Fit( self.m_scrolledWindow1 )
		bSizer5.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()
		bSizer5.Fit( self )

	def __del__( self ):
		pass
