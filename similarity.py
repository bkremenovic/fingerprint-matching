#! /usr/bin/env python

from libs.pysgfplib import *
import argparse
import os

if '__main__' == __name__:
	parser = argparse.ArgumentParser()
	parser.add_argument('--samples', metavar='path', required=True, help='the path to fingerprint samples folder')
	parser.add_argument('--fingerprint', metavar='path', required=True, help='the path to fingerprint file')
	args = parser.parse_args()

	compare1 = open(args.fingerprint, 'r').read()

	sgfplib = PYSGFPLib()
	sgfplib.Create()
	sgfplib.Init(0x4)

	for fingerprint in os.listdir(args.samples):
		compare2 = open(args.samples + "/" + fingerprint, 'r').read()

		cMatched = c_bool(False)
		sgfplib.MatchTemplate(compare1, compare2, SGFDxSecurityLevel.SL_NORMAL, byref(cMatched));

		if (cMatched.value == True):
			print(fingerprint) 
			break		

	sgfplib.Terminate()