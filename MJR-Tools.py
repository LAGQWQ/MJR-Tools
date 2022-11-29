import os
import time

os.system("clear")
print("欢迎使用MJR-Tools")
print("注意：如果您是第一次使用，请输入install安装完整版")
print("Github:https://github.com/LAGQWQ/MJR-Tools/")
print("输入 help 查询可用功能")

while True:
    shinput = input('MJR-Tools>')
    if shinput == 'help':
        print('install        安装/重装MJR-Tools完整版')
        print('tools          系统实用工具')
        print('disk           磁盘实用工具')
        print('bluetooth      蓝牙实用工具')
        print('mirror         换源')
        print('fcitx          安装中文输入法')
        print('branch         切换分支')
        print('update         下载最新版')
        print('store          商店(AUR)')
        print('debtap         deb转pkg.tar.zst')
        print('exit           退出')
    elif shinput == 'install':
        print("注意：即将安装/重装MJR-Tools完整版")
        print("输入y安装，否则输入n")
        shinput = input('[y/n]>')
        if shinput == 'y':
            os.system("clear")
            print("准备安装")
            print("正在检查软件包源码，如弹窗请全部勾选")
            os.system('sudo pacman-mirrors -i -c China -m rank')
            print("正在同步软件包")
            time.sleep(2)
            os.system("sudo pacman -Syy")
            print("正在安装相关依赖")
            time.sleep(2)
            os.system("sudo pacman -S micro cowsay paru lolcat debtap")
            print("正在安装MJR-Tools-full")
            time.sleep(2)
            os.system('mkdir MJR-Tools-full')
            os.chdir('MJR-Tools-full')
            os.system("git clone https://ghproxy.com/https://github.com/LAGQWQ/MJR-Tools.git")
            print("安装完成")
    elif shinput == 'bluetooth':
        print("-"*24)
        print("蓝牙工具箱")
        print("-"*24)
        print('install        安装蓝牙服务')
        print('disable        禁用蓝牙服务')
        print('start          启动蓝牙服务')
        print('unlock         解除蓝牙锁')
        print('bluetoothctl   启动蓝牙控制台')
        shinput = input('bluetooth>')
        if shinput == 'install':
            shinput = input('确定安装?[y/n]>')
            if shinput == 'y':
                os.system("sudo pacman -S bluez bluez-tools rfkill blueman bluedevil pulseaudio-bluetooth")
        elif shinput == 'start':
            print('蓝牙服务正在启动')
            os.system('sudo systemctl enable bluetooth.service')
            os.system('sudo systemctl start bluetooth.service')
            print('蓝牙服务已启动')
        elif shinput == 'start':
            print('蓝牙服务正在禁用')
            os.system('sudo systemctl disable bluetooth.service')
            print('蓝牙服务已禁用')
        elif shinput == 'unlock':
            os.system('sudo rfkill unblock bluetooth')
            print("蓝牙锁已解除")
        elif shinput == 'bluetoothctl':
            os.system('bluetoothctl')
    elif shinput == 'tools':
        print('-'*24)
        print('系统实用工具')
        print('-'*24)
        print('update         检查系统更新')
        print('htop           启动终端任务管理器')
        print('ps             检查当前会话运行进程')
        print('msm            打开manjaro设置')
        print('mns            打开manjaro信息设置(针对KDE)')
        shinput = input('tools>')
        if shinput == 'update':
            os.system('sudo pacman -Syyu')
        elif shinput == 'htop':
            os.system('htop')
        elif shinput == 'ps':
            os.system('ps')
        elif shinput == 'msm':
            os.system('manjaro-settings-manager')  
        elif shinput == 'mns':
            os.system('msm_kde_notifier --settings')
    elif shinput == 'disk':
        print('-'*24)
        print('磁盘实用工具')
        print('-'*24)
        print('dd             U盘刻录')
        print('ddfix          磁盘修复')
        print('df             查看已挂载分区')
        print('list           查看所有分区')
        print('cfdisk         启动cfdisk分区工具')
        shinput = input('disk>')
        if shinput == 'dd':
            shinput = input('确定要刻录吗?[y/n]')
            if shinput == 'y':
                print('请输入您的镜像地址')
                ddif = input('>')
                print('请输入您要刻录的分区。')
                print('如果不明白 请回到主页执行df')
                print('一般/dev/sdb /dev/sda /dev/adb是U盘分区')
                ddof = input('>')
                input('您确定要继续刻录吗?将会丢失所有分区和文件 继续按回车')
                input('最后再询问您是否备份好所有文件 继续刻录会丢失所有文件! 继续按回车')
                print('正在刻录')
                os.system("sudo dd if=%s of=%s status=progress bs=4M"%(ddif,ddof))
                print('刻录完毕')
        elif shinput == 'ddfix':
            shinput = input('确定要修复吗?修复时间较长[y/n]')
            if shinput == 'y':
                print('请输入要修复的分区 该分区必须被挂载')
                print('如果不明白 请回到主页执行df')
                print('一般/dev/sdb /dev/sda /dev/adb是U盘分区')
                ddiof = input('>')
                input('确定修复吗 回车继续')
                os.system("sudo dd if=%s of=%s status=progress"%(ddiof))
                print('刻录完毕')
        elif shinput == 'df':
            os.system("sudo df")
        elif shinput == 'list':
            os.system("sudo fdisk -l")
        elif shinput == 'cfdisk':
            os.system("sudo cfdisk")
    elif shinput == 'mirror':
        print("自动换源[a]")
        print("手动换源[m]")
        print("取消[c]")       
        shinput = input('[a/m/c]>')
        if shinput == 'a':
            print("请稍后")
            time.sleep(2)
            os.system("sudo pacman-mirrors -i -c China -m rank")
            os.system("sudo pacman -Syy")
        elif shinput == 'm':
            print('您想编辑mirrorlist[m]还是pacman.conf[c]')        
            shinput = input('[m/c]>')
            if shinput == 'm':
                os.system('micro /etc/pacman.d/mirrorlist')
                os.system("sudo pacman -Syy")
            elif shinput == 'c':
                os.system('micro /etc/pacman.conf')
                os.system("sudo pacman -Syy")
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
            print("-"*24)
            print('安装完毕 请注销以使用')
        elif shinput == 'n':
            pass
    elif shinput == 'branch':
        print('输入你想切换的分支')
        print('stable[s]')
        print('testing[t]')
        print('unstable[u]')
        print('取消[c]')
        shinput = input('[s/t/u/c]>')
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
            os.system('git clone https://github.com/LAGQWQ/MJR-Tools.git')  
    elif shinput == 'store':
        print('-'*24)
        print('Edge Stable        [e]')     
        print('wine               [w]')
        print('debtap             [d]')
        print('icalingua++        [i]')
        print('neofetch           [n]')
        print('安装本地软件包       [l]')
        print('卸载已经安装的软件包  [r]') 
        shinput = input('请输入>')
        if shinput == 'd': 
            print('-'*24)
            print('名称:debtap')
            print('描述:.deb转.zst工具')
            print('-'*24)
            input('回车确定安装')
            os.system("mkdir debtap")
            os.chdir("debtap")
            os.system("wget https://aur.archlinux.org/cgit/aur.git/snapshot/debtap.tar.gz")
            os.system("tar -zxvf debtap.tar.gz")
            os.chdir("debtap")
            os.system("makepkg")
            print("编译成功")
            print('由于部分原因，自动安装软件包已失效。请手动安装软件包')
        elif shinput == 'w':
            print('-'*24)
            print('名称:wine')
            print('描述:在Manjaro上运行Windows')
            print('-'*24)
            input('回车确定安装')
            os.system("sudo pacman -S wine")    
            print('安装完毕')
        elif shinput == 'e':
            print('-'*24)
            print('名称:Edge-Stable')
            print('描述:由美国微软公司研发的，基于Chromium的浏览器')
            print('-'*24)
            input('回车确定安装')
            os.system("mkdir edge-on-arch")
            os.chdir("edge-on-arch")
            os.system("wget https://aur.archlinux.org/cgit/aur.git/snapshot/microsoft-edge-stable-bin.tar.gz")
            os.system("tar -zxvf microsoft-edge-stable-bin.tar.gz")
            os.chdir("microsoft-edge-stable-bin")
            os.system("makepkg") 
            print("编译成功")
            print('由于部分原因，自动安装软件包已失效。请手动安装软件包')
        elif shinput == 'i':
            print('-'*24)
            print('名称:icalingua++')
            print('描述:Linux QQ的替代品')
            print('-'*24)
            input('回车确定安装')
            print('您是想要从Github直接下载[g]还是加速下载[p]？')
            print('由于网络特殊性，部分用户可能无法下载或过慢，推荐使用加速下载')
            shinput = input('[g/p]>')
            if shinput == 'g':
                os.system('wget https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v2.7.7/icalingua++-2.7.7-2-x86_64.pkg.tar.zst')
                os.system('sudo pacman -U icalingua++-2.7.7-2-x86_64.pkg.tar.zst')
                print('安装完毕')
            elif shinput == 'p':
                os.system('wget https://ghproxy.com/https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v2.7.7/icalingua++-2.7.7-2-x86_64.pkg.tar.zst')
                os.system('sudo pacman -U icalingua++-2.7.7-2-x86_64.pkg.tar.zst')
                print('安装完毕')
        elif shinput == 'n':
            print('-'*24)
            print('名称:neofetch')
            print('描述:查看电脑信息')
            print('-'*24)
            input('回车确定安装')
            os.system("sudo pacman -S neofetch")    
            print('安装完毕')
        elif shinput == 'l':
            local = input("输入路径>")
            os.system('sudo pacman -U '+local)
            print("安装完毕")
        elif shinput == 'r':
            shinput = input('普通删除[a]还是强制删除[b]还是删除目录[c]?[a/b/c]>')
            if shinput == 'a':
                print("输入你要删除的软件")
                remove = input("")
                os.system("sudo pacman -R "+remove)
            elif shinput == 'b':
                print('警告：强制删除是危险行为')
                print("输入你要删除的软件")
                removesc = input("sudo pacman -Rsc "+removesc)
                os.system(""+removesc)   
            elif shinput == 'c':
                print('警告：删除目录是危险行为')
                print("输入你要删除的目录")
                dele = input("")
                os.system("sudo rm -rf"+dele)  
    elif shinput == 'debtap':
        print("debtap首次运行需要更新")
        print("install      安装/修复debtap")
        print("update       更新debtap")    
        print("remove       卸载debtap")
        print("start        启动debtap")
        shinput = input('debtap>')
        if shinput == 'install':
            input('回车以继续')
            os.system("mkdir debtap")
            os.chdir("debtap")
            os.system("wget https://aur.archlinux.org/cgit/aur.git/snapshot/debtap.tar.gz")
            os.system("tar -zxvf debtap.tar.gz")
            os.chdir("debtap")
            os.system("makepkg")
            os.system("sudo pacman -U debtap.pkg.tar.zst")
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
        elif shinput == 'start':
            print('您想使用静默模式[q]还是普通模式[p]?(推荐使用静默模式)')
            shinput = input('请输入>')
            if shinput == 'q':
                print('输入软件包地址')
                debtap = input('>')
                os.system('sudo debtap -Q '+debtap)
            elif shinput == 'p':
                print('输入软件包地址')
                debtap = input('>')
                os.system('sudo debtap '+debtap)
    elif shinput == 'dd':
        shinput = input('确定要刻录吗?[y/n]')
        if shinput == 'y':
             print('请输入您的镜像地址')
             ddif = input('>')
             print('请输入您要刻录的分区。')
             print('如果不明白 请回到主页执行df')
             print('一般/dev/sdb /dev/sda /dev/adb是U盘分区')
             ddof = input('>')
             input('您确定要继续刻录吗?将会丢失所有分区和文件 继续按回车')
             input('最后再询问您是否备份好所有文件 继续刻录会丢失所有文件! 继续按回车')
             print('正在刻录')
             os.system("sudo dd if=%s of=%s status=progress bs=4M"%(ddif,ddof))
             print('刻录完毕')
    elif shinput == 'ddfix':
        shinput = input('确定要修复吗?修复时间较长[y/n]')
        if shinput == 'y':
             print('请输入要修复的分区 该分区必须被挂载')
             print('如果不明白 请回到主页执行df')
             print('一般/dev/sdb /dev/sda /dev/adb是U盘分区')
             ddiof = input('>')
             input('确定修复吗 回车继续')
             os.system("sudo dd if=%s of=%s status=progress"%(ddiof))
             print('刻录完毕')
    elif shinput == 'clear':
        os.system('clear')
    elif shinput == 'df':
        os.system('df')
    elif shinput == 'exit':
        os.system('echo 再见 | cowsay')    
        exit()
    elif shinput == 'msm':
        os.system('manjaro-settings-manager')  
    elif shinput == 'mns':
        os.system('msm_kde_notifier --settings')
    else:
        print("'"+shinput+"'"+' 不是可运行的命令')
 
