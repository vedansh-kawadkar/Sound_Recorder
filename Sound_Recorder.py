import sounddevice as sd 
import soundfile as sf 
import tkinter 

def recording():
    fs = 48000
    duration = 10
    my_recording = sd.rec(frames=int(fs * duration) , samplerate=fs, channels=2)

    sd.wait()

    return sf.write('My_recording.flac', my_recording, samplerate=fs)

master = tkinter.Tk()

tkinter.Label(master=master, text='Voice Recorder :').grid(row=0, column=10, rowspan=10, columnspan=10)

button = tkinter.Button(master=master, text='Record', command=recording)
button.grid(row= 0, column=25, rowspan=15, columnspan=15)

tkinter.mainloop()