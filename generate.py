import os

def generate_train_txt(directory, output_file):
    with open(output_file, 'w') as file:
        for root, _, files in os.walk(directory):
            for name in files:
                if name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    relative_path = os.path.join(root, name)
                    file.write(relative_path + '\n')

# 使用你的图片文件夹路径和输出文件路径
image_folder = r'data\images'
output_txt = r'data\train.txt'

generate_train_txt(image_folder, output_txt)
