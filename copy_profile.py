import os, shutil

#def mountt('sourse','folder'):
    #pass
def coppy(src, dest):
    src_f = os.listdir(src)

    if src_f:
        for file in src_f:
            try:
                shutil.copy(os.path.join(src, file), os.path.join(dest, file))
                print('Перенесено ', src + file, ' в ', dest)
            except IsADirectoryError:
                try:
                    shutil.copytree(os.path.join(src, file), os.path.join(dest, file))
                    print('Перенесена папка ', src + file, ' в ', dest)
                except FileExistsError:
                    print('папка уже сущестует, копирование остановлено')
            except PermissionError:
                print('Не удалось скопировать ', src + file, ' в ', dest, ' нет доступа')
    else:
        print('no files to copy in ', os.listdir(dest))


sourse = '/mnt/logs2/Users/'
dest = '/mnt/logs/Users/'
user = 'boyko_ab'
desktopsourse = sourse + user + '/Desktop'
desktopdest = dest + user + '/Desktop'


stikysourse = sourse + user + '/AppData/Roaming/Microsoft/Sticky Notes'
stikydest = dest + user + '/AppData/Roaming/Microsoft/Sticky Notes'

#mountt(sourse,'/mnt/logs')
#mountt(dest,'/mnt/logs2')
coppy(desktopsourse, desktopdest)
coppy(stikysourse,stikydest)




