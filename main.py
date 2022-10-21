"""
IMPORTANT

The script is still under development and may have unexpected 
behavior and results, this project is for learning purposes only, 
use it with care.
"""


import re
import os
import subprocess
from package.assemble_report import header, report

PATH = os.path.dirname(os.path.realpath(__file__))
DESCRIPTIVE = PATH + '/' +'descriptive.txt'
REPORT = PATH + '/' + 'report.txt'

paths_not_found : list = []
paths_found : list = []

with open(DESCRIPTIVE ,'r') as file:
    file.seek(0)
    paths = file.read()
    filter_paths = re.findall(r'^\*\[(.*)\]\*.*\-\>.*\*\[(.*)\]\*',paths ,flags=re.MULTILINE)
    
    # Checking if all paths or files exist
    for origin , destiny in filter_paths:
        check1 = False
        check2 = False
        list_temp: list = []

        origin = origin.strip()
        destiny = destiny.strip()

        if os.path.exists(origin):
            check1 = True
        if os.path.exists(destiny):
            check2 = True

        if check1 == True and check2 == True:
            list_temp = ['Origin : Found' , origin , 'Destiny : Found', destiny]
            paths_found.append(list_temp)     

        if check1 == False or check2 == False:
            paths_not_found.append(['Origin : Not found' if check1 == False else 'Origin : Found' , origin , 
                                    'Destiny : Not found' if check2 == False else 'Destiny : Found' , destiny ])

    print('Verified and ready to backup')
    for x  in paths_found:print( x  )
    print()

    print('Could not find origin or destination path, therefore possible origin path has been removed from backup list')
    for x in paths_not_found:print( x  )
    print()


    if len(paths_found) > 0 : 
        answer1 = input('(1/2) Do you want to continue Backup with current list?(Y/N)\n')

        if answer1.upper() == 'Y':

            answer2 = input('(2/2) Want to create a report of everything that happened?(Y/N)\n')
            report_status = False
            if answer2.upper() == 'Y':
                header(REPORT)
                report_status = True

            for _ , origin_temp , _ , destiny_temp in paths_found:
                process = subprocess.run(["cp","-r","-f","--preserve",origin_temp,destiny_temp] , capture_output = True)
                
                # Data collect
                status1 = 'SUCESS' if process.returncode == 0 else 'FAILED'
                status2 = 'NO ERROR' if process.stderr == b'' else process.stderr.decode('UTF-8')
                print(status1 , status2 , origin_temp , destiny_temp  )
                if report_status == True:
                    report(REPORT,status1,status2,origin_temp,destiny_temp)
    
        else:
            print('Operation canceled')
            
    else:
        print('No path has been verified as valid, so the backup cannot take place.')
