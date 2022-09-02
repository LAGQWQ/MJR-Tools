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
        print('update         下载最新版')
        print('store          商店(AUR)')
        print('debtap         deb转pkg.tar.zst')
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
    elif shinput == 'update':
        shinput = input('确定下载？[y/n]>')
        if shinput == 'y':
            print('更新...')
            time.sleep(1)
            os.system('git clone https://github.com/LAGQWQ/All-in-manjaro.git')  
    elif shinput == 'store':
        print('当前收录的软件包') 
        print('Edge Stable        [e]')     
        print('wine               [w]')
        print('debtap             [d]') 
        print('卸载已经安装的软件包  [r]') 
        shinput = input('请输入>')
        if shinput == 'd': 
            input('回车确定安装')
            os.system("mkdir debtap")
            os.chdir("debtap")
            os.system("wget https://aur.archlinux.org/cgit/aur.git/snapshot/debtap.tar.gz")
            os.system("tar -zxvf debtap.tar.gz")
            os.chdir("debtap")
            os.system("makepkg")
            print('安装完毕')
        elif shinput == 'w':
            input('回车确定安装')
            os.system("sudo pacman -S wine")    
            print('安装完毕')
        elif shinput == 'e':
            os.system("mkdir edge-on-arch")
            os.chdir("edge-on-arch")
            os.system("wget https://aur.archlinux.org/cgit/aur.git/snapshot/microsoft-edge-stable-bin.tar.gz")
            os.system("tar -zxvf microsoft-edge-stable-bin.tar.gz")
            os.chdir("microsoft-edge-stable-bin")
            os.system("makepkg") 
        elif shinput == 'r':
            shinput = input('普通删除[a]还是强制删除[b]还是删除目录[c]?[a/b/c]>')
            if shinput == 'a':
                print("输入你要删除的软件")
                remove = input("")
                os.system("sudo pacman -R "+remove)
            elif shinput == 'b':
                print("输入你要删除的软件")
                removesc = input("sudo pacman -Rsc "+removesc)
                os.system(""+removesc)   
            elif shinput == 'c':
                print('警告：删除目录是危险行为')
                print("输入你要删除的目录")
                dele = input("")
                os.system("sudo rm -rf"+dele)  
    elif shinput == 'debtap':
        print("debtap首次运行需要以sudo权限更新")
        print("install      安装/修复debtap")
        print("update       以sudo权限更新debtap")    
        print("remove       卸载debtap")
        print("i            以sudo权限启动")
        shinput = input('debtap>')
        if shinput == 'install':
            input('回车以继续')
            os.system("mkdir debtap")
            os.chdir("debtap")
            os.system("wget https://aur.archlinux.org/cgit/aur.git/snapshot/debtap.tar.gz")
            os.system("tar -zxvf debtap.tar.gz")
            os.chdir("debtap")
            os.system("makepkg")
            print('安装完毕')
        elif shinput == 'update':
            os.system("sudo debtap -u") 
            print('更新完毕')
        elif shinput == 'remove':
            print('如果自动卸载失败请手动在终端机内卸载')
            print('即将卸载...')
            time.sleep(2)
            os.system("sudo pacman -Rs debtap")
            print('完成')     
        elif shinput == 'i':
            print('输入软件包地址')
            debtap = input('')      
            os.system('sudo debtap '+debtap)   
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
 
