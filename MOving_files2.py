import os
import time
import re
import datetime
import shutil
import re

folder_to_track = r"D:\Download"


anime_destination = r"D:\Download\Anime"
education_destination = r"D:\Download\PDFs"
setup_destination = r"D:\Download\Setup"
Podcasts_destination = r"D:\Download\Podcasts"
Other_destination =r"D:\Download\Other"
compressed_destination = r'D:\Download\Zip Files'
lecture_destination = r'D:\Download\Lectures'
Videos_destination = r'D:\Download\Videos'
Images_destination = r'D:\Download\Images'


Folders = [r"Anime",r"Other",r"PDFs",r"Setup",r"Podcasts",r"Zip Files",r"Lectures",r"Videos",r"Images"]

dicti={
    anime_destination:r"(.*)([Aa][Nn][Ii][Mm][Ee])(.*)(\.mp4)$",
    lecture_destination:r"(.*)(([Ll][Ee][Cc][Tt][Uu][Rr][Ee])|([Mm][Ee]{2}[Tt][Ii][Nn][Gg]))(.*)(\.mp4)$",
    education_destination:r"(\.pdf)$",
    setup_destination:r"(\.exe)$",
    Podcasts_destination:r"(\.mp3)$",
    compressed_destination:r"(.zip)$",
    Videos_destination:r"((\.mp4)$)|((\.m4a)$)",
    Images_destination:r"((\.jpg)$)|((\.png)$)|((\.jpeg)$)|((\.gif)$)"
    }


def created_from_wanted_time_or_no(filename):
    if datetime.datetime.now()>datetime.datetime.strptime(time.ctime(os.path.getctime(filename)),'%a %b %d %H:%M:%S %Y')+ datetime.timedelta(minutes=30):
        return True
    return False


def work_on_files_only(files):
    for j in Folders:
        files.remove(j)
    return files

def get_src(filename,destination):
    return destination+"/"+filename

def move_file(filename,destination):
    file = get_src(filename,folder_to_track)

    if filename in os.listdir(destination):
        os.remove(get_src(filename,destination))
        shutil.move(file,destination)
    else:
        shutil.move(file,destination) 

def choose_folder_for_file(filename):
    for i in dicti:
        if re.search(dicti[i],filename):
            move_file(filename,i)
            return None
    move_file(filename,Other_destination)



def Moving():
    files = work_on_files_only(os.listdir(folder_to_track))
    for filename in files:
        choose_folder_for_file(filename)
  


Moving()


