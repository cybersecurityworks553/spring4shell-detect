
import argparse
import sys
import requests
import time
from urllib.parse import urljoin

requests.packages.urllib3.disable_warnings()

def VersionCheck(url,debug=False,ver=False):
    if ver:
        print("[<>] Performing Version Detection...!\n")
        try:
            check = requests.head(url,timeout=15,allow_redirects=False, verify=False)
            if check.status_code == 200:
                if "X-Powered-By" in check.headers:
                    if check.headers['X-Powered-By'] == 'ASP.NET':
                        print("Runs on ASP.NET")
                    if 'X-AspNet-Version' in check.headers:
                        print('Version: ' + check.headers['X-AspNet-Version'])
                else:
                    print('Banner Grabbing did not work\n')
            else:
                print('Status code: ' + check.status_code + '\n Exiting!')
                exit(0)
        except:
            if debug:
                print("[-] Some error occured. Detection Failed...!")
                print("Error: " + str(e))
            else:
                print("[-] Some error occured. Detection Failed...! Use -d to print the error.\n")
            pass

def Detect(url,post=True,get=False,debug=False):
    headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "class.module.classLoader.URLs[0]=0"
    try:
        print("[<>] Testing for Spring4Shell...!\n")
        if get:
            print("Using GET Method")
            post = False
            response = requests.get(url, headers=headers, data=data,
                                 timeout=15, allow_redirects=False, verify=False)

            if response.status_code == 400:
                print("[+] Vulnerable!")
            else:
                print("[-] Not likely")
        if post:
            print("Using POST Method")
            response = requests.post(url, headers=headers, data=data,
                                 timeout=15, allow_redirects=False, verify=False)

            if response.status_code == 400:
                print("[+] Vulnerable!")
            else:
                print("[-] Not likely")
        
    
    except Exception as e:
        if debug:
            print("[-] Some error occured. Detection Failed...!")
            print("Error: " + str(e))
        else:
            print("[-] Some error occured. Detection Failed...! Use -d to print the error.\n")
        pass


def main():
    parser = argparse.ArgumentParser(description='Spring-Core Rce.')
    parser.add_argument('--file',help='File containing Form Endpoints',required=False)
    parser.add_argument('--url',help='target Form Endpoints',required=True)
    parser.add_argument('--debug',help='Print errors',action="store_true",required=False)
    parser.add_argument('--get',help='Use Get Method',action="store_true",required=False)
    parser.add_argument('--post',help='Use Post Method',action="store_true",required=False)
    parser.add_argument('--ver',help='Perform Version Detection',action="store_true",required=False)
    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        exit(0)

    if args.url:
        if not(args.get) and not(args.post):
            print('Enter Request Method..!')
            parser.print_help()
            exit(0)           
        else:
            VersionCheck(args.url,args.debug,args.ver)
            Detect(args.url,args.post,args.get,args.debug)
    if args.file:
        with open (args.file) as f:
            for i in f.readlines():
                i = i.strip()
                Detect(i,args.url,args.post,args.get,args.debug)
                VersionCheck(i,args.url,args.debug,args.ver)

if __name__ == '__main__':
    main()