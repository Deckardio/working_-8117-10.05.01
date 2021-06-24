#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Artas
# Generated: Thu Jun 24 14:35:04 2021
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class ARTAS(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Artas")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sample_rate = sample_rate = 2.4E6
        self.RF = RF = 13
        self.CF = CF = 446020000

        ##################################################
        # Blocks
        ##################################################
        self._sample_rate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.sample_rate,
        	callback=self.set_sample_rate,
        	label="Sample Rate: 1.024M, 1.4M, 1.8M, 1.92M, 2.048M, 2.4M & 2. 56M",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._sample_rate_text_box, 7, 0, 1, 5)
        _CF_sizer = wx.BoxSizer(wx.VERTICAL)
        self._CF_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_CF_sizer,
        	value=self.CF,
        	callback=self.set_CF,
        	label="Center Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._CF_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_CF_sizer,
        	value=self.CF,
        	callback=self.set_CF,
        	minimum=80.9e6,
        	maximum=2400000000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_CF_sizer, 5, 0, 1, 5)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=2400000,
                decimation=88200,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_1 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_1.set_sample_rate(sample_rate)
        self.osmosdr_sink_1.set_center_freq(CF, 0)
        self.osmosdr_sink_1.set_freq_corr(0, 0)
        self.osmosdr_sink_1.set_gain(10, 0)
        self.osmosdr_sink_1.set_if_gain(60, 0)
        self.osmosdr_sink_1.set_bb_gain(20, 0)
        self.osmosdr_sink_1.set_antenna("", 0)
        self.osmosdr_sink_1.set_bandwidth(0, 0)
          
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "TX")
        self.GridAdd(self.notebook_0, 1, 0, 4, 5)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/media/sigintos/USB DISK/GNURADIO/Sergjj_Brajjlyan_-_Salo_72157915.wav", True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2, ))
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=44100,
        	quad_rate=88200,
        	tau=75e-6,
        	max_dev=5e3,
                )
        _RF_sizer = wx.BoxSizer(wx.VERTICAL)
        self._RF_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_RF_sizer,
        	value=self.RF,
        	callback=self.set_RF,
        	label="RF Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._RF_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_RF_sizer,
        	value=self.RF,
        	callback=self.set_RF,
        	minimum=0,
        	maximum=45,
        	num_steps=45,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_RF_sizer, 6, 0, 1, 5)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.osmosdr_sink_1, 0))    

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self._sample_rate_text_box.set_value(self.sample_rate)
        self.osmosdr_sink_1.set_sample_rate(self.sample_rate)

    def get_RF(self):
        return self.RF

    def set_RF(self, RF):
        self.RF = RF
        self._RF_slider.set_value(self.RF)
        self._RF_text_box.set_value(self.RF)

    def get_CF(self):
        return self.CF

    def set_CF(self, CF):
        self.CF = CF
        self._CF_slider.set_value(self.CF)
        self._CF_text_box.set_value(self.CF)
        self.osmosdr_sink_1.set_center_freq(self.CF, 0)


def main(top_block_cls=ARTAS, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
