AUTHOR = 'holden'
SITENAME = "hldn.io"
SITEURL = 'https://hldn.io'
SITETITLE = "hldn.io"
SITESUBTITLE = "holden's place on the internet"
SITEDESCRIPTION = "holden writes things here"
FAVICON = "/images/favicon.ico"
SITELOGO = SITEURL + "/images/holden_avatar.png"

MAIN_MENU = True
HOME_HIDE_TAGS = True
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

THEME = "/Users/holden/pelican-themes/flex"
COPYRIGHT_YEAR = 2023
COPYRIGHT_NAME = "holden smith"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('photography portfolio', 'https://hldn.io/portfolio'),
         ('my other website', 'https://mnowls.com'),
         ('owl map', 'https://mnowls.com/owls'),
         ('aurora dashboard (WIP)', 'https://mnowls.com/aurora.html'),
         ('hldn.io - blog (you are here)', 'https://hldn.io')
         )

# Social widget
SOCIAL = (
          ('instagram', 'https://instagram.com/hldnsmith'),
          ('twitter', 'https://twitter.com/mnhldn'),
          ('facebook', 'https://facebook.com/h0lden'),
          ('github', 'https://github.com/freeze')
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
