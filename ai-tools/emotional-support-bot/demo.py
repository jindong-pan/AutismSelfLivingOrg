#!/usr/bin/env python3
"""
情感支持聊天机器人演示脚本
Emotional Support Bot Demo Script
"""

from emotional_support_bot import EmotionalSupportBot

def demo():
    """演示情感支持聊天机器人的功能"""
    bot = EmotionalSupportBot()

    print("🤖 自闭症儿童家长情感支持聊天机器人演示")
    print("=" * 60)

    # 演示对话
    demo_messages = [
        "我今天感到很累，照顾孩子太辛苦了",
        "我觉得很孤独，没有人理解我的感受",
        "我对孩子的未来感到很焦虑",
        "谢谢你的支持，我感觉好多了",
        "我需要一些资源来帮助孩子",
        "有时候我觉得自己不够好，是个糟糕的家长"
    ]

    print("演示对话:")
    print("-" * 30)

    for i, message in enumerate(demo_messages, 1):
        print(f"\n您: {message}")
        response = bot.chat(message)
        print(f"机器人: {response}")

    print("\n" + "=" * 60)
    print("📊 对话总结:")
    summary = bot.get_conversation_summary()
    if "total_messages" in summary:
        print(f"总消息数: {summary['total_messages']}")
        print(f"检测到的常见情绪: {dict(summary['common_emotions'])}")

    print("\n🎯 功能特点:")
    print("✅ 情感识别 - 自动识别用户的情绪状态")
    print("✅ 个性化响应 - 根据情绪提供针对性支持")
    print("✅ 资源推荐 - 连接用户到相关帮助资源")
    print("✅ 危机检测 - 识别危机情况并提供紧急帮助")
    print("✅ 对话历史 - 跟踪对话以提供连续支持")

    print("\n🚀 实际使用:")
    print("运行 'python emotional_support_bot.py' 开始交互式聊天")
    print("机器人会提供24/7的情感支持和资源连接")

if __name__ == "__main__":
    demo()
