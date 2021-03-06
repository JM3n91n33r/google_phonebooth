"""
Script that takes pictures with an Android phone, creates CSV,  renames picture to RMA, SN and timestamp with the use
of a scanner .
Questions or comments: juanramon@google.com
"""

import os
import csv
import time
import glob
import shutil
import string

drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
if 'G:' in drives:
    dr = 'G:\\My Drive\\RL Photobooth\\TestDrive'
    os.chdir(dr)
    cur_dir = os.getcwd()

else:
    print('****PLEASE CLOSE PROGRAM AND MAKE SURE PC IS CONNECTED TO GOOGLE FILE DRIVE SYSTEM ****')

time_ref = time.strftime('%m_%d_%y_%H_%M_%S')
info = ['RMA', 'Serial Number', 'Date', 'Time']
with open('phone_db_' + time_ref + '.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(info)


def cleanup():
    os.chdir(cur_dir)
    print('looking into folder %s ' %os.getcwd())
    print(os.getcwd())
    shutil.rmtree('Camera')


while True:

    '''Script inputs: inbound/outbound, RMA and Serial Number'''

    station = False
    while not station:
        io = input('Please select or Scan [Inbound][i] or [Outbound][o] Station: ')
        station_response = ['i', 'I', 'inbound', 'o', 'O', 'outbound']
        if io in station_response:
            station = True

    rma_in = input('Scan RMA or Work Order: ')

    scan = input('Scan IMEI: ')

    os.system('adb shell rm /sdcard/DCIM/Camera/*jpg')

    def remove_folder():
        shutil.rmtree('Camera')

    '''Android camera commands from script'''

    os.system('adb shell input keyevent KEYCODE_FOCUS')
    print('Focusing lens..')
    time.sleep(2)
    os.system('adb shell input keyevent KEYCODE_CAMERA')
    time.sleep(8)
    os.system('adb pull /sdcard/DCIM/Camera/ .')
    time.sleep(3)
    os.system('adb shell rm /sdcard/DCIM/Camera/*.jpg')

    cam_dir = os.path.dirname('Camera')

    try:
        os.stat('Camera')
    except:
        os.mkdir('Camera')

    files = glob.glob('IMG*')
    for i in files:
        shutil.copy(i, 'Camera')
    #    print(i)
        os.remove(i)
    os.chdir('Camera')
    pic = glob.glob('*jpg')
    pic = ' '.join(pic)
    station_i = ['i', 'I', 'inbound']
    station_o = ['o', 'O', 'outbound']
    time.sleep(2)
    if io in station_i:
        shutil.copy2(pic, 'WO_' + rma_in + '_IMEI_' + scan + '_inb_' + '_front_' + time.strftime('%m%d%y%H%M%S') + '.jpg')
    elif io in station_o:
        shutil.copy2(pic, 'WO_' + rma_in + '_IMEI_' + scan + '_out_' + '_front_' + time.strftime('%m%d%y%H%M%S') + '.jpg')
    file_to_go = glob.glob('IMG*')
    file_to_go = ' '.join(file_to_go)
    os.remove(file_to_go)
    file_to_move = glob.glob('*jpg')
    file_to_move = ' '.join(file_to_move)
    shutil.copy2(file_to_move, cur_dir)
    time.sleep(2)
    os.remove(file_to_move)
    os.chdir(cur_dir)

    user = input('Turn phone upsidedown and press ENTER ')

    upsidedown = False
    while not upsidedown:
         if user == '' or 'enter':
            print('SN: "%s", Work Order: "%s"' % (scan, rma_in))
            upsidedown = True

    os.system('adb shell input keyevent KEYCODE_FOCUS')
    print('Focusing lens.. ')
    time.sleep(2)
    os.system('adb shell input keyevent KEYCODE_CAMERA')
    time.sleep(8)
    os.system('adb pull /sdcard/DCIM/Camera/ .')
    time.sleep(3)
    os.system('adb shell rm /sdcard/DCIM/Camera/*.jpg')
    files = glob.glob('IMG*')
    for i in files:
        shutil.copy(i, 'Camera')
        os.remove(i)
    os.chdir('Camera')
    pic = glob.glob('IMG*')
    pic = ' '.join(pic)
    station_i = ['i', 'I', 'inbound']
    station_o = ['o', 'O', 'outbound']
    time.sleep(2)
    if io in station_i:
        shutil.copy2(pic, 'WO_' + rma_in + '_IMEI_' + scan + '_inb_' + '_back_' + time.strftime('%m%d%y%H%M%S') + '.jpg')
    elif io in station_o:
        shutil.copy2(pic, 'WO_' + rma_in + '_IMEI_' + scan + '_out_' + '_back_' + time.strftime('%m%d%y%H%M%S') + '.jpg')
    file_to_go = glob.glob('IMG*')
    file_to_go = ' '.join(file_to_go)
    os.remove(file_to_go)
    file_to_move = glob.glob('*jpg')
    file_to_move = ' '.join(file_to_move)
    shutil.copy2(file_to_move, cur_dir)
    time.sleep(2)
    os.remove(file_to_move)
    os.chdir(cur_dir)
    remove_folder()

    items = [rma_in, scan, time.strftime('%m/%d/%y/'), time.strftime ('%H:%M:%S')]
    with open('phone_db_' + time_ref + '.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(items)

    print(80*'-')
    print(' ')
    print(80*'-')



