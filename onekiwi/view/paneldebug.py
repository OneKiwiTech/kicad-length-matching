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
## Class DebugPanel
###########################################################################

class DebugPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow7 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow7.SetScrollRate( 5, 5 )
		bSizer37 = wx.BoxSizer( wx.VERTICAL )


		self.m_scrolledWindow7.SetSizer( bSizer37 )
		self.m_scrolledWindow7.Layout()
		bSizer37.Fit( self.m_scrolledWindow7 )
		bSizer33.Add( self.m_scrolledWindow7, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

	def __del__( self ):
		pass


