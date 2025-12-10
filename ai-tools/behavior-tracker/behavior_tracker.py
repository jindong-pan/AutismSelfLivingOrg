#!/usr/bin/env python3
"""
自闭症儿童日常行为追踪器 - Daily Behavior Tracker for Children with Autism

这个AI驱动的工具帮助家长记录和分析儿童的日常行为模式，
提供个性化的洞察和建议。
"""

import json
import datetime
from collections import defaultdict, Counter
from typing import Dict, List, Optional
import os

class BehaviorTracker:
    """AI驱动的行为追踪和分析系统"""

    def __init__(self, data_file: str = "behavior_data.json"):
        self.data_file = data_file
        self.behaviors = self.load_data()

        # 预定义的行为类别和触发因素
        self.behavior_categories = {
            "positive": ["快乐", "专注", "合作", "平静", "社交"],
            "challenging": ["焦虑", "发脾气", "攻击性", "退缩", "过度活跃"],
            "developmental": ["语言进步", "社交技能", "日常生活技能", "认知发展"]
        }

        self.triggers = [
            "环境变化", "睡眠不足", "饥饿", "感官过载", "社交压力",
            "日常变化", "生病", "天气变化", "噪音", "新环境"
        ]

    def load_data(self) -> Dict:
        """加载行为数据"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"entries": []}

    def save_data(self):
        """保存行为数据"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.behaviors, f, ensure_ascii=False, indent=2)

    def add_behavior_entry(self, behavior: str, category: str,
                          intensity: int, trigger: str = "",
                          notes: str = "", duration: int = 0):
        """
        添加行为记录

        Args:
            behavior: 具体行为描述
            category: 行为类别 (positive/challenging/developmental)
            intensity: 强度 (1-5)
            trigger: 可能的触发因素
            notes: 额外备注
            duration: 持续时间(分钟)
        """
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "behavior": behavior,
            "category": category,
            "intensity": max(1, min(5, intensity)),  # 确保在1-5范围内
            "trigger": trigger,
            "notes": notes,
            "duration": duration
        }

        self.behaviors["entries"].append(entry)
        self.save_data()
        print(f"✅ 已记录行为: {behavior}")

    def get_daily_summary(self, date: str = None) -> Dict:
        """获取每日行为总结"""
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")

        day_entries = [entry for entry in self.behaviors["entries"]
                      if entry["timestamp"].startswith(date)]

        if not day_entries:
            return {"message": f"{date} 没有行为记录"}

        summary = {
            "date": date,
            "total_entries": len(day_entries),
            "categories": Counter(entry["category"] for entry in day_entries),
            "avg_intensity": sum(entry["intensity"] for entry in day_entries) / len(day_entries),
            "common_triggers": Counter(entry["trigger"] for entry in day_entries if entry["trigger"]),
            "top_behaviors": Counter(entry["behavior"] for entry in day_entries).most_common(3)
        }

        return summary

    def analyze_patterns(self, days: int = 7) -> Dict:
        """AI驱动的模式分析"""
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
        recent_entries = [entry for entry in self.behaviors["entries"]
                         if datetime.datetime.fromisoformat(entry["timestamp"]) > cutoff_date]

        if not recent_entries:
            return {"message": f"过去{days}天没有足够的数据进行分析"}

        # 分析行为模式
        patterns = {
            "time_patterns": self._analyze_time_patterns(recent_entries),
            "trigger_analysis": self._analyze_triggers(recent_entries),
            "intensity_trends": self._analyze_intensity_trends(recent_entries),
            "recommendations": self._generate_recommendations(recent_entries)
        }

        return patterns

    def _analyze_time_patterns(self, entries: List[Dict]) -> Dict:
        """分析时间模式"""
        hourly_patterns = defaultdict(list)

        for entry in entries:
            dt = datetime.datetime.fromisoformat(entry["timestamp"])
            hour = dt.hour
            hourly_patterns[hour].append(entry)

        # 找出最活跃的时间段
        busiest_hours = sorted(hourly_patterns.keys(),
                              key=lambda h: len(hourly_patterns[h]),
                              reverse=True)[:3]

        return {
            "busiest_hours": busiest_hours,
            "quietest_hours": sorted(hourly_patterns.keys(),
                                   key=lambda h: len(hourly_patterns[h]))[:3]
        }

    def _analyze_triggers(self, entries: List[Dict]) -> Dict:
        """分析触发因素"""
        trigger_counter = Counter(entry["trigger"] for entry in entries if entry["trigger"])

        # 找出最常见的触发因素及其相关行为
        trigger_behaviors = defaultdict(list)
        for entry in entries:
            if entry["trigger"]:
                trigger_behaviors[entry["trigger"]].append(entry["behavior"])

        return {
            "common_triggers": trigger_counter.most_common(5),
            "trigger_behavior_correlations": dict(trigger_behaviors)
        }

    def _analyze_intensity_trends(self, entries: List[Dict]) -> Dict:
        """分析强度趋势"""
        # 按类别分析平均强度
        category_intensity = defaultdict(list)
        for entry in entries:
            category_intensity[entry["category"]].append(entry["intensity"])

        avg_intensity_by_category = {}
        for category, intensities in category_intensity.items():
            avg_intensity_by_category[category] = sum(intensities) / len(intensities)

        return avg_intensity_by_category

    def _generate_recommendations(self, entries: List[Dict]) -> List[str]:
        """生成个性化建议"""
        recommendations = []

        # 基于触发因素的建议
        trigger_analysis = self._analyze_triggers(entries)
        common_triggers = [trigger for trigger, _ in trigger_analysis["common_triggers"][:2]]

        trigger_suggestions = {
            "环境变化": "尝试在日常变化前提前准备和过渡活动",
            "睡眠不足": "建立规律的睡眠时间表，确保充足休息",
            "饥饿": "保持规律的进餐时间，避免长时间空腹",
            "感官过载": "创建安静的休息区域，减少过度刺激",
            "社交压力": "逐渐增加社交活动，从小群体开始",
            "日常变化": "使用视觉时间表帮助理解日常变化",
            "生病": "在生病期间减少活动，提供额外支持",
            "天气变化": "提前了解天气变化，调整户外活动",
            "噪音": "使用噪音消除耳机或创建安静空间",
            "新环境": "提前参观新环境，逐步适应"
        }

        for trigger in common_triggers:
            if trigger in trigger_suggestions:
                recommendations.append(f"针对'{trigger}': {trigger_suggestions[trigger]}")

        # 基于行为类别的建议
        intensity_analysis = self._analyze_intensity_trends(entries)

        if "challenging" in intensity_analysis and intensity_analysis["challenging"] > 3:
            recommendations.append("考虑咨询行为分析师，制定行为干预计划")

        if "positive" in intensity_analysis and intensity_analysis["positive"] < 3:
            recommendations.append("增加积极强化活动，庆祝小成就")

        if len(recommendations) == 0:
            recommendations.append("继续保持记录，数据将帮助我们提供更准确的建议")

        return recommendations[:3]  # 返回前3个建议

    def export_report(self, filename: str = None, days: int = 7):
        """导出分析报告"""
        if filename is None:
            filename = f"behavior_report_{datetime.datetime.now().strftime('%Y%m%d')}.txt"

        patterns = self.analyze_patterns(days)
        daily_summary = self.get_daily_summary()

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("自闭症儿童行为分析报告\n")
            f.write("=" * 50 + "\n\n")

            f.write(f"报告生成日期: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"分析时间范围: 过去{days}天\n\n")

            f.write("📊 每日总结:\n")
            if "total_entries" in daily_summary:
                f.write(f"- 总记录数: {daily_summary['total_entries']}\n")
                f.write(f"- 平均强度: {daily_summary['avg_intensity']:.1f}/5\n")
                f.write(f"- 行为类别分布: {dict(daily_summary['categories'])}\n")
            else:
                f.write(daily_summary.get("message", "无数据") + "\n")

            f.write("\n🔍 模式分析:\n")
            if "time_patterns" in patterns:
                busiest = patterns["time_patterns"]["busiest_hours"]
                f.write(f"- 最活跃时间: {', '.join(map(str, busiest))}点\n")

                trigger_analysis = patterns.get("trigger_analysis", {})
                if trigger_analysis.get("common_triggers"):
                    f.write("- 常见触发因素:\n")
                    for trigger, count in trigger_analysis["common_triggers"][:3]:
                        f.write(f"  • {trigger}: {count}次\n")

            f.write("\n💡 个性化建议:\n")
            recommendations = patterns.get("recommendations", [])
            for i, rec in enumerate(recommendations, 1):
                f.write(f"{i}. {rec}\n")

        print(f"📄 报告已导出到: {filename}")
        return filename


def main():
    """主程序入口"""
    tracker = BehaviorTracker()

    print("🌟 自闭症儿童日常行为追踪器")
    print("=" * 40)

    while True:
        print("\n请选择操作:")
        print("1. 记录新行为")
        print("2. 查看今日总结")
        print("3. 分析行为模式")
        print("4. 生成报告")
        print("5. 退出")

        choice = input("\n请选择 (1-5): ").strip()

        if choice == "1":
            print("\n📝 记录新行为:")
            behavior = input("行为描述: ").strip()
            print("类别:", ", ".join(f"{k}({', '.join(v[:2])}...)" for k, v in tracker.behavior_categories.items()))
            category = input("类别 (positive/challenging/developmental): ").strip()
            intensity = int(input("强度 (1-5): ").strip())
            trigger = input("触发因素 (可选): ").strip()
            notes = input("备注 (可选): ").strip()
            duration = int(input("持续时间(分钟，可选): ").strip() or "0")

            tracker.add_behavior_entry(behavior, category, intensity, trigger, notes, duration)

        elif choice == "2":
            summary = tracker.get_daily_summary()
            print("\n📊 今日行为总结:")
            if "total_entries" in summary:
                print(f"总记录数: {summary['total_entries']}")
                print(f"平均强度: {summary['avg_intensity']:.1f}/5")
                print(f"类别分布: {dict(summary['categories'])}")
                if summary['common_triggers']:
                    print(f"常见触发因素: {dict(summary['common_triggers'])}")
            else:
                print(summary.get("message", "无数据"))

        elif choice == "3":
            patterns = tracker.analyze_patterns()
            print("\n🔍 行为模式分析:")
            if "time_patterns" in patterns:
                print(f"最活跃时间: {patterns['time_patterns']['busiest_hours']}")
                if "trigger_analysis" in patterns:
                    print("常见触发因素:")
                    for trigger, count in patterns["trigger_analysis"]["common_triggers"][:3]:
                        print(f"  • {trigger}: {count}次")
            else:
                print(patterns.get("message", "无数据"))

        elif choice == "4":
            filename = tracker.export_report()
            print(f"报告已生成: {filename}")

        elif choice == "5":
            print("感谢使用行为追踪器！")
            break

        else:
            print("无效选择，请重新输入。")


if __name__ == "__main__":
    main()
