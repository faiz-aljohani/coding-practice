
import cv2
from pyaudio import PyAudio, paInt16

cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
import pyaudio
import time
from math import log10
import audioop

audio = pyaudio.PyAudio()
WIDTH = 2
RATE = int(audio.get_default_input_device_info()['defaultSampleRate'])
DEVICE = audio.get_default_input_device_info()['index']
rms = 1
print(audio.get_default_input_device_info())

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue
while True:
    ret,frame = cap.read()
    cv2.imshow("title",frame)
    cv2.waitKey(1) 
    # if q key is pressed, exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("User pressed q, exited successfully")
        break
    stream = audio.open(format=audio.get_format_from_width(WIDTH),
                    input_device_index=DEVICE,
                    channels=1,
                    rate=RATE,
                    input=True,
                    output=False,
                    stream_callback=callback)  
    stream.start_stream() 
    #   print "recording..." if audio is detected and is above a certain 30db threshold
    
    if stream.is_active():
        db = 20 * log10(rms)
        if db > 10:
            print(f"RMS: {rms} DB: {db}") 
        # refresh every 0.3 seconds 
        time.sleep(0.3)
    # print audio as a stream of bytes in the console
    # print(stream.read(1024))    
    stream.stop_stream()
    stream.close()
cap.release()
cv2.destroyAllWindows()