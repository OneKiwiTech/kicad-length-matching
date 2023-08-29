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
## Class SettingPanel
###########################################################################

class SettingPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow4 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow4.SetScrollRate( 5, 5 )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow4, wx.ID_ANY, u"Class" ), wx.HORIZONTAL )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer32.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceClassChoices = []
		self.choiceClass = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceClassChoices, 0 )
		self.choiceClass.SetSelection( 0 )
		bSizer32.Add( self.choiceClass, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer3.Add( bSizer32, 2, wx.EXPAND, 5 )

		bSizer341 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer341.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textFrom = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textFrom.Wrap( -1 )

		bSizer341.Add( self.textFrom, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText21 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer341.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textTo = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textTo.Wrap( -1 )

		bSizer341.Add( self.textTo, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer3.Add( bSizer341, 1, wx.EXPAND, 5 )


		bSizer34.Add( sbSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow4, wx.ID_ANY, u"Setting" ), wx.VERTICAL )


		bSizer34.Add( sbSizer11, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow4.SetSizer( bSizer34 )
		self.m_scrolledWindow4.Layout()
		bSizer34.Fit( self.m_scrolledWindow4 )
		bSizer30.Add( self.m_scrolledWindow4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer30 )
		self.Layout()

	def __del__( self ):
		pass


