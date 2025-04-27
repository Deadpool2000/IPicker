from flask import Flask, render_template, request, jsonify
import json
import urllib.request
import os
import sys
import argparse

class IPAddressLocator:
    def __init__(self):
        self.R = '\033[91m'
        self.Y = '\033[93m'
        self.G = '\033[92m'
        self.CY = '\033[96m'
        self.W = '\033[97m'
        self.path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')

    # CLI Mode
    def start(self):
        os.system('clear')
        print(self.CY + """
         _ ______ _      _                
        | (_____ (_)    | |               
        | |_____) ) ____| | _ _____ ____ 
        | | ____/ |/ ___) |_/ ) ___ |/ ___)
        | | |   | ( (___| _ (| ____| |   
        |_|_|   |_|\____)_| \_)_____)_|  """ + self.Y + """v1.3""" + self.G + """
        
        
        Simple IP Address locator
        
        """ + self.R + """>>""" + self.Y + """----""" + self.CY + """ Author - Deadpool2000 """ + self.Y + """----""" + self.R + """<<""")

    def finder(self, u):
        try:
            response = urllib.request.urlopen(u)
            data = json.load(response)
            print(self.R + "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(self.Y + '\n>>>' + self.CY + ' IP address details\n ')
            print(self.G + "1) IP Address : " + self.Y, data['query'], '\n')
            print(self.G + "2) Org : " + self.Y, data['org'], '\n')
            print(self.G + "3) City : " + self.Y, data['city'], '\n')
            print(self.G + "4) Region : " + self.Y, data['regionName'], '\n')
            print(self.G + "5) Country : " + self.Y, data['country'], '\n')
            print(self.G + "6) Location\n")
            print(self.G + "\tLatitude : " + self.Y, data['lat'], '\n')
            print(self.G + "\tLongitude : " + self.Y, data['lon'], '\n')
            l = 'https://www.google.com/maps/place/' + str(data['lat']) + '+' + str(data['lon'])
            print(self.R + "\n#" + self.Y + " Google Map link : " + self.CY, l)
        except urllib.error.URLError:
            print(self.R + "\nError!" + self.Y + " Please check your internet connection!\n" + self.W)
            exit()
        except KeyError:
            print(self.R + "\nError! Invalid IP/Website Address!\n" + self.W)

    def main(self):
        u = input(self.G + "\n>>> " + self.Y + "Enter IP Address/website address:" + self.W + " ")
        if u == "":
            print(self.R + "\nEnter valid IP Address/website address!")
            self.main()
        else:
            url = 'http://ip-api.com/json/' + u
            self.finder(url)

    def main2(self):
        url = 'http://ip-api.com/json/'
        self.finder(url)

    def m3(self):
        try:
            print(self.R + """\n
    #""" + self.Y + """ Select option""" + self.G + """ >>""" + self.Y + """
    
    1)""" + self.G + """ Check your IP info""" + self.Y + """
    2)""" + self.G + """ Check other IP info""" + self.Y + """
    3)""" + self.G + """ Exit
    """)
            ch = int(input(self.CY + "Enter Your choice: " + self.W))
            if ch == 1:
                self.main2()
                self.m3()
            elif ch == 2:
                self.main()
                self.m3()
            elif ch == 3:
                print(self.Y + "Exit................" + self.W)
                sys.exit(0)
            else:
                print(self.R + "\nInvalid choice! Please try again\n")
                self.m3()
        except ValueError:
            print(self.R + "\nInvalid choice! Please try again\n")
            self.m3()


    # GUI Mode
    def run_gui(self):
        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/get_ip_details', methods=['POST'])
        def get_ip_details():
            ip_address = request.form.get('ip')
            if not ip_address:
                ip_address = ''
            url = f'http://ip-api.com/json/{ip_address}'
            try:
                response = urllib.request.urlopen(url)
                data = json.load(response)
                return jsonify({
                    'success': True,
                    'data': {
                        'ip': data.get('query', 'N/A'),
                        'org': data.get('org', 'N/A'),
                        'city': data.get('city', 'N/A'),
                        'region': data.get('regionName', 'N/A'),
                        'country': data.get('country', 'N/A'),
                        'lat': data.get('lat', 'N/A'),
                        'lon': data.get('lon', 'N/A'),
                        'map_link': f"https://www.google.com/maps/place/{data.get('lat', '')}+{data.get('lon', '')}"
                    }
                })
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)})

        app.run(debug=True, port=5000)

    def run(self):
        try:
            parser = argparse.ArgumentParser(description="IPicker - A simple IP locator tool.")
            parser.add_argument('--gui', action='store_true', help="Run in GUI mode.")
            args = parser.parse_args()

            if args.gui:
                self.run_gui()
            else:
                self.start()
                self.m3()

        except KeyboardInterrupt:
            print(self.Y + "\nInterrupted! Have a nice day :)" + self.W)

if __name__ == "__main__":
    ip_locator = IPAddressLocator()
    ip_locator.run()