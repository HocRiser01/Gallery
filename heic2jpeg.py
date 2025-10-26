#!/usr/bin/env python3
import sys
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("❌ 需要安装 Pillow 库，请先运行：")
    print("   pip install pillow pillow-heif")
    sys.exit(1)

from pillow_heif import register_heif_opener
register_heif_opener()

def convert_heic_to_jpg(folder_path):
    folder = Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        print(f"❌ 路径无效: {folder}")
        return

    heic_files = list(folder.rglob("*.heic")) + list(folder.rglob("*.HEIC"))
    if not heic_files:
        print("⚠️  未找到 .heic 文件。")
        return

    for file_path in heic_files:
        try:
            img = Image.open(file_path)
            output_path = file_path.with_suffix(".jpg")
            img.save(output_path, "JPEG")
            print(f"✅ 已转换: {file_path.name} → {output_path.name}")
        except Exception as e:
            print(f"❌ 转换失败: {file_path.name}, 错误: {e}")

    print("\n🎉 全部转换完成！")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python heic_to_jpg.py <文件夹路径>")
    else:
        convert_heic_to_jpg(sys.argv[1])