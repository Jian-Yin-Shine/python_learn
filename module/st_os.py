import os

# os.walk(top='') 遍历指定目录的完整结构
# 返回目录结构的迭代器, (dirname 目录， dirname 目录包含的子目录, dirname 目录包含的文件)
for dirname, subdirname, filename in os.walk(top='../'):
    print(dirname, subdirname, filename)
    for file in filename:
        print(os.path.join(dirname, file))

# os.listdir('./') 返回当前目录所有文件/子目录的 列表

print('----------------------------------')

# 当前工作目录
print(os.getcwd())

# 切换当前工作目录
os.chdir('../module')
print(os.getcwd())


# 判断一个文件/ 目录是否存在
print(os.path.exists('st_os.py'))

os.chdir('../')
print(os.path.exists('module'))
os.chdir('module')
print(os.getcwd())

# 创建文件
# open('file.txt', 'w')

# with open('tmp.txt', 'w') as f:
#     pass


# 创建目录
# os.mkdir()
# os.mkdirs()

# 删除文件, 目录
# os.remove('')
# os.rmdir('')


# 复制文件 shutil.copy(src, dst) 复制了文件权限
# shutil.copy2(src, dst) 复制了文件创建时间，修改时间
# shutil.copytree(src, dst, symlinks = False, ignore) 复制文件夹，注意是否是链接形式
# shutil.move(src, dst) 将文件/目录 移动
