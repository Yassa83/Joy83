###YassaTeamScript###
##GodLuck For Decoding ###
##Decoding Kids###
##Kids Script##
###YassaTeamScript###

import os

try:
    import pytube
except:
    os.system("pip install --upgrade pip")
    os.system("pip install pytube")
try:
    import shutil
except:
    os.system("pip install --upgrade pip")
    os.system("pip install shutil")
os.system("clear")
import shutil
import pytube
import webbrowser
from pytube import YouTube
from pytube import exceptions
from pytube import Playlist


print('\033[1;30m='*60)
list = ("\033[1;32m [1] For Download Video MP4 \n\033[1;34m [2] For Download Video MP3 \n\033[1;32m [3] For Download PlayList MP4  \n\033[1;34m [4] For Download PlayList MP3")
print (list)

print('\033[1;30m='*60)
ch = input("\033[1;32m Enter Your Choice Number:\033[1;34m")
print('\033[1;30m='*60)



#MP4 Download#########################################################

if ch =='1':
    
    def ved1():
        fol = input("\033[1;32m Enter a Folder Name To Save In:\033[1;34m")
        print('\033[1;30m='*60)
        
        url = input("\033[1;32m Enter a Video URL:\033[1;34m")
        print('\033[1;30m='*60)
        
        try:
            yt = YouTube(url)
        except exceptions.ExtractError:
            print ("\033[1;31m False URL")    
            
        except exceptions.VideoUnavailable:
            print("\033[1;31m Video Unavilable")
            
        except exceptions.VideoPrivate:
            print("\033[1;31m Video Is Private")
            
        except exceptions.VideoRegionBlocked:
            print("\033[1;31m Video Is Blocked")    
            
              
        else:
            print("\033[1;32m loading Streams....")
            yt=yt.streams.all()
            print('\033[1;30m='*60)
            n=-1
            for i in yt:
                n=n+1
                
                print('\033[1;34m'+str(n)+' : '+str(i))
            print('\033[1;30m='*60)
            cho = int(input("\033[1;32m Enter Your Choice:\033[1;34m"))
            print('\033[1;30m='*60)
            print("\033[1;32m Waiting Downloading....")
            chc=yt[cho].download(fol)
            
            
            print('\033[1;30m='*60)
            print("\033[1;32m Done Downloaded Video MP4....")
            print("\033[1;34m "+chc)
            print('\033[1;30m='*60)
            
           
    ved1()
    
    
#MP3 Download#########################################################

elif ch =='2':
    
    def ved2():
        fol = input("\033[1;32m Enter a Folder Name To Save In:\033[1;34m")
        print('\033[1;30m='*60)
        
        url = input("\033[1;32m Enter a Video URL:\033[1;34m")
        print('\033[1;30m='*60)
        
        try:
            yt = YouTube(url)
        except exceptions.ExtractError:
            print ("\033[1;31m False URL")    
            
        except exceptions.VideoUnavailable:
            print("\033[1;31m Video Unavilable")
            
        except exceptions.VideoPrivate:
            print("\033[1;31m Video Is Private")
            
        except exceptions.VideoRegionBlocked:
            print("\033[1;31m Video Is Blocked")    
            
              
        else:
            
          
            print("\033[1;32m Waiting Downloading....")
            yt = yt.streams.get_audio_only().download(fol)
            
            chc=yt
            
            nam = chc.splitlines()[0].replace(".mp4", "")
            
            nam = nam.splitlines()[0].replace(".webm", "")
            
            nam=shutil.move(chc,""+nam+".mp3")
            
            print('\033[1;30m='*60)
            print("\033[1;32m Done Downloaded MP3....")
            print("\033[1;34m "+nam)
            print('\033[1;30m='*60)
            
           
    ved2()


#PlayList MP4 Download#########################################################



elif ch == '3':
    def ved3():
        fol = input("\033[1;32m Enter a Folder Name To Save In:\033[1;34m")
        print('\033[1;30m='*60)
        
        url = input("\033[1;32m Enter a PlayList URL:\033[1;34m")
        print('\033[1;30m='*60)


        try:
            pl = Playlist(url)
    
        except:
            print ("\033[1;31m False URL") 
    
        else:
            n=0
            for video in pl.videos:
                n=n+1
                print(f"\033[1;32m Waiting Downloading [{n}]....")
                chc = video.streams.get_highest_resolution().download(fol)
                
                print('\033[1;30m='*60)
                
                print(f"\033[1;32m Done Downloaded Video [{n}]....")
                
                print("\033[1;34m "+chc)
                
                print('\033[1;30m='*60)
                
                
       
    ved3()

#PlayList MP3 Download#########################################################


elif ch == '4':
    def ved4():
        fol = input("\033[1;32m Enter a Folder Name To Save In:\033[1;34m")
        print('\033[1;30m='*60)

        url = input("\033[1;32m Enter a PlayList URL:\033[1;34m")
        print('\033[1;30m='*60)

        try:
            pl = Playlist(url)
    
        except:
            print ("\033[1;31m False URL") 
            
        else:
            n=0
            for video in pl.videos:
                n=n+1
                print(f"\033[1;32m Waiting Downloading [{n}]....")
                chc = video.streams.get_audio_only().download(fol)

                nam = chc.splitlines()[0].replace(".mp4", "")
                nam = nam.splitlines()[0].replace(".webm", "")
                
                nam=shutil.move(chc,""+nam+".mp3")
                
                
                print('\033[1;30m='*60)
                
                print(f"\033[1;32m Done Downloaded Audio [{n}]....")
                print("\033[1;34m "+nam)
                print('\033[1;30m='*60)
                
                
    
            
    ved4()




else:
    print("\033[1;31m False Choice")
    print('\033[1;30m='*60)
    
print('\033[1;35m Developer Click Here: \033[1;32mhttps://t.me/YassaHany')
print('\033[1;30m='*60)
print('\033[1;35m Developer Channel Click Here: \033[1;32mhttps://t.me/YassaTeam')
print('\033[1;30m='*60)
webbrowser.open("https://T.ME/YassaTeam")

###YassaTeamScript###
##GodLuck For Decoding ###
##Decoding Kids###
##Kids Script##
###YassaTeamScript###