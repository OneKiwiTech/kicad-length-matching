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
## Class SimplePluginFrame
###########################################################################

class SimplePluginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Simple Plugin", pos = wx.DefaultPosition, size = wx.Size( 320,240 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizerMain = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Display" ), wx.VERTICAL )

		self.edit = wx.TextCtrl( sizerMain.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMain.Add( self.edit, 0, wx.ALL|wx.EXPAND, 5 )

		self.button = wx.Button( sizerMain.GetStaticBox(), wx.ID_ANY, u"Button", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMain.Add( self.button, 0, wx.ALL|wx.EXPAND, 5 )

		self.text = wx.StaticText( sizerMain.GetStaticBox(), wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text.Wrap( -1 )

		sizerMain.Add( self.text, 0, wx.ALL, 5 )


		self.SetSizer( sizerMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SHOW, self.OnShow )
		self.button.Bind( wx.EVT_BUTTON, self.OnButtonPress )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnShow( self, event ):
		event.Skip()

	def OnButtonPress( self, event ):
		event.Skip()


