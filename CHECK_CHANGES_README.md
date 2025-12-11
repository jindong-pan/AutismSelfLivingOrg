# 🌿 本地更改检查工具

`check_changes.py` 是一个帮助您检查本地网站文件更改的工具脚本。

## 🚀 快速使用

### 检查最近更改
```bash
python3 check_changes.py
```
默认检查最近1小时内的文件更改。

### 检查特定时间范围
```bash
# 检查最近30分钟
python3 check_changes.py --since 30m

# 检查最近2小时
python3 check_changes.py --since 2h
```

### 启动本地服务器
```bash
python3 check_changes.py --server
```
直接启动本地开发服务器 (http://localhost:8000)

## 📋 功能特性

- ✅ **文件更改检测**: 自动扫描 `docs/` 目录中的文件更改
- ✅ **时间过滤**: 可指定检查的时间范围
- ✅ **服务器状态检查**: 显示本地服务器是否运行
- ✅ **重要文件高亮**: 突出显示关键文件的更改
- ✅ **中文界面**: 完全中文用户界面
- ✅ **实时更新**: 立即反映最新更改

## 📊 输出示例

```
🌿 Peaceful Independence - 本地更改检查工具
==================================================
服务器状态: 🟢 运行中
服务器地址: http://localhost:8000

📁 检查 docs 目录中的最近更改...
⏰ 时间范围: 最近 60 分钟

📋 发现 6 个文件更改:
------------------------------------------------------------
 1. docs/static/styles.css     15:32:45  5分钟前    12.5KB
 2. docs/index-zh.html         15:28:12  10分钟前   8.3KB
 3. docs/index.html            15:25:33  12分钟前   7.9KB
 4. docs/static/logo.svg       15:20:15  18分钟前   2.1KB
 5. docs/static/logo-icon.svg  15:18:22  20分钟前   1.8KB
 6. docs/index-es.html         15:15:08  23分钟前   5.2KB
------------------------------------------------------------
🎉 本地服务器运行中，可以查看更改效果！
   打开浏览器访问: http://localhost:8000

🔥 重要文件更改:
   • styles.css
   • index-zh.html
   • index.html
   • logo.svg
```

## 🔧 使用场景

### 开发时检查更改
```bash
# 编辑文件后快速检查
python3 check_changes.py --since 5m
```

### 部署前确认更改
```bash
# 检查今天的所有更改
python3 check_changes.py --since 24h
```

### 启动开发环境
```bash
# 一键启动服务器
python3 check_changes.py --server
```

## 📁 检测的文件类型

脚本会检测以下类型的文件更改：
- HTML 文件 (`.html`)
- CSS 文件 (`.css`)
- JavaScript 文件 (`.js`)
- SVG 图像 (`.svg`)
- 其他静态文件

## ⚡ 性能优化

- 只扫描 `docs/` 目录，避免检查无关文件
- 使用文件修改时间进行快速过滤
- 最多显示最近20个更改文件
- 轻量级实现，无需额外依赖

## 🐛 故障排除

### 服务器未运行
```
服务器状态: 🔴 未运行
```
**解决方案**: 运行 `python3 check_changes.py --server`

### 没有检测到更改
```
✅ 没有检测到文件更改
```
**解决方案**: 检查时间范围参数，或确认文件已保存

### 权限错误
某些文件可能因权限问题无法访问，脚本会自动跳过这些文件。

## 🤝 贡献

如需改进此工具，请修改 `check_changes.py` 文件并测试功能。
