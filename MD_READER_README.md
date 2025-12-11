# 📄 本地Markdown文件阅读器

`md_reader.py` 是一个强大的本地Markdown文件阅读和显示工具。

## 🚀 快速开始

### 安装依赖
```bash
pip3 install markdown
```

### 查看可用文件
```bash
python3 md_reader.py --list
```

### 读取Markdown文件
```bash
python3 md_reader.py README.md
python3 md_reader.py docs/SETUP.md
```

## 📋 功能特性

- ✅ **Markdown文件检测** - 自动扫描项目中的所有`.md`文件
- ✅ **多种显示方式** - 终端显示或浏览器美化显示
- ✅ **HTML转换** - 将Markdown转换为美观的HTML页面
- ✅ **本地服务器** - 自动启动本地服务器查看文件
- ✅ **文件信息** - 显示文件大小和修改时间
- ✅ **中文支持** - 完全本地化的用户界面

## 🎨 显示选项

运行脚本后，您可以选择三种显示方式：

1. **终端显示** - 在命令行中直接查看文件内容
2. **浏览器显示** - 转换为美观的HTML页面在浏览器中查看（推荐）
3. **两者都显示** - 同时在终端和浏览器中显示

## 💡 使用示例

### 查看项目文档
```bash
# 查看README
python3 md_reader.py README.md

# 查看筹款计划
python3 md_reader.py FUNDRAISING_PLAN.md

# 查看AI工具文档
python3 md_reader.py ai-tools/README.md
```

### 列出所有文档
```bash
python3 md_reader.py --list
```

输出示例：
```
📚 可用的Markdown文件:
 1. README.md
 2. FUNDRAISING_PLAN.md
 3. IMPLEMENTATION_PLAN.md
 4. OUR_PHILOSOPHY.md
 5. ai-tools/README.md
 6. ai-tools/behavior-tracker/README.md
 ...
```

## 🎨 浏览器显示特性

当选择浏览器显示时，您将获得：

- **美观的排版** - 清晰的标题、段落和列表
- **语法高亮** - 代码块的彩色语法高亮
- **表格支持** - 漂亮的表格显示
- **响应式设计** - 在手机和电脑上都完美显示
- **导航链接** - 返回上一页的链接

## 🔧 技术细节

- **依赖包**: `markdown` (用于HTML转换)
- **扩展支持**: 表格、代码块、语法高亮
- **编码支持**: UTF-8 中文显示
- **跨平台**: 支持Linux、macOS、Windows

## 📁 支持的文件类型

脚本会自动识别和处理：
- `.md` - Markdown文件
- `.markdown` - 替代的Markdown扩展名

## 🚨 故障排除

### 找不到文件
```
❌ 文件不存在: filename.md
```
**解决方案**: 使用 `--list` 查看可用文件，或检查文件路径

### 包未安装
```
ModuleNotFoundError: No module named 'markdown'
```
**解决方案**: 运行 `pip3 install markdown`

### 编码问题
如果遇到中文显示乱码，请确保文件使用UTF-8编码保存。

## 🤝 集成使用

### 与其他工具结合
```bash
# 与check_changes.py结合使用
python3 check_changes.py --since 1h  # 查看最近更改
python3 md_reader.py README.md       # 阅读更新后的文档
```

### 项目文档管理
- 使用 `--list` 查看所有项目文档
- 定期检查重要文档的更新
- 在浏览器中获得最佳阅读体验

## 📖 完整帮助

```bash
python3 md_reader.py --help
```

享受舒适的本地Markdown阅读体验！📚✨
