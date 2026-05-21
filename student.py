class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.attendance_record = []  # 出欠記録リスト

    def attend(self, date: str):
        """出席を記録する"""
        if date not in self.attendance_record:
            self.attendance_record.append(date)
            print(f"{self.name} ({self.student_id}) : {date} に出席しました")
        else:
            print(f"{self.name} : {date} はすでに出席済みです")

    def get_attendance_rate(self, total_classes: int) -> float:
        """出席率を計算して返す"""
        if total_classes == 0:
            return 0.0
        return len(self.attendance_record) / total_classes * 100

    def show_record(self):
        """出欠記録を表示する"""
        print(f"\n--- {self.name} ({self.student_id}) の出欠記録 ---")
        if not self.attendance_record:
            print("  出席記録がありません")
        for date in self.attendance_record:
            print(f"  出席: {date}")

    def __repr__(self):
        return f"Student(id={self.student_id}, name={self.name})"

# 修正2: メソッドの説明を追記
