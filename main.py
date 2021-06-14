# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:54:24 2021

@author: Jim Katsanos
"""
import librosa
import os 
import fnmatch
import datetime

def proper_time(s):
    return str(datetime.timedelta(seconds=int(s))) #basically turns seconds to H:M:S

def dal():
    print("-")
tracklist = [] #a tracklist - file array
bpm = [] # a tempo array
dura = [] # a song duration array in seconds
durax = [] # a song duration array IN PROPER FORMAT
for file in os.listdir('.'): 
    if fnmatch.fnmatch(file, '*.mp3'): #if it is mp3
        tracklist.append(file) #append the name to the tracklist array


print (len(tracklist) , "songs found!") #print "x songs found!"
print ("Scanning for tempos. This might take some time...")

for i in range(len(tracklist)):
    #loading the file
    y, sr = librosa.load(tracklist[i])
    #detecting the tempo
    tempo , beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    if int(tempo) < 100:
        tempo = tempo*2
    bpm.append(int(tempo)) #append to the tempo array
    dur = librosa.get_duration(y=y , sr = sr)#detecting the duration
    dura.append(int(dur)) #append duration in seconds array
    durax.append(proper_time(dur)) #append in proper format array
    i+=1 #goes to the next track
dal()
print("RESULTS:")
dal()
print("Average estimation of duration:" , proper_time(sum(dura)/len(dura)))
print("Duration values from" , proper_time(min(dura)) , "to" , proper_time(max(dura)))
dal()
print("Average estimation of tempo:" , sum(bpm)/len(bpm))
print("Tempo values from" , int(min(bpm)), "BPM to" , int(max(bpm)) , "BPM.")
dal()