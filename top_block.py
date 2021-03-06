#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Jan  9 10:57:15 2015
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import gnuradio.power
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.variable_slider_1 = variable_slider_1 = 2
		self.variable_slider_0 = variable_slider_0 = 2
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		_variable_slider_1_sizer = wx.BoxSizer(wx.VERTICAL)
		self._variable_slider_1_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_variable_slider_1_sizer,
			value=self.variable_slider_1,
			callback=self.set_variable_slider_1,
			label='variable_slider_1',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._variable_slider_1_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_variable_slider_1_sizer,
			value=self.variable_slider_1,
			callback=self.set_variable_slider_1,
			minimum=0,
			maximum=100,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_variable_slider_1_sizer)
		_variable_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
		self._variable_slider_0_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_variable_slider_0_sizer,
			value=self.variable_slider_0,
			callback=self.set_variable_slider_0,
			label='variable_slider_0',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._variable_slider_0_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_variable_slider_0_sizer,
			value=self.variable_slider_0,
			callback=self.set_variable_slider_0,
			minimum=0,
			maximum=100,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_variable_slider_0_sizer)
		self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
			self.GetWin(),
			unit="Units",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate,
			number_rate=15,
			average=False,
			avg_alpha=None,
			label="Number Plot",
			peak_hold=False,
			show_gauge=True,
		)
		self.Add(self.wxgui_numbersink2_0.win)
		self.power_xy_power_0 = gnuradio.power.power()
		self.const_source_x_1 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, variable_slider_1)
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, variable_slider_0)

		##################################################
		# Connections
		##################################################
		self.connect((self.const_source_x_0, 0), (self.power_xy_power_0, 0))
		self.connect((self.const_source_x_1, 0), (self.power_xy_power_0, 1))
		self.connect((self.power_xy_power_0, 0), (self.wxgui_numbersink2_0, 0))


	def get_variable_slider_1(self):
		return self.variable_slider_1

	def set_variable_slider_1(self, variable_slider_1):
		self.variable_slider_1 = variable_slider_1
		self.const_source_x_1.set_offset(self.variable_slider_1)
		self._variable_slider_1_slider.set_value(self.variable_slider_1)
		self._variable_slider_1_text_box.set_value(self.variable_slider_1)

	def get_variable_slider_0(self):
		return self.variable_slider_0

	def set_variable_slider_0(self, variable_slider_0):
		self.variable_slider_0 = variable_slider_0
		self._variable_slider_0_slider.set_value(self.variable_slider_0)
		self._variable_slider_0_text_box.set_value(self.variable_slider_0)
		self.const_source_x_0.set_offset(self.variable_slider_0)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

