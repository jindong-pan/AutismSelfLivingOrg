#!/bin/bash

# Firebase登录助手脚本
# 这个脚本会设置正确的Node.js版本并运行Firebase登录

echo "🚀 Firebase登录助手"
echo "===================="

# 加载nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# 验证Node.js版本
echo "📋 当前Node.js版本: $(node --version)"
echo "📋 当前npm版本: $(npm --version)"
echo "📋 当前Firebase CLI版本: $(firebase --version)"
echo ""

# 检查Node.js版本是否兼容
NODE_VERSION=$(node --version | sed 's/v//' | cut -d. -f1)
if [ "$NODE_VERSION" -lt 20 ]; then
    echo "❌ Node.js版本不兼容！需要 >= 20.0.0"
    echo "请先运行: nvm use 24"
    exit 1
fi

echo "✅ Node.js版本兼容"
echo ""

echo "🔐 正在启动Firebase登录..."
echo "请在浏览器中完成Google账户认证"
echo ""

# 运行Firebase登录
firebase login

echo ""
echo "🎉 Firebase登录完成！"
echo "您现在可以使用Firebase CLI命令了。"
