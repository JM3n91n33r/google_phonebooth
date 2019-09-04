import os
import time
import shutil
import glob
import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
num = range(0,len(drives))
print('choice', '-------', 'drive')
d = dict(zip(num, drives))
for i in d:
    print(i + 1 ,'------------', d[i])
selection = input('Please select network picture drive: ')
selection = int(selection) - 1
os.chdir(d[selection])
os.chdir('My Drive')
my_dir = (os.getcwd())
print('contents of "%s"' %my_dir)
files = os.listdir(my_dir)
n_files = range(0, len(files))
df = dict(zip(n_files, files))
for j in df:
    print(j + 1, '------------', df[j])
d_choice = input('PLease select the picture folder: ')
d_choice = int(d_choice) - 1
os.chdir(df[d_choice])
cur_dir = os.getcwd()
print('folder selected: %s' %cur_dir)

finished = False

def cleanup():                                      # function removes dir 'Camera' created by adb pull
    os.chdir(cur_dir)
    print('looking into folder %s ' %os.getcwd())
    print(os.getcwd())
    shutil.rmtree('Camera')                         # command removes dir 'Camera' and any contents created by adb pull

while not finished:

    inout = False

    while not inout:
        io = input('for inbound type "i" or scan "inbound" for outbound type "o" or scan "outbound": ')
        io_options = ['i', 'inbound', 'o', 'outbound']
        if io in io_options:
            inout = True

    scan_complete = False

    while not scan_complete:
        answers = ['', 'y', 'Y']
        start = False
        while not start:
            scan = input('Place phone face up, scan Serial Number and press ENTER: ')
            if len(scan) != 0:
                start = True
        yesno = input('If Serial Number "%s" is correct press Enter, [y/Y] or [N/n] if need to re-scan ' % scan)
        if yesno in answers:
            scan_complete = True


    
    os.system('adb pull /sdcard/DCIM/Camera/ .')


    os.system('adb shell input keyevent KEYCODE_FOCUS')
    print('Focusing lens.. waiting 3 seconds')
    time.sleep(2)    
    os.system('adb shell input keyevent KEYCODE_CAMERA')
    time.sleep(5)
    os.system('adb pull /sdcard/DCIM/Camera/ .')
    time.sleep(3)
    os.system('adb shell rm /sdcard/DCIM/Camera/*.jpg')
    repo = os.getcwd()
    print(repo)
    os.chdir('Camera')
    pic = glob.glob('*jpg')
    pic = ' '.join(pic)
    station_i = ['i', 'I', 'inbound']
    station_o = ['o', 'O', 'outbound']
    time.sleep(2)
    if io in station_i:
        shutil.copy2(pic, scan + '_inb_' + '_front_' + time.strftime('%m%d%y%H%M%S') + '.jpg')
    elif io in station_o:
        shutil.copy2(pic, scan + '_out_' + '_front_' + time.strftime('%m%d%y%H%M%S') + '.jpg')
    file_to_go = glob.glob('IMG*')
    file_to_go = ' '.join(file_to_go)
    os.remove(file_to_go)
    print(df[d_choice])
    print(os.getcwd())
    file_to_move = glob.glob('*jpg')
    print(file_to_move)
    file_to_move = ' '.join(file_to_move)
    print(file_to_move)
    shutil.copy2(file_to_move, cur_dir)
    print(os.getcwd())
    os.remove(file_to_move)

 #   cleanup()

    user = input('Turn phone upsidedown and press ENTER ')

    upsidedown = False
    while not upsidedown:
        if user == '':
            print('Serial Number: %s' % scan)
            upsidedown = True

    os.system('adb shell input keyevent KEYCODE_FOCUS')
    print('Focusing lens.. waiting 3 seconds')
    time.sleep(2)    
    os.system('adb shell input keyevent KEYCODE_CAMERA')
    time.sleep(5)
    os.system('adb pull /sdcard/DCIM/Camera/ .')
    time.sleep(3)
    os.system('adb shell rm /sdcard/DCIM/Camera/*.jpg')
    repo = os.getcwd()
    print(repo)
    os.chdir('Camera')
    pic = glob.glob('*jpg')
    pic = ' '.join(pic)
    station_i = ['i', 'I', 'inbound']
    station_o = ['o', 'O', 'outbound']
    time.sleep(2)
    if io in station_i:
        shutil.copy2(pic, scan + '_inb_' + '_back_' + time.strftime('%m%d%y%H%M%S') + '.jpg')
    elif io in station_o:
        shutil.copy2(pic, scan + '_out_' + '_back_' + time.strftime('%m%d%y%H%M%S') + '.jpg')
    file_to_go = glob.glob('IMG*')
    file_to_go = ' '.join(file_to_go)
    os.remove(file_to_go)
    print(df[d_choice])
    print(os.getcwd())
    file_to_move = glob.glob('*jpg')
    print(file_to_move)
    file_to_move = ' '.join(file_to_move)
    print(file_to_move)
    shutil.copy2(file_to_move, cur_dir)
    print(os.getcwd())
    os.remove(file_to_move)
 #   cleanup()
    
    print(80*'*')


    
