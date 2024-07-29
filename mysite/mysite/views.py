from django.shortcuts import render,HttpResponse,redirect
from pytube import YouTube 
import os 

def Home(request):
    print('Home sweet Home')
    yt = request.POST.get('youtube')
    print("context is {}".format(yt))
    return render(request,"Home.html")

def youtubeDownload(request):
    print("youtube Home")
    youtube = request.POST.get('youtube')
    print("youtube is {}".format(youtube))
    vid_url = request.POST.get("text")
    print("youtube url valu {}".format(vid_url))
    nuetral(vid_url,youtube)
    yt = {"youtube":"Your Youtube video is downloading!"}
    print("")
    return render(request,"download.html")

def facebookDownload(request):
   print('facebook Home')
   facebook = request.POST.get("facebook","")
   print(facebook)
   vid_url = request.POST.get("url")
   print("facebook url is {}".format(vid_url))
   print(vid_url)
   nuetral(vid_url,facebook)
   fb = {"facebook":"Your Facebook video is downloading!"}
   #return render(request,"download.html",fb)
   

def instagramDownload(request):
   print("instagram Home")
   instagram =request.POST.get("instagram","")
   vid_url = request.POST.get("url","")
   print(vid_url)
   print("insta value is {}".format(instagram))
   nuetral(vid_url,instagram)
   ins = {"instagram":"Your Instagram video is downloading!"}
   #return render(request,"download.html",ins)

def nuetral(url,type):
    return url,type
    
    
    
    



