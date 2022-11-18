import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='youtube-comment-scraper',
    version='2022.1.2.0',
    author='Richard Mwewa',
    author_email='rly0nheart@duck.com',
    packages=['youtube_comment_scraper'],
    description='YouTube Comment Scraper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rly0nheart/youtube-comment-scraper',
    license='GNU General Public License v3 (GPLv3)',
    install_requires=['requests', 'youtube-comment-downloader'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
        ],
    entry_points={
        'console_scripts': [
            'youtube_comment_scraper=youtube_comment_scraper.main:main',
        ]
    },
)
