#!/usr/bin/env python

# Mathematical hat, directly converted from Compute!, Mar 1981 issue, p. 37
# ad for the Commodore PET computer.
#
# Mike Markowski, mike.ab3ap@gmail.com
# April 2022
#
# Conversion required almost no work.  'for' loop syntax and graphics calls
# were changed and the vertical axis has to be flipped from the original
# code.

from PIL import Image, ImageDraw
from numpy import sin as SIN, sqrt as SQR # Mimic BASIC names.

                                        # Line no. in BASIC code
scrX=320; scrY=200                      # Implied from original line 20
img = Image.new('RGB', (scrX,scrY))     #  10
w = ImageDraw.Draw(img)                 #  10
fg = 'green'; bg = 'black'
#P=160; Q=100                           #  20 original
P=scrX//2; Q=scrY//2                    #  20 new, scrY for vertical flip
XP=144; XR=1.5*3.1415927                #  30
YP=56; YR=1; ZP=64                      #  40
XF=XR/XP; YF=YP/YR; ZF=XR/ZP            #  50
for ZI in range(-Q,Q):                  #  60
 if ZI>=-ZP and ZI<=ZP:                 #  70
  ZT=ZI*XP/ZP; ZZ=ZI                    #  80
  XL=int(.5+SQR(XP*XP-ZT*ZT))           #  90
  for XI in range(-XL,XL+1):            # 100
   XT=SQR(XI*XI+ZT*ZT)*XF; XX=XI        # 110
   YY=(SIN(XT)+.4*SIN(3*XT))*YF         # 120
   X1=XX+ZZ+P                           # 170
   #Y1=YY-ZZ+Q                          # 180 upside down if (0,0) upper left!
   Y1=scrY-(YY-ZZ+Q)                    # 180 new
   w.point((X1,Y1),fill=fg)             # 190
   if Y1==0:                            # 200
    continue                            # 220 kind of...
   #w.line([(X1,Y1-1),(X1,0)],fill=bg)  # 210 orig, upside down
   w.line([(X1,Y1+1),(X1,scrY)],fill=bg) # 210 new, vertical flip
img.save('hatCompute-1981.png')
img.show()
