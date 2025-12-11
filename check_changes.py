#!/usr/bin/env python3
"""
Peaceful Independence Website - Local Change Checker
检查本地网站文件更改的工具脚本

Usage:
    python3 check_changes.py
    python3 check_changes.py --since 1h
    python3 check_changes.py --server
"""

import os
import sys
import time
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent
DOCS_DIR = PROJECT_ROOT / "docs"
SERVER_PORT = 8000
SERVER_URL = f"http://localhost:{SERVER_PORT}"

def get_recent_changes(since_minutes=60):
    """获取最近修改的文件"""
    cutoff_time = time.time() - (since_minutes * 60)
    changes = []

    for file_path in DOCS_DIR.rglob("*"):
        if file_path.is_file():
            try:
                mtime = file_path.stat().st_mtime
                if mtime > cutoff_time:
                    # 计算相对路径
                    relative_path = file_path.relative_to(PROJECT_ROOT)
                    # 格式化时间
                    dt = datetime.fromtimestamp(mtime)
                    time_str = dt.strftime("%H:%M:%S")
                    # 计算分钟前
                    minutes_ago = int((time.time() - mtime) / 60)
                    time_ago = f"{minutes_ago}分钟前" if minutes_ago > 0 else "刚刚"

                    changes.append({
                        'path': relative_path,
                        'time': dt,
                        'time_str': time_str,
                        'time_ago': time_ago,
                        'size': file_path.stat().st_size
                    })
            except (OSError, PermissionError):
                continue

    # 按修改时间排序（最新的在前面）
    changes.sort(key=lambda x: x['time'], reverse=True)
    return changes

def check_server_status():
    """检查本地服务器是否运行"""
    try:
        import requests
        response = requests.get(SERVER_URL, timeout=2)
        if response.status_code == 200:
            return True, "运行中"
    except:
        pass

    # 检查是否有Python HTTP服务器进程
    try:
        result = subprocess.run(['pgrep', '-f', f'python3.*http.server.*{SERVER_PORT}'],
                              capture_output=True, text=True)
        if result.returncode == 0:
            return True, "运行中"
    except:
        pass

    return False, "未运行"

def start_server():
    """启动本地服务器"""
    print(f"🚀 启动本地服务器: {SERVER_URL}")
    print("按 Ctrl+C 停止服务器\n")

    try:
        # 切换到docs目录并启动服务器
        os.chdir(DOCS_DIR)
        subprocess.run([sys.executable, '-m', 'http.server', str(SERVER_PORT)])
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
    except Exception as e:
        print(f"❌ 启动服务器失败: {e}")

def format_file_size(size_bytes):
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return ".1f"
        size_bytes /= 1024.0
    return ".1f"

def main():
    print("🌿 Peaceful Independence - 本地更改检查工具")
    print("=" * 50)

    # 解析命令行参数
    since_minutes = 60  # 默认检查最近1小时
    check_server_only = False
    start_server_flag = False

    args = sys.argv[1:]

    # Parse arguments
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == '--server':
            start_server_flag = True
        elif arg in ['--help', '-h']:
            print(__doc__)
            return
        elif arg == '--since' and i + 1 < len(args):
            try:
                time_spec = args[i + 1]
                if time_spec.endswith('h'):
                    since_minutes = int(time_spec[:-1]) * 60
                elif time_spec.endswith('m'):
                    since_minutes = int(time_spec[:-1])
                else:
                    since_minutes = int(time_spec)
                i += 1  # Skip the next argument
            except:
                print("❌ 时间参数格式错误，使用默认值: 1小时")
        elif arg.startswith('--since'):
            try:
                time_spec = arg[7:]  # Remove '--since'
                if time_spec.endswith('h'):
                    since_minutes = int(time_spec[:-1]) * 60
                elif time_spec.endswith('m'):
                    since_minutes = int(time_spec[:-1])
                else:
                    since_minutes = int(time_spec)
            except:
                print("❌ 时间参数格式错误，使用默认值: 1小时")
        else:
            print(f"❌ 未知参数: {arg}，使用默认设置")
        i += 1

    # 检查服务器状态
    is_running, status = check_server_status()
    server_status = "🟢" if is_running else "🔴"
    print(f"服务器状态: {server_status} {status}")
    print(f"服务器地址: {SERVER_URL}")

    if start_server_flag:
        print()
        start_server()
        return

    print()
    print(f"📁 检查 {DOCS_DIR.name} 目录中的最近更改...")
    print(f"⏰ 时间范围: 最近 {since_minutes} 分钟")

    # 获取更改
    changes = get_recent_changes(since_minutes)

    if not changes:
        print("✅ 没有检测到文件更改")
        if not is_running:
            print("\n💡 提示: 运行以下命令启动本地服务器:")
            print(f"   cd {DOCS_DIR}")
            print(f"   python3 -m http.server {SERVER_PORT}")
        return

    print(f"\n📋 发现 {len(changes)} 个文件更改:")
    print("-" * 60)

    for i, change in enumerate(changes[:20], 1):  # 最多显示20个
        print("2d"
              "4.1f")

    if len(changes) > 20:
        print(f"   ... 还有 {len(changes) - 20} 个文件更改")

    print("-" * 60)

    # 总结信息
    if is_running:
        print("🎉 本地服务器运行中，可以查看更改效果！")
        print(f"   打开浏览器访问: {SERVER_URL}")
    else:
        print("💡 要查看更改，请启动本地服务器:")
        print(f"   python3 {Path(__file__).name} --server")

    # 检查是否有重要的文件更改
    important_files = ['index.html', 'index-zh.html', 'styles.css', 'logo.svg']
    important_changes = [c for c in changes if any(imp in str(c['path']) for imp in important_files)]

    if important_changes:
        print("\n🔥 重要文件更改:")
        for change in important_changes:
            print(f"   • {change['path'].name}")

if __name__ == "__main__":
    main()
