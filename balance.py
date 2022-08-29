import serial, keyboard

COM = 'COM4'

s = serial.Serial(COM, timeout=1)

while True:
    stream = s.read(20).decode('utf-8').strip()
    if stream != '':
        print(stream)
        keyboard.write(stream+'\n')
