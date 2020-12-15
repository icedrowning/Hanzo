一、Jenkins的安装 & 卸载
1.安装
使用brew安装
##brew install jenkins

通过homedrew安装后jenkins安装好后所在的位置：

实际安装位置：/usr/local/Cellar/jenkins/

配置文件所在位置：/usr/local/opt/jenkins/

工作空间位置：/Users/用户/.jenkins

进入工作空间位置：cd ~/.jenkins

2.卸载
使用brew卸载
##brew uninstall jenkins

二、Jenkins的启动 & 重启

启动
##brew services start jenkins

重启
##brew services restart jenkins

启动后在浏览器访问:localhost:8080即可
