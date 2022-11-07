import requests
from itertools import islice
from itertools import combinations
from collections import defaultdict
from youtube_comment_downloader import YoutubeCommentDownloader


class YouTubeCommentScraper:
    def __init__(self):
        self.program_version_number = '2022.1.0.0'
        self.update_check_endpoint = "https://api.github.com/repos/rly0nheart/youtube-comment-scraper/releases/latest"
        
        
    def notice(self):
        notice_msg = f"""
        YouTube-Comment-Scraper {self.program_version_number} Copyright (C) 2022  Richard Mwewa
        
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.
        """
        print(notice_msg)

        
    def check_and_get_updates(self):
        self.notice()
        """
        Checks if the release tag matches the current tag in the program
        If there's a match, ignore
        """
        response = requests.get(self.update_check_endpoint).json()
        if response['tag_name'] == self.program_version_number:
            pass
        else:
            print(f"[!] A new release is available ({response['tag_name']}). Run 'pip install --upgrade youtube-comment-scraper' to get the updates.\n")

            
    def get_comment_dictionary(self, video_url, max_comments=100):
        """
        Creates a dictionary mapping comment-authors
        to a list of their comments
        """
        downloader = YoutubeCommentDownloader()
        comment_dictionary = defaultdict(list)
        comments = downloader.get_comments_from_url(video_url)
        for comment in islice(comments, max_comments):
            comment_dictionary[comment['author']].append(comment)
        
        return comment_dictionary

        
    def find_multiple_users(self, video_urls):
        self.check_and_get_updates()
        # video_dictionary maps the video url id to the 
        # comment dict for that video
        video_dictionary = {}
        for url in video_urls:
            video_uid = url.split('=')[1].split('&')[0]
            print('[*] Getting comments for video: ', video_uid)
            video_dictionary[video_uid] = self.get_comment_dictionary(url)
            
        # Iterate over the possible combinations of videos
        for item_1, item_2 in combinations(video_dictionary.items(), r=2):
            # Unpack from tuple
            video_id_1, dictionary_1 = item_1
            video_id_2, dictionary_2 = item_2
            # Use set intersection to find common authors
            common_authors = dictionary_1.keys() & dictionary_2.keys()
            print(f'Videos: {video_id_1} & {video_id_2} have {len(common_authors)}')
            print(common_authors)
            for author in common_authors:
                print(f'[+] Author: {author}')
                print(f'[+] Video {video_id_1} comments: ')
                # Iterate over each comment author left on video1
                # and print first 100 chars
                for count, comment in enumerate(dictionary_1[author], start=1):
                    print(count, comment['text'][:100])
                print(f'[+] Video {video_id_2} comments: ')
                for count, comment in enumerate(dictionary_2[author], start=1):
                    print(count, comment['text'][:100])
                print()
