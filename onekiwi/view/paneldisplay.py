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
## Class DisplayPanel
###########################################################################

class DisplayPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow5 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		bSizer35 = wx.BoxSizer( wx.VERTICAL )


		self.m_scrolledWindow5.SetSizer( bSizer35 )
		self.m_scrolledWindow5.Layout()
		bSizer35.Fit( self.m_scrolledWindow5 )
		bSizer31.Add( self.m_scrolledWindow5, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer31 )
		self.Layout()

	def __del__( self ):
		pass


