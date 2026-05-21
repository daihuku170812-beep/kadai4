from attendance import AttendanceManager


def main():
    # 授業を作成
    manager = AttendanceManager("プロジェクトマネジメント演習")

    # 学生を登録
    manager.add_student("36714040", "鎌田空")
    manager.add_student("36714041", "田中太郎")
    manager.add_student("36714042", "佐藤花子")

    # 授業日を追加
    dates = ["2026-04-23", "2026-04-30", "2026-05-07", "2026-05-14"]
    for d in dates:
        manager.add_class_date(d)

    # 出席を記録
    manager.mark_attendance("36714040", "2026-04-23")
    manager.mark_attendance("36714040", "2026-04-30")
    manager.mark_attendance("36714040", "2026-05-07")
    manager.mark_attendance("36714041", "2026-04-23")
    manager.mark_attendance("36714042", "2026-04-23")
    manager.mark_attendance("36714042", "2026-04-30")
    manager.mark_attendance("36714042", "2026-05-07")
    manager.mark_attendance("36714042", "2026-05-14")

    # 全記録を表示
    manager.show_all_records()

    # 特定日の欠席者確認
    manager.show_absent_students("2026-05-14")


if __name__ == "__main__":
    main()

# 修正1: コメントを追加
