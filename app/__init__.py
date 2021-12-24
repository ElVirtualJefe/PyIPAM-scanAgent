# -*- encoding: utf-8 -*-
'''
Copyright (c) 2021 - ElVirtualJefe
'''

ARGUMENTS = {
    "pingScan": "-R -sP -PE -T4",
    "baseScan": "-T4 -PS21,22,80,443,3389 --open"
}

import nmap

def scanAgent():
    print(f"Hello, World!")

    scanner = nmap.PortScanner();

    print(f"Strating the try statement...")

    try:
        
        #print(scanner.command_line())

        results = scanner.scan(hosts='10.33.17.0/24',arguments=ARGUMENTS["pingScan"])
        outPing = ",".join(scanner.all_hosts())
        print(f"Output: {outPing}")

        results = scanner.scan(hosts='10.33.17.0/24',arguments=ARGUMENTS["baseScan"]+" --exclude="+outPing)
        out = ",".join(scanner.all_hosts())
        print(f"Output: {out}")

    except FileNotFoundError:
        print(f"FAILED - File Not Found!!")
    except:
        print(f"FAILED!!")

'''
def pingScan(scanner: nmap.PortScanner,scanHosts,exclude=''):
    scanner.scan(arguments='-R -sP -PE -T4 --exclude='+exclude,hosts=scanHosts)
    print(scanner.command_line())
    output = ",".join(scanner.all_hosts())
    if output == "":
        return "No Hosts..."
    else:
        return output

def baseScan(scanner: nmap.PortScanner,scanHosts,exclude=''):
    scanner.scan(arguments='-T4 --top-ports 5 --open --exclude='+exclude,hosts=scanHosts)
    print(scanner.command_line())
    output = ",".join(scanner.all_hosts())
    if output == "":
        return "No Hosts..."
    else:
        return output
'''
