import tqdm
import requests
import argparse
from collections import defaultdict
from itertools import combinations
from itertools import islice
from youtube_comment_downloader import YoutubeCommentDownloader


program_version_number = '2022.1.0.0'
update_check_endpoint = "https://api.github.com/repos/rly0nheart/YouTube-Comment-Scraper/releases/latest"

def notice():
    notice_msg = f"""
    YouTube-Comment-Scraper {program_version_number} Copyright (C) 2022  Richard Mwewa

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    """
    print(notice_msg)


def check_and_get_updates():
    notice()
    """
    Checks if the release tag matches the current tag in the program
    If there's a match, ignore
    """
    response = requests.get(update_check_endpoint).json()
    if response['tag_name'] == program_version_number:
        pass
    else:
        update_prompt = input(f"[?] A new release is available ({response['tag_name']}). Would you like to install it? (y/n) ")
        if update_prompt.lower() == "y":
            files_to_update = ['scraper.py', 'test_find_multiple_users.py', 'README.md', 'requirements.txt']
            for file in tqdm(files_to_update, desc=f'Updating'):
                data = requests.get(f'https://raw.githubusercontent.com/rly0nheart/YouTube-Comment-Scraper/master/{file}')
                with open(file, "wb") as f:
                    f.write(data.content)
                    f.close()
            print(f"[+] Updated: Re-run program.");exit()
        else:
            pass


def get_comment_dict(video_url, max_comments=100):
    """
    Creates a dictionary mapping comment-authors 
    to a list of their comments
    """
    downloader = YoutubeCommentDownloader()
    comment_dict = defaultdict(list)
    comments = downloader.get_comments_from_url(video_url)
    for comment in islice(comments, max_comments):
        comment_dict[comment['author']].append(comment)

    return comment_dict

def find_multiple_authors(video_urls):

    # video_dict maps the video url id to the 
    # comment dict for that video
    video_dict = {}
    for url in video_urls:
        vid_uid = url.split('=')[1].split('&')[0]
        print('[~] Getting comments for video: ', vid_uid)
        video_dict[vid_uid] = get_comment_dict(url)

    # Iterate over the possible combinations of videos
    for item1, item2 in combinations(video_dict.items(), r=2):
        # Unpack from tuple
        vid_id1, dict1 = item1
        vid_id2, dict2 = item2
        # Use set intersection to find common authors
        common_authors = dict1.keys() & dict2.keys()
        print(f'Videos: {vid_id1} & {vid_id2} have {len(common_authors)}')
        print(common_authors)
        for author in common_authors:
            print(f'[+] Author: {author}')
            print(f'[+] Video {vid_id1} comments: ')
            # Iterate over each comment author left on video1
            # and print first 100 chars
            for i, comment in enumerate(dict1[author]):
                print(i+1, comment['text'][:100])
            print(f'[+] Video {vid_id2} comments: ')
            for i, comment in enumerate(dict2[author]):
                print(i+1, comment['text'][:100])

            print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('YouTube-Comment-Scraper — by Richard Mwewa', epilog='scrapes youtube comments and checks whether a user commented on the given videos')
    parser.add_argument('videos', nargs='+', help='list of youtube video urls')
    parser.add_argument('-v', '--version', version='2022.1.0.0', action='version')
    args = parser.parse_args()
    try:
        check_and_get_updates()
        find_multiple_authors(args.videos)

    except KeyboardInterrupt:
        print('[!] Process interrupted with Ctrl+C.')
    
    except Exception as e:
        print('[!] An error occurred:', e)

