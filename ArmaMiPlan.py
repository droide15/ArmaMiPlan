# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Arma mi plan", pos = wx.DefaultPosition, size = wx.Size( 534,559 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 0, 0, 5 )
		
		m_checkList1Choices = []
		self.m_checkList1 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,150 ), m_checkList1Choices, 0 )
		bSizer2.Add( self.m_checkList1, 0, wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 0, 0, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 0, 0, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,100 ), m_listBox2Choices, 0 )
		bSizer6.Add( self.m_listBox2, 0, wx.ALL, 5 )
		
		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,100 ), m_listBox3Choices, 0 )
		bSizer6.Add( self.m_listBox3, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 0, 0, 5 )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,200 ), 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 14, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"Lunes" )
		self.m_grid1.SetColLabelValue( 1, u"Martes" )
		self.m_grid1.SetColLabelValue( 2, u"Miercoles" )
		self.m_grid1.SetColLabelValue( 3, u"Jueves" )
		self.m_grid1.SetColLabelValue( 4, u"Viernes" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelValue( 0, u"7-8" )
		self.m_grid1.SetRowLabelValue( 1, u"8-9" )
		self.m_grid1.SetRowLabelValue( 2, u"9-10" )
		self.m_grid1.SetRowLabelValue( 3, u"10-11" )
		self.m_grid1.SetRowLabelValue( 4, u"11-12" )
		self.m_grid1.SetRowLabelValue( 5, u"12-13" )
		self.m_grid1.SetRowLabelValue( 6, u"13-14" )
		self.m_grid1.SetRowLabelValue( 7, u"14-15" )
		self.m_grid1.SetRowLabelValue( 8, u"15-16" )
		self.m_grid1.SetRowLabelValue( 9, u"16-17" )
		self.m_grid1.SetRowLabelValue( 10, u"17-18" )
		self.m_grid1.SetRowLabelValue( 11, u"18-19" )
		self.m_grid1.SetRowLabelValue( 12, u"19-20" )
		self.m_grid1.SetRowLabelValue( 13, u"20-21" )
		self.m_grid1.SetRowLabelValue( 14, u"7-8" )
		self.m_grid1.SetRowLabelValue( 15, wx.EmptyString )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.m_grid1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Horarios", pos = wx.DefaultPosition, size = wx.Size( 514,571 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, 0, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,100 ), m_listBox4Choices, 0 )
		bSizer3.Add( self.m_listBox4, 0, wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer4, 0, 0, 5 )
		
		
		bSizer1.Add( bSizer3, 0, 0, 5 )
		
		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid2.CreateGrid( 14, 5 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"Lunes" )
		self.m_grid2.SetColLabelValue( 1, u"Martes" )
		self.m_grid2.SetColLabelValue( 2, u"Miercoles" )
		self.m_grid2.SetColLabelValue( 3, u"Jueves" )
		self.m_grid2.SetColLabelValue( 4, u"Viernes" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelValue( 0, u"7-8" )
		self.m_grid2.SetRowLabelValue( 1, u"8-9" )
		self.m_grid2.SetRowLabelValue( 2, u"9-10" )
		self.m_grid2.SetRowLabelValue( 3, u"10-11" )
		self.m_grid2.SetRowLabelValue( 4, u"11-12" )
		self.m_grid2.SetRowLabelValue( 5, u"12-13" )
		self.m_grid2.SetRowLabelValue( 6, u"13-14" )
		self.m_grid2.SetRowLabelValue( 7, u"14-15" )
		self.m_grid2.SetRowLabelValue( 8, u"15-16" )
		self.m_grid2.SetRowLabelValue( 9, u"16-17" )
		self.m_grid2.SetRowLabelValue( 10, u"17-18" )
		self.m_grid2.SetRowLabelValue( 11, u"18-19" )
		self.m_grid2.SetRowLabelValue( 12, u"19-20" )
		self.m_grid2.SetRowLabelValue( 13, u"20-21" )
		self.m_grid2.SetRowLabelValue( 14, u"7-8" )
		self.m_grid2.SetRowLabelValue( 15, wx.EmptyString )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.m_grid2, 0, wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 0, 0, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		bSizer1.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

