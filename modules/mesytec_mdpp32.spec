// -*- C++ -*-

/* This file is part of UCESB - a tool for data unpacking and processing.
 *
 * Copyright (C) 2017  Bastian Loeher  <b.loeher@gsi.de>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA  02110-1301  USA
 */

/*
 * ------------------------------------------------------------------------
 *  MULTI-HIT ADC AND TDC
 * ------------------------------------------------------------------------
 * 16 SIGNAL INPUTS ARE PRESENT ON THE VME MODULE
 * 34 CHANNELS ARE ENCODED
 * data [0..31] : ADC VALUE FOR INPUT 0..31
 * data [32..63]: TDC VALUE FOR INPUT 0..31
 * data [64]    : TDC VALUE FOR TRIGGER INPUT T0
 * data [65]    : TDC VALUE FOR TRIGGER INPUT T1
 */

VME_MESYTEC_MDPP32(geom)
{
  MEMBER(DATA16_OVERFLOW data[66] ZERO_SUPPRESS_MULTI(20));

  MARK_COUNT(start);
  UINT32 header NOENCODE
  {
    0_9:   word_number; // includes end_of_event
    10_12: adc_res;
    13_15: tdc_res;
    16_23: geom = MATCH(geom);
    24_29: 0b000000;
    30_31: 0b01;
  }

  several UINT32 ch_data NOENCODE
  {
    0_15:  value;
    16_21: channel;
    22: overflow;
    23: pileup;
    24_27: 0b0000;
    28_31: 0b0001;

    ENCODE(data[channel], (value = value, overflow = overflow, pileup = pileup));
  }

  several UINT32 fill_word NOENCODE
  {
    0_31: 0x0;
  }

  UINT32 end_of_event
  {
    0_29:  counter;
    30_31: 0b11;
  }

  MARK_COUNT(end);
  CHECK_COUNT(header.word_number,start,end,-4,4);
}
