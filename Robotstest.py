import urllib.robotparser, urllib.parse

AGENT_NAME = '*'
URL_BASE = 'https://hackingu.net/robots.txt'
parser = urllib.robotparser.RobotFileParser()
parser.set_url(urllib.parse.urljoin(URL_BASE, 'robots.txt'))
parser.read()
wordlist = open('wordlist.txt','r')
rwordlist = wordlist.readlines()
PATHS = ['/wp-admin/',
         '/2018/07/18/a-seguranca-no-wordpress/',
        ]


for path in PATHS:
    print("%6s : %s" % (parser.can_fetch(AGENT_NAME, path), path))
    url = urllib.parse.urljoin(URL_BASE, path)
    print("%6s : %s" % (parser.can_fetch(AGENT_NAME, url), url))
    print()