import serial
import sys

import rtmidi
import time

sButton = ''
iButton = 0
iEnc = 0

midiout = rtmidi.MidiOut()
midiout.open_virtual_port("FrontPanel")


iLastButton = 0

BUTTON_1 = 8192
BUTTON_2 = 4096
BUTTON_3 = 2048
BUTTON_4 = 1024
BUTTON_5 = 512
BUTTON_6 = 256
BUTTON_7 = 128
BUTTON_8 = 64
BUTTON_ENC = 32

SHIFT_BUTTON_2 = 12288
SHIFT_BUTTON_3 = 10240
SHIFT_BUTTON_4 = 9216
SHIFT_BUTTON_5 = 8704
SHIFT_BUTTON_6 = 8448
SHIFT_BUTTON_7 = 8320
SHIFT_BUTTON_8 = 9216
SHIFT_BUTTON_ENC = 8224

NOTE_ON = 0x90
NOTE_OFF = 0x80


ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=None)

print("connected to: " + ser.portstr)

# einmal den IST Zustand abholen
ser.write('e'.encode('utf-8'))
iEnc = int(ser.readline().strip())
print('Encoder:' + str(iEnc))


tmpInput = 0
while True:
    ser.write('e'.encode('utf-8'))
    iEncNew = int(ser.readline().strip())

    if iEnc != iEncNew:
        # print('Encoder:' + str(iEnc))
        if iEncNew < iEnc:
            # print('CCW')
            midiout.send_message([0xB0, 0x01, 0x7F])
        else:
            # print('CW')
            midiout.send_message([0xB0, 0x01, 0x01])
        iEnc = iEncNew

    ser.write('b'.encode('utf-8'))
    tmpInput = ser.readline().strip()
    iButton = int(tmpInput)
    if iButton != iLastButton:
        if iButton == 0:
            # release button
            if (iLastButton == BUTTON_1):
                midiout.send_message([NOTE_OFF, 61, 0])
            elif (iLastButton == BUTTON_2):
                midiout.send_message([NOTE_OFF, 62, 0])
            elif (iLastButton == BUTTON_3):
                midiout.send_message([NOTE_OFF, 63, 0])
            elif (iLastButton == BUTTON_4):
                midiout.send_message([NOTE_OFF, 64, 0])
            elif (iLastButton == BUTTON_5):
                midiout.send_message([NOTE_OFF, 65, 0])
            elif (iLastButton == BUTTON_6):
                midiout.send_message([NOTE_OFF, 66, 0])
            elif (iLastButton == BUTTON_7):
                midiout.send_message([NOTE_OFF, 67, 0])
            elif (iLastButton == BUTTON_8):
                midiout.send_message([NOTE_OFF, 68, 0])
            elif (iLastButton == BUTTON_ENC):
                midiout.send_message([NOTE_OFF, 69, 0])
            # elif (iLastButton == SHIFT_BUTTON_1):
            #    midiout.send_message([NOTE_OFF, 70, 0])
            elif (iLastButton == SHIFT_BUTTON_2):
                midiout.send_message([NOTE_OFF, 71, 0])
            elif (iLastButton == SHIFT_BUTTON_3):
                midiout.send_message([NOTE_OFF, 72, 0])
            elif (iLastButton == SHIFT_BUTTON_4):
                midiout.send_message([NOTE_OFF, 73, 0])
            elif (iLastButton == SHIFT_BUTTON_5):
                midiout.send_message([NOTE_OFF, 74, 0])
            elif (iLastButton == SHIFT_BUTTON_6):
                midiout.send_message([NOTE_OFF, 75, 0])
            elif (iLastButton == SHIFT_BUTTON_7):
                midiout.send_message([NOTE_OFF, 76, 0])
            elif (iLastButton == SHIFT_BUTTON_8):
                midiout.send_message([NOTE_OFF, 77, 0])
            elif (iLastButton == SHIFT_BUTTON_ENC):
                midiout.send_message([NOTE_OFF, 78, 0])
            else:
                print(str(iButton))
        elif (iButton == BUTTON_1):
            midiout.send_message([NOTE_ON, 61, 127])
        elif (iButton == BUTTON_2):
            midiout.send_message([NOTE_ON, 62, 127])
        elif (iButton == BUTTON_3):
            midiout.send_message([NOTE_ON, 63, 127])
        elif (iButton == BUTTON_4):
            midiout.send_message([NOTE_ON, 64, 127])
        elif (iButton == BUTTON_5):
            midiout.send_message([NOTE_ON, 65, 127])
        elif (iButton == BUTTON_6):
            midiout.send_message([NOTE_ON, 66, 127])
        elif (iButton == BUTTON_7):
            midiout.send_message([NOTE_ON, 67, 127])
        elif (iButton == BUTTON_8):
            midiout.send_message([NOTE_ON, 68, 127])
        elif (iButton == BUTTON_ENC):
            midiout.send_message([NOTE_ON, 69, 127])
        # elif (iButton == SHIFT_BUTTON_1):
        #    midiout.send_message([NOTE_ON, 70, 127])
        elif (iButton == SHIFT_BUTTON_2):
            midiout.send_message([NOTE_ON, 71, 127])
        elif (iButton == SHIFT_BUTTON_3):
            midiout.send_message([NOTE_ON, 72, 127])
        elif (iButton == SHIFT_BUTTON_4):
            midiout.send_message([NOTE_ON, 73, 127])
        elif (iButton == SHIFT_BUTTON_5):
            midiout.send_message([NOTE_ON, 74, 127])
        elif (iButton == SHIFT_BUTTON_6):
            midiout.send_message([NOTE_ON, 75, 127])
        elif (iButton == SHIFT_BUTTON_7):
            midiout.send_message([NOTE_ON, 76, 127])
        elif (iButton == SHIFT_BUTTON_8):
            midiout.send_message([NOTE_ON, 77, 127])
        elif (iButton == SHIFT_BUTTON_ENC):
            midiout.send_message([NOTE_ON, 78, 127])
        else:
            print(str(iButton))
        iLastButton = iButton

# ser.close()
