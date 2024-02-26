import re
import os

file_name = 'decomp'
# exract the data
with open(file_name + '.obj', 'r') as file:
    obj_data = file.read()

# 使用正则表达式匹配块的模式
pattern = r'(o\s+\S+\s+[\s\S]*?)(?=o)'

# 使用findall函数提取每个块的内容
blocks = re.findall(pattern, obj_data, flags=re.MULTILINE)

# 记录上一个块中以 'v' 开头的行数
previous_vertex_count = 0

# 遍历每个块，将其保存为单独的文件
for id, block in enumerate(blocks):
    # 获取块的内容
    block_content = block

    # 以每行为单位分割内容，并找到以 'v' 开头的行
    lines = block_content.split('\n')
    vertex_lines = [line for line in lines if line.startswith('v')]
    face_lines = [line for line in lines if line.startswith('f')]

    # 对于每个 'f' 开头的行，将每行对应的三个数字减去上一个块中以 'v' 开头的行数
    modified_face_lines = []
    for face_line in face_lines:
        # 提取行中的数字
        numbers = re.findall(r'\d+', face_line)
        modified_numbers = [str(int(number) - previous_vertex_count) for number in numbers]
        modified_line = face_line.replace(numbers[0], modified_numbers[0]).replace(numbers[1], modified_numbers[1]).replace(numbers[2], modified_numbers[2])
        modified_face_lines.append(modified_line)
        
    # 更新以 'v' 开头的行数
    previous_vertex_count += len(vertex_lines)

    # 组合新的输出
    newblock = lines[0] + '\n' + lines[1] + '\n' + '\n'.join(vertex_lines + modified_face_lines)

    # 写入块内容到单独的文件
    # 检查目录是否存在，如果不存在则创建
    directory = 'output'
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f'output/{file_name}{id}.obj', 'w+') as file:
        file.write(newblock)
