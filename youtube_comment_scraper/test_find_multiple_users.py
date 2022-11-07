from youtube_comment_scraper.scraper import YouTubeCommentScraper
     
def test_find_multiple_users():
    # List contains, videos from Google's YouTube channel
    vids = [
        'https://www.youtube.com/watch?v=8qGV_O_y4DA',
        'https://www.youtube.com/watch?v=WSkETCRe7Ic',
        'https://www.youtube.com/watch?v=cdgQpa1pUUE'
    ]
    YouTubeCommentScraper().find_multiple_users(vids)
