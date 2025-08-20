# song-downloader
A Python Script to download songs in the best available format from Youtube. Haven't tested it in a Windows machine. So, it would be nice if somebody could do it. As of now, it works with command line arguments. Why? No apparent reason, other than that it is more convinient for me. Just provide the song names after the program name, in quotes.  
`python downloader.py "<Song1>" "<Song2>" ...` or  
`python downloader.py -i <filename>`  
where filename contains a list of song names

### Dependancies
* `urllib`: Install `urllib` module with `pip3` with this command  
`pip3 install urllib`
* BeautifulSoup: Install BeautifulSoup4 with  
`pip3 install beautifulsoup4`
* yt-dlp: Install yt-dlp with  
`pip3 install yt_dlp`
* ffmpeg: Install ffmmpeg ( on Fedora, it differs on different distributions of linux and on windows) with  
  `sudo dnf install ffmpeg `

### How to Use  
* First time users please check the next section.
* Download the downloader.py file to your system.
* Open the terminal and into the directory where the you saved the file.
* Run this command:  
`python3 downloader.py <songname>`
* Enjoy ;)

### First Time Use
* Before using the program, open it with a text editor.
* Change `~/Music/` to the path where you want the downloaded songs to be saved. And do leave a trailing '/' character. 
* Example: If you want them to be saved at `~/Music` folder, then line 6 should look like this:  
`pathToSave = "~/Music/"`  
and not  
`pathToSave = "~/Music"`
* You're good to go. Refer How to Use if there's any issue.
