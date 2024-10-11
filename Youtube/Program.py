# pip install pytube

import pytube 
from sys import argv
import os
os.system("cls")
# Jmeno adresaře
cesta = os.path.dirname(__file__)
print(cesta)
Downloads = cesta + "\\Downloads" 

if not os.path.exists(Downloads):
    os.mkdir(Downloads)

print(Downloads)
# url = imput("url")
# print(argv)
# url = argv[1]
# url = "https://www.youtube.com/watch?v=_G9lKpfbk_8&ab_channel=KnihyDobrovsk%C3%BD"
url = "https://www.youtube.com/watch?v=v0-yVAdtd-0&ab_channel=KnihyDobrovsk%C3%BD"

urlchannel = "https://www.youtube.com/channel/UCwwoOKNIs-1xwV_AqUkVEPg"
urlchannel = "https://www.youtube.com/channel/UCX9mTbVpUlqhKsqscmkKGCQ"
channel = pytube.Channel(urlchannel)

# Získání informací o kanálu
print("Informace o kanálu:")
# informace v description nemusí existovat 
# print(f"Popis kanálu: {channel.channel_metadata['description']}")
# print(f"Počet odběratelů: {channel.subscriber_count}")
# print(f"Počet zobrazení: {channel.view_count}")
# print(f"Počet nahrávek: {channel.video_count}")

# Získání seznamu nahrávek z kanálu
print("\nSeznam videí na kanálu: " + urlchannel)
print(f"Jméno kanálu: {channel.channel_name}")
for video in channel.videos:
    try:
        print(f"- {video.title} ({video.views} zobrazení)")
    except:
        pass

# seznam = "http://www.youtube.com/@knihydobrovskycz"
seznam = "https://www.youtube.com/results?search_query=lucie+lenertova"
seznam = "https://www.youtube.com/playlist?list=PLjQgcUrQ52qkpXtCJvI7-GmPGS4gYuXUR"
seznam = "https://www.youtube.com/playlist?list=PL35IqLRAUZkxery2dpVsZSwiVTnKr-QBg"
seznam = "https://www.youtube.com/playlist?list=PLNyzSjIOf2h6z-Ock6uV2QHyr9CXJGRge"

print("\nSeznam videí na playlist: " + seznam)
c = pytube.Playlist(seznam)
for url in c.video_urls:
    print(url)
    # Tube = pytube.YouTube(url).streams.get_highest_resolution()
    # Tube.download(Downloads)
    break

print("\nPokus o seznam")
# print(c.title)
for video in c.videos: # .video_urls:
#      print(v.channel_url)
    # print(video)
    print(video.title)
    print(video.author) 
    # vv = video.streams.first()
    # Tube = pytube.YouTube(v)
    # v.streams.first().download()
    # video.streams.first().download(Downloads)
    break

    # for stream in v.streams:
        # print(f"   - {stream.resolution} | {stream.mime_type} | {stream.type}| {stream.itag}")


# p = pytube.Playlist(url)
# for video in p.videos:
    # print(video.streams)

# seznam = "https://www.youtube.com/@knihydobrovskycz"
seznam = "knihydobrovskycz"
seznam = "TotallyFashion"
seznam = "huge fat ass"
seznam = "Petr kulhanek"

c = pytube.Search(seznam)
print(len(c.results))
print("\nSeznam " + seznam)
for v in c.results:
    print(v.title)

Pole = c.results
for j in Pole:
    print("\nJedna položka")    
    print(j.title)
    # stahování Funguje
    # stream = j.streams.get_highest_resolution()
    # stream.download(Downloads)
    # Jiný pokus 
    # stream = j.streams.get_highest_resolution()
    break

# seznam = "https://www.youtube.com/@TotallyFashion"
seznam = "TotallyFashion"
seznam = "Petr kulhanek"
c = pytube.Search(seznam)
print("\n"+ seznam)
print(len(c.results))
p = c.results

print(p[1].title)

# Tube = pytube.YouTube(p[1].url)
#  stream = Tube.streams.get_highest_resolution()
# stream.download(Downloads)

# print(f'Downloading videos by: {c.channel_name}')

# url = "https://www.youtube.com/@knihydobrovskycz"
# url = "https://www.youtube.com/watch?v=v0-yVAdtd-0&ab_channel=KnihyDobrovsk%C3%BD"
url = "https://www.youtube.com/watch?v=zmjNBIGeKQw"

print("\nPokus o stahování")
Tube = pytube.YouTube(url)
print(Tube.title)
print(Tube.author)
print(Tube.keywords)
print(Tube.length)

# stream = pytube.Playlist(url)
# print(stream)

# stream = Tube.streams.get_audio_only()
# stream.download(Downloads)
print("\nCreate stream")
# stream = Tube.streams
# for s in stream:
#     print(s)

print("\nCreate stream")
# stream.get_highest_resolution().download(Downloads)

# stream = Tube.streams.get_lowest_resolution()
# stream.download(Downloads)