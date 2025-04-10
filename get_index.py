import os
from natsort import natsorted  # 自然排序库

def extract_ordered_filenames(src_dirs, output_dir):
    """
    保持文件顺序提取文件名（需安装natsort库）
    :param src_dirs: 源目录字典，格式为 {'train': 'path1', 'val': 'path2', 'test': 'path3'}
    :param output_dir: 输出目录路径
    """
    # 创建输出目录（支持多级目录创建）
    os.makedirs(output_dir, exist_ok=True)
    
    for split_name, src_path in src_dirs.items():
        output_file = os.path.join(output_dir, f"{split_name}.txt")
        
        if not os.path.exists(src_path):
            print(f"警告：源目录 {src_path} 不存在，跳过处理")
            continue
        
        # 获取自然排序后的文件名（保持数字顺序）
        filenames = []
        for filename in natsorted(os.listdir(src_path)):  # 关键修改点[6,7](@ref)
            if os.path.isfile(os.path.join(src_path, filename)):
                base_name = os.path.splitext(filename)[0]
                filenames.append(base_name)
        
        # 写入文件（保持原始顺序）
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(filenames))
        print(f"成功生成（顺序保留）：{output_file}")

if __name__ == "__main__":
    # 配置路径参数（使用原始字符串避免转义问题）
    source_dirs = {
        'train': r'C:\Users\HJW\Desktop\yolov5-7.0\temp5\train\images',
        'val': r'C:\Users\HJW\Desktop\yolov5-7.0\temp5\valid\images',
        'test': r'C:\Users\HJW\Desktop\yolov5-7.0\temp5\test\images'
    }
    output_path = r'.\dataset\ImageSets\main'
    
    # 执行提取
    extract_ordered_filenames(source_dirs, output_path)