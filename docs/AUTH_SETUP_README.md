# 用户认证系统设置指南

本文档介绍如何为 Peaceful Independence 网站设置完整的用户注册和登录系统。

## 🚀 概述

网站现已集成 Firebase Authentication，提供以下功能：
- 用户注册和登录
- 密码重置
- 用户仪表板
- 会话管理

## 📋 前置要求

1. **Firebase 账号**：访问 [Firebase Console](https://console.firebase.google.com/)
2. **基本 HTML/CSS/JS 知识**

## 🔧 Firebase 设置步骤

### 1. 创建 Firebase 项目

1. 访问 [Firebase Console](https://console.firebase.google.com/)
2. 点击 "创建项目" 或 "Create a project"
3. 输入项目名称：`peaceful-independence`
4. 启用 Google Analytics（可选）
5. 点击 "创建项目"

### 2. 启用 Authentication

1. 在 Firebase Console 中选择您的项目
2. 点击左侧菜单中的 "Authentication"
3. 点击 "开始使用" 或 "Get started"
4. 选择 "电子邮件/密码" 登录方式
5. 点击 "启用"
6. 在 "设置" > "授权域名" 中添加您的域名

### 3. 获取 Firebase 配置

1. 点击项目设置（齿轮图标）
2. 选择 "项目设置"
3. 滚动到 "您的应用" 部分
4. 点击 "添加应用" > "Web 应用"
5. 输入应用名称：`Peaceful Independence Website`
6. 复制生成的配置对象

### 4. 更新配置文件

编辑 `static/firebase-config.js` 文件，将配置信息替换为您的实际值：

```javascript
const firebaseConfig = {
    apiKey: "your-actual-api-key",
    authDomain: "your-project-id.firebaseapp.com",
    projectId: "your-project-id",
    storageBucket: "your-project-id.appspot.com",
    messagingSenderId: "your-actual-messaging-sender-id",
    appId: "your-actual-app-id"
};
```

## 📁 文件结构

```
docs/
├── register.html          # 注册页面
├── login.html            # 登录页面
├── dashboard.html        # 用户仪表板
├── static/
│   ├── firebase-config.js    # Firebase 配置
│   ├── styles.css           # 样式文件（已更新）
│   └── script.js            # 主脚本文件
└── AUTH_SETUP_README.md     # 本文档
```

## 🎨 页面功能

### 注册页面 (register.html)
- 邮箱和密码注册
- 表单验证
- 使用条款同意
- 成功后自动跳转到仪表板

### 登录页面 (login.html)
- 邮箱和密码登录
- 忘记密码功能
- 记住登录状态
- 自动重定向已登录用户

### 用户仪表板 (dashboard.html)
- 用户信息显示
- 支持资源链接
- 进度追踪
- 快捷操作按钮
- 账号设置

## 🔒 安全特性

- **密码要求**：至少8个字符
- **邮箱验证**：自动验证邮箱格式
- **会话管理**：自动检测登录状态
- **安全重定向**：未登录用户自动跳转到登录页面

## 🚀 部署说明

### 本地测试
1. 确保所有文件都在同一目录
2. 使用本地服务器运行（推荐使用 Live Server 扩展）
3. 测试注册、登录和仪表板功能

### 生产部署
1. 确保 Firebase 配置已更新
2. 上传所有文件到您的网站主机
3. 测试所有功能正常工作

## 🛠️ 故障排除

### 常见问题

**Q: Firebase 错误 "auth/invalid-api-key"**
A: 检查 `firebase-config.js` 中的 API 密钥是否正确

**Q: 注册后无法登录**
A: 确保在 Firebase Console 中启用了邮箱/密码认证

**Q: 页面无法加载**
A: 检查网络连接和 Firebase 配置

**Q: 用户被重定向到登录页面**
A: 这是正常行为，用户需要先登录才能访问仪表板

### 调试技巧

1. 打开浏览器开发者工具 (F12)
2. 查看 Console 标签中的错误信息
3. 检查 Network 标签中的请求状态

## 📞 支持

如果您遇到设置问题，请：

1. 检查本文档的所有步骤
2. 验证 Firebase 配置
3. 查看浏览器控制台错误
4. 联系技术支持团队

## 🔄 未来扩展

计划添加的功能：
- 社交媒体登录 (Google, Facebook)
- 双因素认证
- 用户角色管理
- 密码强度指示器
- 邮箱验证流程

## 📝 许可证

本认证系统遵循与主项目相同的许可证条款。

