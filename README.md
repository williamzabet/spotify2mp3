# spotify2mp3 - Automate downloading spotify playlists to a local folder
![image](https://user-images.githubusercontent.com/48535302/219539970-36128e8b-893d-4233-954a-a5f8008d827f.png)

## Note:
Note that downloading audio from YouTube videos may be illegal depending on the circumstances, so please be aware of the laws and regulations in your area. It is illegal, and frowned-upon, to download copyrighted music from YouTube. This project is intended for downloading non-copyrighted music only. 

## Inspiration
This project gained inspiration from one of the biggest challenges people face on a daily basis: saving time. Firstly, as an avid patron of my local gym, I find myself wasting precious time skipping through songs in between sets until I find the "right" song to help me get that extra burst of energy as I am lifting weights. Not only is that time consuming, but rather unenjoyable. Pictured in the image at the top is Cristiano Ronaldo, arguably one of the best soccer players ever, walking to the dressing room before his match. When this picture was taken, the media were quick to point out Ronaldo's bold fashion statement. It wasn't his flashy sunglasses, nor was it his wacky hair-doo that gained so much attention. It was the ancient technological gizmo of the past that was clamped to his tie: A 2nd Gen iPod Shuffle. 

As soon as I saw this image, I ordered my very own shuffle off of eBay. Not because I wanted to emulate one of my role-models, but the brilliance and potential time saving that it could yield. Essentially, I thought that if I were going to listen to music in the gym, i'd benefit by using a device that not only didnt have a screen, but didn't have access to the internet. This way, whatever songs I pre-loaded on to the iPod were the ones that I were going to listen to. No ifs, ands, or buts, the days spent scouring through music streaming services for a song were over.

With this came the tedious task of creating playlists, I would have to get songs, download them, and then upload the folder into my iPod. As I finally solved a time-wasting issue, another came. So I decided to sit down, type up some code, and write a script that took in a spotify playlist, found the songs on youtube, converted them to an mp3 file, and placed them in a folder, cutting time down tremendously.

## Installation and Usage
#### What you'll need:
- python3 / jupyter Notebook
- latest version of Google Chrome
- chromedriver
- spotify account 
- youtube account

#### Python packages required:
- base64
- requests
- json
- googleapiclient.discovery
- selenium, selenium.webdriver.chrome.service
- time
- os

#### This script makes use of HTTP requests, the Spotify API, YouTube API, and finally selenium to create the local playlist. The code is all inside of the spotify2mp3 function and requires 6 parameters from the user:
##### The spotify playlist's ID:
###### Go to the playlist of your choosing, click the three dots -> share -> copy link to playlist. Afterwards make sure to only type in the characters after "https://open.spotify.com/playlist/"
##### Your spotify developer api client ID and client secret ID:
###### Log in to developer.spotify.com and create a new app. Your credentials will be displayed afterwards
##### Your YouTube api key:
###### Refer to this guide: https://blog.hubspot.com/website/how-to-get-youtube-api-key
##### The path to your chromedriver executable:
###### Open up your terminal, drag and drop the chromedriver executable and copy the path given as an output
##### The path to your folder where you want to save the mp3 files:
###### Copy the folder path where you wish for the mp3 files to be saved

Once you have everything, change the values of the 6 variables and run the script. The first part of the code will give you authorization to use the spotify API with an access token. It will then store the title and artist for each song within a playlist to an array as "[Song] by [Artist] audio. Afterwards, the youtube api will be used where it will take in the stored array (playlist), and then store the link to the first result into another array (video_links). Selenium will then go to work by using the youtube to mp3 converter website tomp3.cc. It will input each link from the (video_links) array into the submission box, click on the start -> convert -> download buttons. Lastly, the mp3 files within the folder will be renamed to remove the "tomp3.cc - " prefix. 

Note: Any youtube to mp3 converting site will work should this one cease to exist. Using the inspection tool with google chrome on such a site, you can find the unique id's for the submission box and buttons and replace their names in the driver.find_element("id", <UNIQUE ID>) functions. 

Here is a link to an example of how this works:  

