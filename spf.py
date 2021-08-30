# install dnspython or dnspython3 to use dns
import sys
from dns import resolver


def banner():
    print('Usage: #py spf.py domain.com')
    print('[+] Made by b3h0x')


def getSpfResponse():
    response = [x for x in resolver.query(sys.argv[-1], 'txt')]
    return response


def treatResponse():
    for i in getSpfResponse():
        if str(i).count('~all') or str(i).count('all'):
            return True
    return False


if(len(sys.argv) > 1):
    print('[+] Is vulnerable.' if treatResponse() else '[-] Not vulnerable.')
    opt = str(input('Want see? (y/n): '))
    if opt == "y":
        for line in [x for x in resolver.query(sys.argv[-1], 'txt')]:
            print(line)
else:
    banner()
