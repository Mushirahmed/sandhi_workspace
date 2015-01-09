#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Jan  2 10:24:11 2015
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
from sbhs import plot_sink
import gnuradio.sbhs.sbfan as sbfan
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.variable_slider_0 = variable_slider_0 = 30
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
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
		self.sbfan_0 = sbfan.sbfan(1,0,0)
		self.plot_sink_0 = plot_sink.plot_sink_f(
			self.GetWin(),
			title="Scope Plot",
			vlen=1,
			decim=1,
			gsz=1000,
			zoom=0,
		)
		self.Add(self.plot_sink_0.win)
		self.gr_sig_source_x_0 = gr.sig_source_f(samp_rate, gr.GR_SIN_WAVE, 1000, 30, 0)
		self.gr_delay_0 = gr.delay(gr.sizeof_float*1, 5)
		self.gr_add_const_vxx_0 = gr.add_const_vff((30, ))
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 40)

		##################################################
		# Connections
		##################################################
		self.connect((self.const_source_x_0, 0), (self.sbfan_0, 0))
		self.connect((self.gr_sig_source_x_0, 0), (self.gr_add_const_vxx_0, 0))
		self.connect((self.sbfan_0, 0), (self.plot_sink_0, 0))
		self.connect((self.gr_add_const_vxx_0, 0), (self.gr_delay_0, 0))
		self.connect((self.gr_delay_0, 0), (self.sbfan_0, 1))


	def get_variable_slider_0(self):
		return self.variable_slider_0

	def set_variable_slider_0(self, variable_slider_0):
		self.variable_slider_0 = variable_slider_0
		self._variable_slider_0_slider.set_value(self.variable_slider_0)
		self._variable_slider_0_text_box.set_value(self.variable_slider_0)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.gr_sig_source_x_0.set_sampling_freq(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

