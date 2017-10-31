#! /usr/bin/env python
'''
 * pysgfplib.py
 * SecuGen Fingerprint Library Wrapper.
 *
 * Created on December 18, 2014
 * Copyright(c): SecuGen Corporation, All rights reserved
'''

from ctypes import *
from sgfdxerrorcode import *
from sgfdxdevicename import *
from sgfdxsecuritylevel import *

class PYSGFPLib:

  slib   = '/usr/local/lib/libpysgfplib.so'
  hlib   = CDLL(slib)

  def __init__(self):
    self.data = []

  def Create(self):
    return self.hlib.PY_SGFPM_Create()

  def Terminate(self):
    return self.hlib.PY_SGFPM_Terminate()

  #virtual ~SGFPM(){};
  #virtual DWORD WINAPI  GetLastError() = 0;

  def Init(self, devName):
    return self.hlib.PY_SGFPM_Init(c_long(devName))

  #virtual DWORD WINAPI  InitEx(DWORD width, DWORD height, DWORD dpi) = 0;
  #virtual DWORD WINAPI  SetTemplateFormat(WORD format) = 0; // default is SG400

  #Image sensor API
  #virtual DWORD WINAPI  EnumerateDevice(DWORD* ndevs, SGDeviceList** devList) = 0;
  def OpenDevice(self, devId):
    return self.hlib.PY_SGFPM_OpenDevice(c_long(devId))

  def CloseDevice(self):
    return self.hlib.PY_SGFPM_CloseDevice()

  #virtual DWORD WINAPI  GetDeviceInfo(SGDeviceInfoParam* pInfo)= 0;
  #virtual DWORD WINAPI  Configure(HWND hwnd) = 0;
  #virtual DWORD WINAPI  SetBrightness(DWORD brightness) = 0;

  def SetLedOn(self, bOn = True):
    return self.hlib.PY_SGFPM_SetLedOn(c_bool(bOn))

  def GetImage(self, buffer):
    return self.hlib.PY_SGFPM_GetImage(buffer)
    
    return result
  
  #virtual DWORD WINAPI  GetImageEx(BYTE* buffer, DWORD timeout, HWND dispWnd, DWORD quality)= 0;
  #virtual DWORD WINAPI  GetImageEx2(BYTE* buffer, DWORD timeout, HDC dispDC, LPRECT dispRect, DWORD quality)= 0;

  def GetImageQuality(self, width, height, imgBuf, quality):
    return self.hlib.PY_SGFPM_GetImageQuality(width, height, imgBuf, quality)

  #virtual DWORD WINAPI  SetCallBackFunction(DWORD selector, DWORD (WINAPI*)(void* pUserData, void* pCallBackData), void* pUserData) = 0;

  #// FDU03 Only APIs
  #virtual DWORD WINAPI  EnableAutoOnEvent(BOOL enable, HWND hwnd, void* reserved)= 0;

  #// Algorithm: Extraction API
  #virtual DWORD WINAPI  GetMaxTemplateSize(DWORD* size) = 0;
  #virtual DWORD WINAPI  CreateTemplate(SGFingerInfo* fpInfo, BYTE *rawImage, BYTE* minTemplate)= 0;
  #virtual DWORD WINAPI  GetTemplateSize(BYTE* buf, DWORD* size) = 0;
  def CreateSG400Template(self, rawImage, minTemplate):
    return self.hlib.PY_SGFPM_CreateSG400Template(rawImage, minTemplate)

  #// Algorithm: Matching API
  def MatchTemplate(self, minTemplate1, minTemplate2, secuLevel, matched):
    return self.hlib.PY_SGFPM_MatchTemplate(minTemplate1, minTemplate2, secuLevel, matched)

  def GetMatchingScore(self, minTemplate1, minTemplate2, score):
    return self.hlib.PY_SGFPM_GetMatchingScore(minTemplate1, minTemplate2, score)

  #// Algorithim: Only work with ANSI378 Template
  #virtual DWORD  WINAPI  GetTemplateSizeAfterMerge(BYTE* ansiTemplate1, BYTE* ansiTemplate2, DWORD* size) = 0;
  #virtual DWORD  WINAPI  MergeAnsiTemplate(BYTE* ansiTemplate1, BYTE* ansiTemplate2, BYTE* outTemplate) = 0;
  #virtual DWORD  WINAPI  MergeMultipleAnsiTemplate(BYTE* inTemplates, DWORD nTemplates, BYTE* outTemplate) = 0;
  #virtual DWORD  WINAPI  GetAnsiTemplateInfo(BYTE* ansiTemplate, SGANSITemplateInfo* templateInfo) = 0;
  #virtual DWORD  WINAPI  MatchAnsiTemplate(BYTE*  ansiTemplate1, DWORD  sampleNum1, BYTE*  ansiTemplate2, DWORD sampleNum2, DWORD secuLevel, BOOL*  matched) = 0;
  #virtual DWORD  WINAPI  GetAnsiMatchingScore(BYTE*  ansiTemplate1, DWORD    sampleNum1, BYTE* ansiTemplate2, DWORD sampleNum2, DWORD* score) = 0;


  #// Algorithim: Only work with ISO19794 Template
  #virtual DWORD  WINAPI  GetIsoTemplateSizeAfterMerge(BYTE* isoTemplate1, BYTE* isoTemplate2, DWORD* size) = 0;
  #virtual DWORD  WINAPI  MergeIsoTemplate(BYTE* isoTemplate1, BYTE* isoTemplate2, BYTE* outTemplate) = 0;
  #virtual DWORD  WINAPI  MergeMultipleIsoTemplate(BYTE* inTemplates, DWORD nTemplates, BYTE* outTemplate) = 0;
  #virtual DWORD  WINAPI  GetIsoTemplateInfo(BYTE* isoTemplate, SGISOTemplateInfo* templateInfo) = 0;
  #virtual DWORD  WINAPI  MatchIsoTemplate(BYTE*  isoTemplate1, DWORD sampleNum1, BYTE*  isoTemplate2, DWORD sampleNum2, DWORD secuLevel, BOOL*  matched) = 0;
  #virtual DWORD  WINAPI  GetIsoMatchingScore(BYTE*  isoTemplate1, DWORD sampleNum1, BYTE* isoTemplate2, DWORD sampleNum2, DWORD* score) = 0;

  #// Algorithim: 
  #virtual DWORD  WINAPI  MatchTemplateEx(BYTE*  minTemplate1, WORD tempateType1,  DWORD sampleNum1, BYTE* minTemplate2, WORD tempateType2,  DWORD sampleNum2, DWORD  secuLevel, BOOL*  matched) = 0;
  #virtual DWORD  WINAPI  GetMatchingScoreEx(BYTE* minTemplate1, WORD tempateType1, DWORD sampleNum1, BYTE* minTemplate2, WORD tempateType2, DWORD sampleNum2, DWORD* score) = 0;

  #// 2006.6.5, Device Driver
  #virtual  DWORD	WINAPI  SetAutoOnIRLedTouchOn(BOOL iRLed, BOOL touchOn) = 0;
  #// Algorithm, 2006.10.9, jkang
  #virtual  DWORD  WINAPI  GetMinexVersion(DWORD *extractor, DWORD* matcher) = 0;

  #// Algorithm, 2006.10.9, Can set Image width, height, xRes, yRes separately 
  #virtual  DWORD  WINAPI  CreateTemplateEx(SGFPImageInfo* fpImageInfo, BYTE *rawImage, BYTE* minTemplate)= 0;
  #// Algorithm, 2006.10.9, have Image width, height, xRes, yRes separately 
  #virtual DWORD  WINAPI   GetAnsiTemplateInfoEx(BYTE* ansiTemplate, SGANSITemplateInfoEx* templateInfo) = 0;

  #// 06/08/2009, Enable/disable the check of finger liveness
  #virtual DWORD WINAPI		EnableCheckOfFingerLiveness(bool enable) = 0;

  #// 05/19/2011, Adjust fake detection level
  #virtual DWORD WINAPI		SetFakeDetectionLevel(int level) = 0;

  #// 05/27/2011, Get fake detection level
  #virtual DWORD WINAPI		GetFakeDetectionLevel(int *level) = 0;

  #// 09/09/2011, Send commands to device
  #virtual DWORD WINAPI		WriteData(unsigned char index, unsigned char data) = 0;

#end class PYSGFPLib
