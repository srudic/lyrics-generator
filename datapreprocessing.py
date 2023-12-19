import tensorflow as tf
import pandas as pd
import numpy as np
import os
import time

data=pd.read_csv('final_taylor_swift_lyrics.tsv',encoding='utf-8', sep='\t').drop(columns=['index'])
data.album.drop_duplicates().tolist()
k=0
Not_good_words=['Live','Genius','Demo','folklore']
TODEL=[]
for alb in data.album.drop_duplicates().tolist():
    sp=alb.split()
    if len(sp)!=0:
        for s in sp:
            if s=='Live' or s=='Genius' or s=='Demo' or s=='folklore':
                TODEL.append(k)
    k=k+1
alb=np.array(data.album.drop_duplicates().tolist())
ALB=[]
for a in range(len(alb)):
    if a not in TODEL:
        ALB.append(alb[a])
LIST_ALB_TITLE=[]
for a in ALB:
    sp=a.split()
    LIST_ALB_TITLE.append(sp)
ALB=ALB+['folklore']
ALB=pd.DataFrame(ALB).drop_duplicates(keep='first')
ALB=ALB.drop([15,12])[0].tolist()
IND=data[(data.album.isin(ALB)) & (data.lyric=='[Chorus]')].drop_duplicates(subset='song_title').index.tolist()
stop=[]
for l in data.lyric.tolist():
    if l[0]=='[':
        stop.append(1)
    else:
        stop.append(0)
data['S']=stop
CHORUSES=[]
for i in IND:
    new_d=data[i+1::]
    ss=new_d.S.tolist()
    for q in range(len(ss)):
        if ss[q]==1:
            break
    new_d=data[i+1:i+1+q]
    CHORUSES.append(new_d.lyric.tolist())
CHORUSES.index(["I didn't bring her up so they could cut her down\t8\tNone\n197\tUnreleased Songs\tBrought Up That Way \tI didn't bring her here so they could shut her out\t9\tNone\n197\tUnreleased Songs\tBrought Up That Way \tI live my whole damn life to see that little girl's smile\t10\tNone\n197\tUnreleased Songs\tBrought Up That Way \tSo why are tears pouring down that sweet face?\t11\tNone\n197\tUnreleased Songs\tBrought Up That Way \tShe wasn't brought up that way"])
CHORUSES=np.array(CHORUSES, dtype=object) 
CHORUSES=np.delete(CHORUSES,[121,])
CHORUSES=CHORUSES.tolist()
TERM=''
for c in range(len(CHORUSES)):
    for i in range(len(CHORUSES[c])):
        TERM= TERM+ CHORUSES[c][i]+ ' \n '
TERM
f = open("choruses.txt", "w", encoding="utf-8")
f.write(TERM)
f.close()