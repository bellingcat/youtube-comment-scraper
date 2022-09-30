import argparse
from collections import defaultdict
from itertools import combinations
from itertools import islice
from youtube_comment_downloader import YoutubeCommentDownloader


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
        print('Getting comments for video: ', vid_uid)
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
            print(f'Author: {author}')
            print(f'Video {vid_id1} comments: ')
            # Iterate over each comment author left on video1
            # and print first 100 chars
            for i, comment in enumerate(dict1[author]):
                print(i+1, comment['text'][:100])
            print(f'Video {vid_id2} comments: ')
            for i, comment in enumerate(dict2[author]):
                print(i+1, comment['text'][:100])

            print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='scraper.py')
    parser.add_argument('videos', nargs='+', help='List of YouTube video urls')
    args = parser.parse_args()
    find_multiple_authors(args.videos)

