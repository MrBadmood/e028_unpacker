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
 *  VME data collector with 8 optical buses
 * ------------------------------------------------------------------------
 * 8 OPTICAL FIBER INPUTS ARE PRESENT ON THE VME MODULE
 */

// TODO: time_diff requires uint16_t casting to value, not supported.
VME_MESYTEC_VMMR8(geom)
{
	MEMBER(DATA12 data[8][128] ZERO_SUPPRESS_MULTI(20));
	
	MEMBER(DATA16 time_diff[8] ZERO_SUPPRESS);
	MEMBER(DATA16 time_ext[10] NO_INDEX_LIST);

	MARK_COUNT(start);
	UINT32 header NOENCODE
	{
		 0_11: word_number; // includes end_of_event
		12_15: 0b0000;
		16_23: geom = MATCH(geom);
		   24: trig; 
		25_29: 0b00000;
		30_31: 0b01;
	}

	list(0 <= index < header.word_number - 1) {
		UINT32 event NOENCODE {
			 0_11: part0;
			12_15: part1;
			16_23: part2;
			24_27: part3;
			28_29: type;
			30_31: 0b00;
		}

		// Channel = (event.part2 << 4 | event.part1)
		// adc_value = event.part0
		// bus = event.part3

		// HOW TO MAKE SINGLE VARIABLE FOR EACH BUS DATA
		if (1 == event.type) {
		  // ADC.
		  ENCODE(data[event.part3] // bus
			 [(event.part2 << 4 | event.part1)] // Channel
			 , (value = event.part0));
		}
		if (2 == event.type && 0 == event.part2) {
		  // Time difference.
		  ENCODE(time_diff[
				   event.part3 // Bus.
				   ], (value = event.part1 << 12 | event.part0));
		}
		if (2 == event.type && 0 != event.part2) {
		  // Extended timestamp.
		  ENCODE(time_ext APPEND_LIST,
			 (value = event.part1 << 12 | event.part0));
		}
	}

	UINT32 end_of_event
	{
		 0_29: counter;
		30_31: 0b11;
	}

	MARK_COUNT(end);
	CHECK_COUNT(header.word_number, start, end, -4, 4);
}
