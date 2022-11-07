import argparse
from youtube_comment_scraper.scraper import YouTubeCommentScraper


def create_parser():
    parser = argparse.ArgumentParser('YouTube-Comment-Scraper — by Richard Mwewa', epilog='scrapes youtube comments and checks whether a user commented on the given videos')
    parser.add_argument('videos', nargs='+', help='list of youtube video urls')
    return parser
    

def main():
    _parser = create_parser()
    args = _parser.parse_args()
    try:
        YouTubeCommentScraper().find_multiple_authors(args.videos)
    except KeyboardInterrupt:
        print("[x] Process interrupted with Ctrl+C.")

    except Exception as e:
        print("[!] An error occurred:", e)
