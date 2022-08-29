import re
import requests
from bs4 import BeautifulSoup as bs
import webbrowser
from tkinter import messagebox as ms
import tkinter as tk

#BeautifulSoup
s = requests.get('https://a.xsanime.com/')
soup = bs(s.text,'lxml')

favourite_animes = ["Ousama Ranking","Kimetsu no Yaiba","Shingeki no Kyojin"]

#to hide the root tkinter window which is plank and useless
root = tk.Tk()
root.withdraw()

def get_mega_link(link):
    s2 = requests.get(link)
    soup2 = bs(s2.text,'lxml')
    links = soup2.find_all('a',{'class':'download--item'})
    for j in links:
        if re.search(r"mega.nz",str(j)):
            final_link = j['href']
            break;
    webbrowser.open(final_link)

def bring_new_episodes(current,old):
    new_episdoes = []
    for episode in current:
        episode_name= episode.find('div',{'class':'itemtype_episode_name'}).text
        if not re.search(episode_name,old):
            new_episdoes.append(episode_name)
    return new_episdoes

def favourite_episode(new_episdoes):
    favourite_episodes= new_episdoes
    for i in range(len(favourite_episodes)):
        if favourite_episodes[i] not in favourite_animes:
            favourite_episodes.pop(i)
    return favourite_episodes

          
def main(): 
    episodes = soup.find_all('div',{'class':'itemtype_episode'})
    with open(r"D:\Mohammed\Coding\Python Scripting\Youtube\Oldlist.txt",'r',encoding="utf-8") as file:
        old_episodes= file.read()

    new_episdoes=bring_new_episodes(episodes,old_episodes)
    
    for episode in favourite_episode(new_episdoes):
        if ms.askyesno("New Episode", f"{episode} episode is available, Do you wish to download it?",icon='info'):
            get_mega_link(episode.a.attrs['href'])

    with open(r"D:\Mohammed\Coding\Python Scripting\Youtube\Oldlist.txt",'w',encoding="utf-8") as file2:
        for line in new_episdoes:
            file2.write(line.find('div',{'class':'itemtype_episode_name'}).text)
            file2.write('\n')

main()

