from pytube import YouTube
from django import redirect
import os
url = "https://www.youtube.com/watch?v=7KwD-dz7Scg"

video_source = YouTube(url)
try:
    if os.name == "nt":
       DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
    else:  # PORT: For *Nix systems
       DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"

    video = YouTube(url).streams.get_highest_resolution().download(DOWNLOAD_FOLDER)
    #video_source.streams.filter(progressive=True,file_extension="mp4").first().download(output_path="Downloads")
except Exception as e:
    print("e")
    print("Not download succcessfully")

def downloading(request):
    url = request.POST.get("video","")
    print(url)
    try:
      if os.name == "nt":
       DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
      else:  # PORT: For *Nix systems
       DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"
      video = YouTube(url).streams.get_highest_resolution().download(DOWNLOAD_FOLDER)
    #video_source.streams.filter(progressive=True,file_extension="mp4").first().download(output_path="Downloads")
    except Exception as e:
       print(e)
       print("Not download succcessfully")
    return redirect("/")



    val = {"down":"Videos is downloading...."}
    try:
      if os.name == "nt":
       DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
      else:  # PORT: For *Nix systems
       DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"
      vid = YouTube(url).streams.get_highest_resolution().download(DOWNLOAD_FOLDER)
    #video_source.streams.filter(progressive=True,file_extension="mp4").first().download(output_path="Downloads")
    except Exception as e:
       print(e)
       print("Not download succcessfully")