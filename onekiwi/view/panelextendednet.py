# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class ExtendedNetPanel
###########################################################################

class ExtendedNetPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"label" ), wx.HORIZONTAL )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer32.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceClassChoices = []
		self.choiceClass = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceClassChoices, 0 )
		self.choiceClass.SetSelection( 0 )
		bSizer32.Add( self.choiceClass, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer3.Add( bSizer32, 2, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer34.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textFrom = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textFrom.Wrap( -1 )

		bSizer34.Add( self.textFrom, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText21 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer34.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textTo = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textTo.Wrap( -1 )

		bSizer34.Add( self.textTo, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer3.Add( bSizer34, 1, wx.EXPAND, 5 )


		bSizer22.Add( sbSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"label" ), wx.VERTICAL )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer18.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editFilter = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.editFilter, 1, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Reference:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer18.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceReferenceChoices = []
		self.choiceReference = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceReferenceChoices, 0 )
		self.choiceReference.SetSelection( 0 )
		bSizer18.Add( self.choiceReference, 1, wx.ALL, 5 )

		self.buttonUpdate = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.buttonUpdate, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer4.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText24 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Primary Net:     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer35.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceNetName1Choices = []
		self.choiceNetName1 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNetName1Choices, 0 )
		self.choiceNetName1.SetSelection( 0 )
		bSizer35.Add( self.choiceNetName1, 1, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Start:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer35.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceNetStart1Choices = []
		self.choiceNetStart1 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNetStart1Choices, 0 )
		self.choiceNetStart1.SetSelection( 0 )
		bSizer35.Add( self.choiceNetStart1, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"End:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer35.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceNetEnd1Choices = []
		self.choiceNetEnd1 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNetEnd1Choices, 0 )
		self.choiceNetEnd1.SetSelection( 0 )
		bSizer35.Add( self.choiceNetEnd1, 0, wx.ALL, 5 )


		sbSizer4.Add( bSizer35, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText28 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Secondary Net:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer39.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceNetName2Choices = []
		self.choiceNetName2 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNetName2Choices, 0 )
		self.choiceNetName2.SetSelection( 0 )
		bSizer39.Add( self.choiceNetName2, 1, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Start:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		bSizer39.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceNetStart2Choices = []
		self.choiceNetStart2 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNetStart2Choices, 0 )
		self.choiceNetStart2.SetSelection( 0 )
		bSizer39.Add( self.choiceNetStart2, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"End:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer39.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceNetEnd2Choices = []
		self.choiceNetEnd2 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNetEnd2Choices, 0 )
		self.choiceNetEnd2.SetSelection( 0 )
		bSizer39.Add( self.choiceNetEnd2, 0, wx.ALL, 5 )


		sbSizer4.Add( bSizer39, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonAddxNet = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Add xNet", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.buttonAddxNet, 0, wx.ALL, 5 )

		self.buttonRemovexNet = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Remove xNet", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.buttonRemovexNet, 0, wx.ALL, 5 )


		sbSizer4.Add( bSizer40, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_dataViewListCtrl2 = wx.dataview.DataViewListCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_dataViewListCtrl2, 1, wx.ALL, 5 )


		sbSizer4.Add( bSizer20, 1, wx.EXPAND, 5 )


		bSizer22.Add( sbSizer4, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer22 )
		self.m_scrolledWindow2.Layout()
		bSizer22.Fit( self.m_scrolledWindow2 )
		bSizer16.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()
		bSizer16.Fit( self )

	def __del__( self ):
		pass


