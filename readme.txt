1.创建images文件夹，将所有图片放入该文件夹。

2.创建obj.names文件
创建txt文本，分别输入物品名称，每种占一行。另存为obj.names文件。

3.生成train.txt文件
以txt文本格式打开generate_train_txt.py文件，修改其中图片路径和输出路径为你自己文件的实际路径。随后运行脚本，生成train.txt

4.创建release文件夹，将images、obj.names、train.txt、yolo_mark.exe全部放入release文件夹。

5.运行
打开cmd，进入release文件夹，运行以下指令：yolo_mark.exe images train.txt obj.names

6.开始标注
←：代表上一张图片
→：代表下一张图片
鼠标左键拖动，进行框选目标
清除选择框，按C
数字0、1、2 分别代表物品种类
退出标记yolo_mark.exe

