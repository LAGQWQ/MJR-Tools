import os
import time

os.system("clear")
print("欢迎使用All-in-manjaro")
print("Manjaro用户的家")
print("Github:https://github.com/LAGQWQ/All-in-manjaro/")
print("输入 help 查询可用功能")

while True:
    shinput = input('All-in-manjaro>')
    if shinput == 'help':
        print('mirror         换源')
        print('fcitx          安装中文输入法')
        print('branch         切换分支')
        print('msm            打开manjaro设置')
        print('mns            打开manjaro信息设置(针对KDE)')
        print('exit           退出')
    elif shinput == 'mirror':
        print("自动换源[a]")
        print("手动换源[m]")
        print("取消[c]")       
        shinput = input('[a/m/c]>')
        if shinput == 'a':
            print("请稍后")
            time.sleep(2)
            os.system("sudo pacman-mirrors -i -c China -m rank")
        elif shinput == 'm':
            print('您想编辑mirrorlist[m]还是pacman.conf[c]')        
            shinput = input('[m/c]>')
            if shinput == 'm':
                os.system('micro /etc/pacman.d/mirrorlist')
            elif shinput == 'c':
                os.system('micro /etc/pacman.conf')
        elif shinput == 'c':
            pass        
    elif shinput == 'fcitx':
        print('确定安装输入法吗?[y/n]')
        shinput = input('[y/n]>')
        if shinput == 'y':
            print('请稍后')
            time.sleep(2)
            os.system("sudo pacman -S fcitx5-im")
            os.system("sudo pacman -S fcitx5-chinese-addons  fcitx5-rime")
            print("-"*24)
            print("即将打开/etc/environment 请复制以下内容")
            print("GTK_IM_MODULE=fcitx")
            print("QT_IM_MODULE=fcitx")
            print("XMODIFIERS=@im=fcitx")
            print("SDL_IM_MODULE=fcitx")
            input("复制完毕后按回车 并粘贴以上内容")
            os.system("sudo nano /etc/environment")
        elif shinput == 'n':
            pass
    elif shinput == 'branch':
        print('输入你想切换的分支')
        print('stable[s]')
        print('testing[t]')
        print('unstable[u]')
        print('取消[c]')
        shinput == input('[s/t/u/c]')
        if shinput == 's':
            os.system("sudo pacman-mirrors --api --set-branch stable")
            print('切换成功')
        elif shinput == 't':
            os.system("sudo pacman-mirrors --api --set-branch testing")
            print('切换成功')
        elif shinput == 'u':
            os.system("sudo pacman-mirrors --api --set-branch unstable")
            print('切换成功')
        elif shinput == 'c':
            pass
    elif shinput == 'clear':
        os.system('clear')
    elif shinput == 'exit':
        os.system('echo 再见 | cowsay')    
        exit()
    elif shinput == 'msm':
        os.system('manjaro-settings-manager')  
    elif shinput == 'mns':
        os.system('msm_kde_notifier --settings')     
    else:
        print("'"+shinput+"'"+' 不是可运行的命令')
 