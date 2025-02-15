import os

# 定义原始图片文件夹路径
folder_path = '.'  # 替换为你的图片文件夹路径

# 获取文件夹中所有文件
files = os.listdir(folder_path)

# 遍历文件夹中的所有文件
for file_name in files:
    # 检查文件是否是 jpg 文件
    if file_name.endswith('.jpg'):
        # 如果文件名中包含空格，去掉空格
        if ' ' in file_name:
            new_name = file_name.replace(' ', '')  # 去掉空格
            # 构造源文件路径和目标文件路径
            source_file = os.path.join(folder_path, file_name)
            destination_file = os.path.join(folder_path, new_name)
            # 重命名文件
            os.rename(source_file, destination_file)
            print(f"Renamed: {file_name} -> {new_name}")
