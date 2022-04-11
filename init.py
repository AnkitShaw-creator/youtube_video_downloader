from pytube import YouTube


link = input("Enter Link: \n")
yt = YouTube(link)



def get_resources():
    print("Thumbnail: ", yt.thumbnail_url)
    print("Title: ", yt.title)
    print("Rating: ",yt.rating)
    print("Author: ", yt.author)
    print("Age restriction:", yt.age_restricted)
    print(f"Length:{yt.length} seconds")
    
    choice= input("Want to download?(y/n)")
    return choice


def download():
    print("Available streams ->\n")
    print("|---------------------------------For video quality higher than 720p choose Dash streaming. but you would need to mix audio later----------------------------------------|")
    k=1
    for i in yt.streams:
        print(f'{k}. {i}')
        k+=1

    p = input("Enter the number or enter 'best' to download the best quality video:\n")

    if p == 'best':
        ys = yt.streams.get_highest_resolution
    else:
        ys = yt.streams[int(p)]

    location = input('Enter the location for saving the video, else the video would be saved in the desktop')

    if location == '':
        ys.download('C:\\Users\\ankit\\Desktop')
    else:
        ys.download(location.replace("\\", "\\\\"))

    print("Video was downloaded!!!")
    


if __name__ == "__main__":
    c = get_resources()

    if c == 'y':
        download()

    else:
        exit()