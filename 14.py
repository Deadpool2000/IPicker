import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    if path:
        print(R+"Termux detected ! some functions will not work :( ")
    def main():
        u=input(G+">>> "+Y+"Enter IP Address/website address:"+W+" ")
        url ='http://ip-api.com/json/'
        response = urllib.request.urlopen(url+u)
        data = json.load(response)
        ip=data['query']
        org=data['org']
        c=data['city']
        cont=data['country']
        reg=data['regionName']
        latt=data['lat']
        lonp=data['lon']

        print(CY+'\n>>> Your IP detail\n ')
        print("1) IP Address : ",ip,'\n')
        print("2) Org : ",org,'\n')
        print("3) City : ",c,'\n')
        print("4) Region : ",reg,'\n')
        print("5) Country : ",cont,'\n')
        print("6) Location\n")
        print("\tLattitude : ",latt,'\n')
        print("\tLongitude : ",lonp,'\n')
        http='https://'
        l='www.google.com/maps/place/'+str(latt)+'+'+str(lonp)
        print("Google Map link : ",http+l)
        path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
        if path:
            link='am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity -d "'+str(l)+'" --activity-clear-task'
            pr=input("Open link in browser? (y|n): ")
            if pr=="y":
                os.system(str(link))
            elif pr=="n":
                print("\nCheck another IP or exit using Ctrl + C\n\n")
                main()

            else:
                print("\nInvalid choice! Please try again\n")
                main()
        else:
            pr=input("Open link in browser? (y|n): ")
            if pr=="y":
                webbrowser.open(http+l,new=0)
            elif pr=="n":
                print("\nCheck another IP or exit using Ctrl + C\n\n")
                main()

            else:
                print("\nInvalid choice! Please try again\n")
                main()
    def main2():
        url ='http://ip-api.com/json/'
        response = urllib.request.urlopen(url)
        data = json.load(response)

        ip=data['query']
        org=data['org']
        c=data['city']
        cont=data['country']
        reg=data['regionName']
        latt=data['lat']
        lonp=data['lon']

        print(CY+'\n>>> Your IP detail\n ')
        print("1) IP Address : ",ip,'\n')
        print("2) Org : ",org,'\n')
        print("3) City : ",c,'\n')
        print("4) Region : ",reg,'\n')
        print("5) Country : ",cont,'\n')
        print("6) Location\n")
        print("\tLattitude : ",latt,'\n')
        print("\tLongitude : ",lonp,'\n')
    def m3():
        print("""
Select option >>

1) Check your IP info
2) Check other IP info
3) Exit
""")
        ch=int(input("Enter Your choice: "))
        if ch==1:
            main2()
            m3()
        elif ch==2:
            main()
            m3()
        elif ch==3:
            print("Exit................")
        else:
            print("Invalid choice!")
            m3()
    m3()
except KeyboardInterrupt:
    print("\nInterrupted ! Have a nice day :)")
