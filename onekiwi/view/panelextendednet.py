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

		self.m_staticText8 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		sbSizer3.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceClassChoices = []
		self.choiceClass = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceClassChoices, 0 )
		self.choiceClass.SetSelection( 0 )
		sbSizer3.Add( self.choiceClass, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( sbSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"label" ), wx.VERTICAL )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer18.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_textCtrl6, 1, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Reference:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer18.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice5Choices = []
		self.m_choice5 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		bSizer18.Add( self.m_choice5, 1, wx.ALL, 5 )

		self.m_button19 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button19, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer4.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer27.Add( self.m_staticText12, 0, wx.ALL, 5 )

		listNetChoices = []
		self.listNet = wx.ListBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listNetChoices, wx.LB_MULTIPLE )
		bSizer27.Add( self.listNet, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer201.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer26.Add( self.m_staticText13, 0, wx.ALL, 5 )

		listNetClassChoices = []
		self.listNetClass = wx.ListBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listNetClassChoices, wx.LB_MULTIPLE )
		bSizer26.Add( self.listNetClass, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer201.Add( bSizer26, 1, wx.EXPAND, 5 )


		bSizer20.Add( bSizer201, 1, wx.EXPAND, 5 )


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


