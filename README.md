# Newsletter
The poly Newsletter app allows you to instantly construct an HTML file to be used as an email news letter. The app runs locally on any machine and uses Python 3.
## Setup

 - Download all files and folders.
 - Ensure all packages in requirements.txt are enabled in your python environment. 

## Use

 - Compile the articles you want featured in the newsletter in a .txt file. Each article should be specified by its poly.rpi.edu URL and should be separated by a newline. 
 - From the command line run
    python3 newsletter_builder.py \<cmd args\>
### Command Line Arguments
Through the command line you can specify 3 fields. 
 
 - Name of the input file. If not supplied defaults to 'articles.txt'
 - Name of the output file. If not supplied defaults to 'my_newsletter.txt'
 - Block types for each article. 

usage: newsletter_builder.py [-h] [-o OUTPUT_FILE] [-a ARTICLES_FILE]
						                             [-b BLOCK_TYPES [BLOCK_TYPES ...]]

optional arguments:
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
  -a ARTICLES_FILE, --article_file ARTICLES_FILE
  -b BLOCK_TYPES [BLOCK_TYPES ...], --block_types BLOCK_TYPES [BLOCK_TYPES ...]

## Block types
Block types are specified by a sequential series of integers.

 0. Top Story
 1. Middle Story Left
 2. Middle Story Right

