import sys
import yt_dlp

# Path where songs will be saved
pathToSave = "~/Music/"

def titleCase(s):
    """
    Convert a song name to title case but keep
    small words like 'the', 'and', 'of' lowercase.
    """
    words = s.split()
    result = words[0][0].upper() + words[0][1:]
    
    for word in words[1:]:
        if word not in ['in', 'the', 'for', 'of', 'a', 'at', 'an', 'is', 'and']:
            result += ' ' + word[0].upper() + word[1:]
        else:
            result += ' ' + word
    return result

def doStuff(song):
    print("Downloading " + titleCase(song))
    
    # yt-dlp options
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True,
        "outtmpl": pathToSave + titleCase(song) + ".%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    # ytsearch1: tells yt-dlp to grab the first YouTube result
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{song} lyrics"])

    print("Downloaded " + titleCase(song) + "\n")

def main():
    print('-------------------------------------------------------------')
    if len(sys.argv) == 3 and sys.argv[1] in ['-i', '-I']:
        for song in open(sys.argv[2]).readlines():
            doStuff(song.strip())
    else:
        for song in sys.argv[1:]:
            doStuff(song)

if __name__ == '__main__':
    main()
