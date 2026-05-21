from student import Student


class AttendanceManager:
    def __init__(self, course_name: str):
        self.course_name = course_name
        self.students: dict[str, Student] = {}
        self.class_dates: list[str] = []

    def add_student(self, student_id: str, name: str):
        """学生を登録する"""
        if student_id in self.students:
            print(f"学生ID {student_id} はすでに登録されています")
            return
        self.students[student_id] = Student(student_id, name)
        print(f"学生を登録しました: {name} ({student_id})")

    def add_class_date(self, date: str):
        """授業日を追加する"""
        if date not in self.class_dates:
            self.class_dates.append(date)
            print(f"授業日を追加: {date}")

    def mark_attendance(self, student_id: str, date: str):
        """指定学生の出席を記録する"""
        if date not in self.class_dates:
            print(f"エラー: {date} は授業日として登録されていません")
            return
        if student_id not in self.students:
            print(f"エラー: 学生ID {student_id} は登録されていません")
            return
        self.students[student_id].attend(date)

    def show_all_records(self):
        """全学生の出欠記録を表示する"""
        print(f"\n=== {self.course_name} 出欠一覧 ===")
        total_classes = len(self.class_dates)
        for student in self.students.values():
            student.show_record()
            rate = student.get_attendance_rate(total_classes)
            print(f"  出席率: {rate:.1f}% ({len(student.attendance_record)}/{total_classes}回)")

    def get_absent_students(self, date: str) -> list[Student]:
        """指定日の欠席者リストを返す"""
        absent = []
        for student in self.students.values():
            if date not in student.attendance_record:
                absent.append(student)
        return absent

    def show_absent_students(self, date: str):
        """指定日の欠席者を表示する"""
        absent = self.get_absent_students(date)
        print(f"\n{date} の欠席者:")
        if not absent:
            print("  全員出席")
        for s in absent:
            print(f"  - {s.name} ({s.student_id})")
