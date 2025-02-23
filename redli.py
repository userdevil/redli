import requests
import sys
from colorama import Fore, Back, Style

class name_ban:
    def banner(self):
        c = Fore.WHITE


   print(c+"_____________________________  .____    .___ ")
   print(c+"\______   \_   _____/\______ \ |    |   |   |")
    print(c+"|       _/|    __)_  |    |  \|    |   |   |")
    print(c+"|    |   \|        \ |    `   \    |___|   |")
    print(c+"|____|_  /_______  //_______  /_______ \___|")
        print(c +"  \/        \/         \/        \/ ")   
        print(c + "    TRACKING THE END FACE OF URLs\n   ")

    def help(self):
        print('REDLI v1.0')
        about = '''Have you ever wondered: Where does this link go? 
The REDLI it allows you to see the complete path a redirected URL goes through. 
It will show you the full redirection path of URLs, shortened links, or tiny URLs.'''
        print(about)
        print('\nRequirements: Python 3, requests and colorama libraries')
        print('To install the requirements run these commands')
        print('\tUpdate: apt-get update')
        print('\tPython 3: apt-get install python3')
        print('\tRequests: pip install requests')
        print('\tcolorama: pip install colorama')
        print('\nRun the tool: redli.py --track')
        print('Commands')
        print("--track or -t  -> Track the given URL's redirection path & find its end URL.")
        print('--help or -h  -> To display helpline how to use this tool & about tool. ')
        print('\nCoded by: Mavin')

    def cmdusage(self):
        print('Invalid command-line arguments!')
        print('Commands')
        print("--track or -t  -> Track the given URL's redirection path & find its end URL.")
        print('--help or -h  -> To display helpline how to use this tool & about tool. ')

class redli:
    def __init__(self, url):
        self.url = url
    def track_url(self):
        try:
            resp = requests.get(self.url)
            if resp.history:
                print(Fore.RED + '\nYes URL is Redirected or Shorten!')
                print(Fore.RED + 'Here the following redirected chain...\n')
                for r in resp.history:
                    print(Fore.RED + '|', r.status_code, '|', r.url, '|', r.reason)
                print(Fore.WHITE + '\nEND URL :', resp.url)
                print(Fore.WHITE + 'Status Code :', resp.status_code, resp.reason)
            else:
                print(Fore.WHITE + '\nURL is Not Redirected or Shorten!')
                print(Fore.WHITE + 'END URL :', resp.url)
                print(Fore.WHITE + 'Status Code :',resp.status_code, resp.reason)
        except BaseException as be:
            print(Fore.RED + 'Tracking Failed! Check URL')
            print(be)
            exit()

if __name__=='__main__':
    intro = name_ban()
    intro.banner()
    if len(sys.argv) == 2:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            intro.help()
        elif sys.argv[1] == '--track' or sys.argv[1] == '-t':
            url = input('Enter URL to Track:')
            print('Tracking Redirection Of URL...')
            track = redli(url)
            track.track_url()
        else:
            intro.cmdusage()
    else:
        intro.cmdusage()
