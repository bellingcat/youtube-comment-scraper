# YouTube-Comment-Scraper
Scrapes youtube comments and checks whether a user commented on the given videos

# Installation
## Install with pip
```
pip install git+https://github.com/bellingcat/youtube-comment-scraper
```

## Build from source
1. Clone the repository
```
git clone https://github.com/bellingcat/youtube-comment-scraper
```
2. Move to the cloned project's directory
```
cd youtube-comment-scraper
```
3. Install the `build` package (If not already installed)
```
pip install build
```
4. Build the project
```
python -m build
```
5. Install the built package
```
pip install dist/*.whl
```

# Usage
## PyPi Package
```
youtube_comment_scraper <video_urls>
```

## Note
> Upon run, the scraper will first check for updates. If found, users will be prompted to download the updates
>> The scraper uses [Egbert Bouman's](https://github.com/egbertbouman) [YouTube-Comment-Downloader](https://github.com/egbertbouman/youtube-comment-downloader) to get the comments

# Donations
If you would like `youtube-comment-scraper` and would like to show support, you could Buy A Coffee for the developer using the button below

<a href="https://www.buymeacoffee.com/189381184" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Your support will be much appreciated!😊

