#!/usr/bin/env python3
"""
Peaceful Independence - Local Markdown File Reader
读取和显示本地Markdown文件的工具

Usage:
    python3 md_reader.py <filename.md>
    python3 md_reader.py --list
    python3 md_reader.py --help
"""

import os
import sys
import markdown
import webbrowser
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time

class MarkdownReader:
    def __init__(self):
        self.project_root = Path(__file__).parent

    def list_md_files(self):
        """列出所有Markdown文件"""
        md_files = []
        for file_path in self.project_root.rglob("*.md"):
            relative_path = file_path.relative_to(self.project_root)
            md_files.append(relative_path)

        return sorted(md_files)

    def read_md_file(self, filename):
        """读取Markdown文件"""
        file_path = self.project_root / filename

        if not file_path.exists():
            print(f"❌ 文件不存在: {filename}")
            return None

        if not file_path.suffix.lower() == '.md':
            print(f"❌ 不是Markdown文件: {filename}")
            return None

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            print(f"❌ 读取文件失败: {e}")
            return None

    def convert_to_html(self, md_content, title="Markdown File"):
        """转换Markdown为HTML"""
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'codehilite'])

        html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }}
        h1 {{
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        code {{
            background-color: #f8f8f8;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #f8f8f8;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            border-left: 4px solid #3498db;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin-left: 0;
            color: #555;
            font-style: italic;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        ul, ol {{
            padding-left: 30px;
        }}
        li {{
            margin: 5px 0;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="javascript:history.back()" class="back-link">← 返回</a>
        {html_content}
    </div>
</body>
</html>"""
        return html_template

    def display_in_terminal(self, md_content, filename):
        """在终端中显示Markdown内容"""
        print(f"\n{'='*60}")
        print(f"📄 {filename}")
        print(f"{'='*60}")
        print(md_content)
        print(f"{'='*60}\n")

    def serve_html(self, html_content, filename):
        """启动本地服务器显示HTML"""
        # 创建临时HTML文件
        temp_html = self.project_root / f"_temp_{Path(filename).stem}.html"
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # 启动服务器
        def start_server():
            os.chdir(self.project_root)
            server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
            print("🌐 本地服务器已启动: http://localhost:8080")
            print(f"📄 打开: {temp_html.name}")
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                print("\n👋 服务器已停止")

        # 在后台启动服务器
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()

        # 等待一下让服务器启动
        time.sleep(1)

        # 自动打开浏览器
        try:
            webbrowser.open(f"http://localhost:8080/{temp_html.name}")
        except:
            print("❌ 无法自动打开浏览器")

        try:
            input("按 Enter 键停止服务器...")
        except KeyboardInterrupt:
            pass

        # 清理临时文件
        if temp_html.exists():
            temp_html.unlink()

def main():
    reader = MarkdownReader()

    if len(sys.argv) < 2:
        print("❌ 请提供Markdown文件名")
        print("使用方法: python3 md_reader.py <filename.md>")
        print("或: python3 md_reader.py --list")
        return

    command = sys.argv[1]

    if command == '--help' or command == '-h':
        print(__doc__)
        return

    elif command == '--list':
        print("📚 可用的Markdown文件:")
        md_files = reader.list_md_files()
        if not md_files:
            print("❌ 未找到Markdown文件")
            return

        for i, file in enumerate(md_files, 1):
            print("2d")
        return

    elif command.endswith('.md'):
        filename = command
        content = reader.read_md_file(filename)

        if content is None:
            return

        # 显示文件信息
        file_path = reader.project_root / filename
        file_size = file_path.stat().st_size
        print(f"📄 文件: {filename}")
        print(f"📏 大小: {file_size} 字节")
        print(f"📅 修改时间: {time.ctime(file_path.stat().st_mtime)}")

        # 提供选项
        print("\n选择显示方式:")
        print("1. 在终端中显示")
        print("2. 在浏览器中显示 (推荐)")
        print("3. 两者都显示")

        try:
            choice = input("请选择 (1-3): ").strip()
        except (EOFError, KeyboardInterrupt):
            choice = "1"

        title = f"Peaceful Independence - {Path(filename).stem}"

        if choice == "1":
            reader.display_in_terminal(content, filename)
        elif choice == "2":
            html_content = reader.convert_to_html(content, title)
            reader.serve_html(html_content, filename)
        elif choice == "3":
            reader.display_in_terminal(content, filename)
            html_content = reader.convert_to_html(content, title)
            reader.serve_html(html_content, filename)
        else:
            reader.display_in_terminal(content, filename)

    else:
        print(f"❌ 无效命令或文件: {command}")
        print("使用 --help 查看帮助信息")

if __name__ == "__main__":
    main()
