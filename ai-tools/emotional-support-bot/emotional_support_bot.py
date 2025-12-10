#!/usr/bin/env python3
"""
自闭症儿童家长情感支持聊天机器人
Emotional Support Chatbot for Parents of Children with Autism

为自闭症儿童的家长提供24/7情感支持、资源推荐和实用建议
"""

import re
import random
import datetime
from typing import Dict, List, Optional
import json

class EmotionalSupportBot:
    """专门为自闭症儿童家长设计的情感支持聊天机器人"""

    def __init__(self):
        # 情感关键词映射
        self.emotion_keywords = {
            "疲惫": ["累", "疲惫", "精疲力尽", "没有力气", "筋疲力尽"],
            "焦虑": ["担心", "焦虑", "害怕", "紧张", "不安", "压力"],
            "孤独": ["孤独", "孤单", "没人理解", "无助", "一个人"],
            "沮丧": ["沮丧", "失望", "挫败", "无望", "绝望"],
            "内疚": ["内疚", "愧疚", "自责", "觉得自己不够好"],
            "愤怒": ["生气", "愤怒", "烦躁", "火大", "受不了"],
            "感激": ["感谢", "感激", "谢谢", "感动"],
            "希望": ["希望", "积极", "乐观", "信心"]
        }

        # 支持响应模板
        self.support_responses = {
            "疲惫": [
                "我理解照顾自闭症儿童会让人感到非常疲惫。您正在做一件了不起的事情！💪",
                "休息是非常重要的。您试过寻找一些临时的照顾帮助吗？",
                "照顾者也需要照顾自己。请记住，这是马拉松，不是短跑。"
            ],
            "焦虑": [
                "焦虑是正常的，每位家长都会经历。您并不孤单。🤝",
                "深呼吸，试着把大问题分解成小步骤，一步一步来。",
                "如果焦虑持续影响您的日常生活，考虑寻求专业咨询师的帮助。"
            ],
            "孤独": [
                "感到孤独是很常见的。您知道有很多家长支持团体吗？",
                "加入家长互助群，可以和其他经历相似的家长交流经验。",
                "您可以随时来这里倾诉，我们会一直倾听。❤️"
            ],
            "沮丧": [
                "进步可能很慢，但每一点小小的改善都很重要。🌱",
                "试着记录孩子的积极时刻，这能帮助您看到进展。",
                "有时候需要调整期望，给自己和孩子更多时间。"
            ],
            "内疚": [
                "您已经在尽力了，这就足够了。请对自己温柔一些。🌸",
                "内疚感并不能帮助孩子，反而会消耗您的能量。",
                "您对孩子的爱是最重要的，专业帮助只是锦上添花。"
            ],
            "愤怒": [
                "愤怒是正常的反应。重要的是找到健康的方式来处理它。",
                "试着找出愤怒的根源，是什么触发了这种情绪？",
                "照顾自闭症儿童确实有很多挑战，给自己一些理解的空间。"
            ],
            "感激": [
                "很高兴听到您积极的时刻！请继续珍惜这些美好时光。😊",
                "分享积极经历也能鼓励其他家长，谢谢您的分享。",
                "这些积极时刻提醒我们，所有的努力都是值得的。"
            ],
            "希望": [
                "您的乐观态度非常重要，会影响整个家庭的氛围！🌟",
                "继续保持这种积极的心态，每一天都会变得更好。",
                "希望是推动我们前进的力量，您已经走在正确的道路上。"
            ]
        }

        # 资源推荐
        self.resources = {
            "support_groups": [
                "本地自闭症家长支持团体",
                "在线社区：Wrong Planet, Autism Speaks论坛",
                "Facebook自闭症家长群组"
            ],
            "professional_help": [
                "行为分析师 (BCBA)",
                "儿童心理医生",
                "特殊教育顾问",
                "职业治疗师"
            ],
            "respite_care": [
                "临时照顾服务",
                "周末营地项目",
                "家庭支持服务"
            ],
            "educational_resources": [
                "自闭症教育书籍",
                "在线课程和研讨会",
                "YouTube教育频道"
            ]
        }

        # 对话历史
        self.conversation_history = []

        # 问候语
        self.greetings = [
            "您好！我是您的自闭症儿童家长支持伙伴。我在这里倾听您的感受，提供支持和资源。有什么我可以帮助您的吗？",
            "欢迎来到这里。我理解照顾自闭症儿童的挑战，也见证了许多家庭的成长。请告诉我您的感受。",
            "您好！作为一位经历过类似经历的支持伙伴，我很高兴能为您提供支持。今天过得怎么样？"
        ]

    def analyze_emotion(self, message: str) -> List[str]:
        """分析用户消息中的情感关键词"""
        detected_emotions = []
        message_lower = message.lower()

        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                # 对于中文，使用简单的字符串包含检查
                if keyword in message_lower:
                    if emotion not in detected_emotions:
                        detected_emotions.append(emotion)

        return detected_emotions

    def get_support_response(self, emotions: List[str]) -> str:
        """基于检测到的情绪生成支持响应"""
        if not emotions:
            return "我在这里倾听。请告诉我更多关于您的情况，我会尽力提供支持。"

        # 随机选择一个主要情绪进行响应
        primary_emotion = random.choice(emotions)

        if primary_emotion in self.support_responses:
            response = random.choice(self.support_responses[primary_emotion])
        else:
            response = "谢谢您分享您的感受。我会尽力理解和支持您。"

        # 如果检测到多个情绪，添加额外支持
        if len(emotions) > 1:
            response += "\n\n我感受到您有多种情绪在交织，这很正常。照顾自闭症儿童确实会带来复杂的感受。"

        return response

    def provide_resources(self, query: str) -> str:
        """根据查询提供相关资源"""
        query_lower = query.lower()

        if any(word in query_lower for word in ["支持", "团体", "社区", "交流"]):
            resources = random.sample(self.resources["support_groups"], 2)
            return f"推荐的家长支持资源：\n• {resources[0]}\n• {resources[1]}"

        elif any(word in query_lower for word in ["专业", "医生", "治疗", "专家"]):
            resources = random.sample(self.resources["professional_help"], 2)
            return f"专业帮助建议：\n• {resources[0]}\n• {resources[1]}"

        elif any(word in query_lower for word in ["休息", "照顾", "暂时", "帮助"]):
            resources = random.sample(self.resources["respite_care"], 2)
            return f"临时照顾资源：\n• {resources[0]}\n• {resources[1]}"

        elif any(word in query_lower for word in ["学习", "教育", "知识", "了解"]):
            resources = random.sample(self.resources["educational_resources"], 2)
            return f"教育资源推荐：\n• {resources[0]}\n• {resources[1]}"

        else:
            return "我可以帮您找到更多资源。请告诉我您具体需要什么类型的帮助？"

    def get_crisis_support(self) -> str:
        """提供危机情况下的支持信息"""
        return """🚨 如果您或您的孩子正处于危机中，请立即寻求专业帮助：

• 拨打紧急服务：急救电话
• 联系当地心理健康危机热线
• 寻求医疗专业人士的立即帮助
• 如果有自杀念头，请拨打自杀预防热线

您并不孤单，专业帮助就在那里。请优先考虑安全。"""

    def check_crisis_keywords(self, message: str) -> bool:
        """检查是否包含危机关键词"""
        crisis_keywords = [
            "自杀", "结束生命", "不想活了", "伤害自己",
            "危机", "紧急", "危险", "伤害孩子"
        ]

        message_lower = message.lower()
        return any(keyword in message_lower for keyword in crisis_keywords)

    def generate_greeting(self) -> str:
        """生成问候语"""
        return random.choice(self.greetings)

    def chat(self, user_message: str) -> str:
        """主要的聊天功能"""
        # 记录对话历史
        self.conversation_history.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "user": user_message,
            "bot": ""
        })

        # 检查危机情况
        if self.check_crisis_keywords(user_message):
            response = self.get_crisis_support()
        else:
            # 分析情感
            emotions = self.analyze_emotion(user_message)

            # 生成响应
            if not self.conversation_history or len(self.conversation_history) == 1:
                # 第一次对话或问候
                response = self.generate_greeting()
            else:
                # 基于情感的响应
                response = self.get_support_response(emotions)

            # 检查是否需要提供资源
            if any(word in user_message.lower() for word in ["资源", "帮助", "推荐", "找", "需要"]):
                response += "\n\n" + self.provide_resources(user_message)

        # 更新对话历史
        if self.conversation_history:
            self.conversation_history[-1]["bot"] = response

        return response

    def get_conversation_summary(self) -> Dict:
        """获取对话总结"""
        if not self.conversation_history:
            return {"message": "还没有对话记录"}

        total_messages = len(self.conversation_history)
        emotions_detected = []

        for entry in self.conversation_history:
            emotions_detected.extend(self.analyze_emotion(entry["user"]))

        # 统计最常见的情绪
        from collections import Counter
        common_emotions = Counter(emotions_detected).most_common(3)

        return {
            "total_messages": total_messages,
            "common_emotions": common_emotions,
            "conversation_length": len(self.conversation_history)
        }


def main():
    """主程序"""
    bot = EmotionalSupportBot()

    print("🤖 自闭症儿童家长情感支持聊天机器人")
    print("=" * 50)
    print("输入 'quit' 或 '退出' 结束对话")
    print("输入 'summary' 查看对话总结")
    print()

    # 初始问候
    print("机器人:", bot.generate_greeting())
    print()

    while True:
        try:
            user_input = input("您: ").strip()

            if user_input.lower() in ['quit', '退出', 'q']:
                print("\n机器人: 感谢您与我聊天。记住，您永远不是一个人在战斗。保重！❤️")
                break

            elif user_input.lower() == 'summary':
                summary = bot.get_conversation_summary()
                print("\n📊 对话总结:")
                if "total_messages" in summary:
                    print(f"总消息数: {summary['total_messages']}")
                    print(f"常见情绪: {dict(summary['common_emotions'])}")
                else:
                    print(summary["message"])
                print()
                continue

            if user_input:
                response = bot.chat(user_input)
                print(f"机器人: {response}")
                print()

        except KeyboardInterrupt:
            print("\n\n机器人: 感谢您的使用！希望我的支持对您有帮助。")
            break
        except Exception as e:
            print(f"抱歉，出现了一个错误: {e}")
            print("请继续我们的对话，或者输入 'quit' 退出。")


if __name__ == "__main__":
    main()
