#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: QQQ
# Author: RUSSIAN ICE
# Generated: Mon Jun 21 18:16:51 2021
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class PAPICH(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="QQQ")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.input_decimation = input_decimation = 100
        self.hackrf_sample_rate = hackrf_sample_rate = 8e6
        self.xlate_firdes_taps = xlate_firdes_taps = 1
        self.main_sample_rate = main_sample_rate = hackrf_sample_rate/input_decimation
        self.base_freq = base_freq = 446.02e6
        self.VLM = VLM = 1
        self.RF = RF = 20

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "FFT")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Waterfall")
        self.Add(self.notebook_0)
        self._hackrf_sample_rate_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.hackrf_sample_rate,
        	callback=self.set_hackrf_sample_rate,
        	label="Sample_rate",
        	choices=[5e6, 8e6, 10e6],
        	labels=["5M", "8M", "10M"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._hackrf_sample_rate_chooser)
        _base_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._base_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_base_freq_sizer,
        	value=self.base_freq,
        	callback=self.set_base_freq,
        	label='base_freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._base_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_base_freq_sizer,
        	value=self.base_freq,
        	callback=self.set_base_freq,
        	minimum=20e6,
        	maximum=2.5e9,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_base_freq_sizer)
        _VLM_sizer = wx.BoxSizer(wx.VERTICAL)
        self._VLM_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_VLM_sizer,
        	value=self.VLM,
        	callback=self.set_VLM,
        	label='VLM',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._VLM_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_VLM_sizer,
        	value=self.VLM,
        	callback=self.set_VLM,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_VLM_sizer)
        _RF_sizer = wx.BoxSizer(wx.VERTICAL)
        self._RF_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_RF_sizer,
        	value=self.RF,
        	callback=self.set_RF,
        	label="RF_GAIN",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._RF_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_RF_sizer,
        	value=self.RF,
        	callback=self.set_RF,
        	minimum=0,
        	maximum=50,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_RF_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=main_sample_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
        	baseband_freq=base_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=main_sample_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=input_decimation,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=6,
                decimation=10,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(hackrf_sample_rate)
        self.osmosdr_source_0.set_center_freq(base_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(RF, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, main_sample_rate, 12e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((VLM, ))
        self.audio_sink_0 = audio.sink(44100, "pulse", True)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=int(main_sample_rate),
        	quad_rate=int(main_sample_rate),
        	tau=75e-6,
        	max_dev=5e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_1, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.low_pass_filter_1, 0), (self.wxgui_waterfallsink2_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_1_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.low_pass_filter_1, 0))    

    def get_input_decimation(self):
        return self.input_decimation

    def set_input_decimation(self, input_decimation):
        self.input_decimation = input_decimation
        self.set_main_sample_rate(self.hackrf_sample_rate/self.input_decimation)

    def get_hackrf_sample_rate(self):
        return self.hackrf_sample_rate

    def set_hackrf_sample_rate(self, hackrf_sample_rate):
        self.hackrf_sample_rate = hackrf_sample_rate
        self._hackrf_sample_rate_chooser.set_value(self.hackrf_sample_rate)
        self.set_main_sample_rate(self.hackrf_sample_rate/self.input_decimation)
        self.osmosdr_source_0.set_sample_rate(self.hackrf_sample_rate)

    def get_xlate_firdes_taps(self):
        return self.xlate_firdes_taps

    def set_xlate_firdes_taps(self, xlate_firdes_taps):
        self.xlate_firdes_taps = xlate_firdes_taps

    def get_main_sample_rate(self):
        return self.main_sample_rate

    def set_main_sample_rate(self, main_sample_rate):
        self.main_sample_rate = main_sample_rate
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.main_sample_rate, 12e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.main_sample_rate)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.main_sample_rate)

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq
        self._base_freq_slider.set_value(self.base_freq)
        self._base_freq_text_box.set_value(self.base_freq)
        self.osmosdr_source_0.set_center_freq(self.base_freq, 0)
        self.wxgui_fftsink2_0.set_baseband_freq(self.base_freq)

    def get_VLM(self):
        return self.VLM

    def set_VLM(self, VLM):
        self.VLM = VLM
        self._VLM_slider.set_value(self.VLM)
        self._VLM_text_box.set_value(self.VLM)
        self.blocks_multiply_const_vxx_0.set_k((self.VLM, ))

    def get_RF(self):
        return self.RF

    def set_RF(self, RF):
        self.RF = RF
        self._RF_slider.set_value(self.RF)
        self._RF_text_box.set_value(self.RF)
        self.osmosdr_source_0.set_gain(self.RF, 0)


def main(top_block_cls=PAPICH, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
