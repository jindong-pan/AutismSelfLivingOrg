#!/usr/bin/env python3
"""
行为追踪器演示脚本 - Behavior Tracker Demo Script

这个脚本演示如何使用行为追踪器记录和分析行为数据
"""

from behavior_tracker import BehaviorTracker
import datetime

def demo():
    """演示行为追踪器的功能"""
    print("🌟 自闭症儿童行为追踪器演示")
    print("=" * 50)

    # 创建追踪器实例
    tracker = BehaviorTracker("demo_data.json")

    print("\n📝 添加演示数据...")

    # 添加一些演示数据
    demo_entries = [
        {
            "behavior": "在超市排队时发脾气",
            "category": "challenging",
            "intensity": 4,
            "trigger": "等待时间长",
            "notes": "不喜欢排队，提前准备了玩具但还是发生了",
            "duration": 15
        },
        {
            "behavior": "专注玩拼图游戏",
            "category": "positive",
            "intensity": 2,
            "trigger": "感兴趣的活动",
            "notes": "连续玩了30分钟，进展很好",
            "duration": 30
        },
        {
            "behavior": "早晨起床困难",
            "category": "challenging",
            "intensity": 3,
            "trigger": "日常变化",
            "notes": "需要更多时间适应早晨 routine",
            "duration": 20
        },
        {
            "behavior": "与兄弟姐妹分享玩具",
            "category": "developmental",
            "intensity": 2,
            "trigger": "家庭活动",
            "notes": "这是第一次主动分享，很好的社交进步",
            "duration": 10
        },
        {
            "behavior": "在公园玩耍开心",
            "category": "positive",
            "intensity": 1,
            "trigger": "户外活动",
            "notes": "喜欢秋千和滑梯，社交互动增加",
            "duration": 45
        }
    ]

    # 添加演示数据（设置过去几天的日期以便分析）
    base_date = datetime.datetime.now() - datetime.timedelta(days=3)

    for i, entry in enumerate(demo_entries):
        # 模拟不同日期的数据
        entry_date = base_date + datetime.timedelta(days=i % 3)
        entry["timestamp"] = entry_date.isoformat()

        # 移除timestamp，因为add_behavior_entry会自动添加当前时间戳
        temp_entry = entry.copy()
        del temp_entry["timestamp"]

        tracker.add_behavior_entry(**temp_entry)

    print("✅ 演示数据添加完成")

    # 演示功能
    print("\n📊 今日行为总结:")
    summary = tracker.get_daily_summary()
    if "total_entries" in summary:
        print(f"  总记录数: {summary['total_entries']}")
        print(f"  平均强度: {summary['avg_intensity']:.1f}/5")
        print(f"  类别分布: {dict(summary['categories'])}")
        if summary['common_triggers']:
            print(f"  常见触发因素: {dict(summary['common_triggers'])}")
    else:
        print(f"  {summary.get('message', '无数据')}")

    print("\n🔍 行为模式分析 (过去7天):")
    patterns = tracker.analyze_patterns(days=7)
    if "time_patterns" in patterns:
        print(f"  最活跃时间段: {patterns['time_patterns']['busiest_hours']}")

        trigger_analysis = patterns.get("trigger_analysis", {})
        if trigger_analysis.get("common_triggers"):
            print("  常见触发因素:")
            for trigger, count in trigger_analysis["common_triggers"][:3]:
                print(f"    • {trigger}: {count}次")

        print("  💡 AI建议:")
        recommendations = patterns.get("recommendations", [])
        for i, rec in enumerate(recommendations, 1):
            print(f"    {i}. {rec}")
    else:
        print(f"  {patterns.get('message', '无数据')}")

    print("\n📄 生成分析报告...")
    report_file = tracker.export_report("demo_report.txt", days=7)
    print(f"✅ 报告已保存到: {report_file}")

    # 显示报告内容预览
    print("\n📋 报告预览:")
    print("-" * 30)
    try:
        with open(report_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:20]  # 只显示前20行
            for line in lines:
                print(line.rstrip())
            if len(lines) == 20:
                print("... (报告完整内容请查看文件)")
    except FileNotFoundError:
        print("报告文件未找到")

    print("\n🎉 演示完成！")
    print("您可以运行 'python behavior_tracker.py' 开始使用完整功能")

if __name__ == "__main__":
    demo()
