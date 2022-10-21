"""
IMPORTANT

The script is still under development and may have unexpected 
behavior and results, this project is for learning purposes only, 
use it with care.
"""


from datetime import datetime
import os


def header(file):
    a = os.getlogin()
    b , c , d , e , f = os.uname()

    #CLEANING FILE
    with open( f'{file}', 'w+') as update_file:
        pass

    with open( f'{file}', 'a+') as update_file :
        update_file.write('--------------------------------------------------------------------------\n')
        update_file.write(f'User: {a}\n')
        update_file.write(f'Operating system name: {b}\n')
        update_file.write(f'Name of machine on network: {c}\n')
        update_file.write(f'Operating system release: {d}\n')
        update_file.write(f'Operating system version: {e}\n')
        update_file.write(f'Hardware identifier: {f}\n')
        update_file.write(f'Start date and time: {datetime.now()}\n')
        update_file.write('--------------------------------------------------------------------------\n')



def report(file,status1, status2, origin,destiny):
    with open( f'{file}', 'a+') as update_file :
        update_file.write(f'''
    Date and time: {datetime.now()} 
    Process status: {status1} Error: {status2}     
    {origin}     ========= FOR ===========>     {destiny}
    \n''' )
        



