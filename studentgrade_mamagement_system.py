# 学生成绩管理系统

students = []  # 学生记录列表
course_count = 0  # 课程门数
student_count = 0  # 学生人数

# 成绩等级划分：(等级名称, 分数下限)
GRADE_LEVELS = [
    ("优秀", 90),
    ("良好", 80),
    ("中等", 70),
    ("及格", 60),
    ("不及格", 0),
]


def student_total(student):
    return sum(student["scores"])


def student_avg(student):
    return student_total(student) / course_count


def has_records():
    if not students:
        print("暂无学生记录，请先录入记录！")
        return False
    return True


def input_int(prompt, min_val, max_val):
    while True:
        try:
            n = int(input(prompt))
            if min_val <= n <= max_val:
                return n
            print(f"输入错误，必须在{min_val}到{max_val}之间，请重新输入！")
        except ValueError:
            print("输入错误，请输入一个整数！")


def input_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("成绩必须在0~100之间，请重新输入！")
        except ValueError:
            print("输入错误，请输入一个数字！")


# 菜单显示函数
def print_menu():
    print("=" * 44)
    print("  1. Input record")
    print("  2. Calculate total and average score of every course")
    print("  3. Calculate total and average score of every student")
    print("  4. Sort in descending order by total score of every student")
    print("  5. Sort in ascending order by total score of every student")
    print("  6. Sort in ascending order by number")
    print("  7. Sort in dictionary order by name")
    print("  8. Search by number")
    print("  9. Search by name")
    print(" 10. Statistic analysis for every course")
    print(" 11. List record")
    print("  0. Exit")
    print("=" * 44)


# 功能1：输入每个学生的学号、姓名和各科考试成绩
def input_records():
    global students, course_count, student_count
    student_count = input_int("请输入学生人数(1~30): ", 1, 30)
    course_count = input_int("请输入课程门数(1~6): ", 1, 6)
    students = []
    for i in range(student_count):
        print(f"\n请输入第{i + 1}个学生的信息:")
        stu_id = input("  学号: ")
        stu_name = input("  姓名: ")
        scores = []
        for j in range(course_count):
            score = input_score(f"  第{j + 1}门课成绩: ")
            scores.append(score)
        students.append({"id": stu_id, "name": stu_name, "scores": scores})
    print(f"\n记录录入完成！共录入{student_count}名学生，{course_count}门课程。")


# 功能2：计算每门课程的总分和平均分
def calc_course_total_avg():
    if not has_records():
        return
    print("\n每门课程的总分和平均分:")
    print("课程编号    总分      平均分")
    print("-" * 30)
    for j in range(course_count):
        total = 0
        # 逐个累加所有学生该门课的成绩
        for s in students:
            total += s["scores"][j]
        avg = total / len(students)
        print(f"第{j + 1}门      {total:.2f}    {avg:.2f}")


# 功能3：计算每个学生的总分和平均分
def calc_student_total_avg():
    if not has_records():
        return
    print("\n每个学生的总分和平均分:")
    print(f"{'学号':<10}{'姓名':<10}{'总分':<10}{'平均分'}")
    print("-" * 40)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<10}{student_total(s):<10.2f}{student_avg(s):.2f}")


# 功能4：按每个学生的总分由高到低排出名次表
def sort_by_total_desc():
    if not has_records():
        return
    # 使用sorted按总分降序排序，reverse=True表示降序
    ranked = sorted(students, key=lambda s: student_total(s), reverse=True)
    print("\n按总分由高到低名次表:")
    print(f"{'名次':<6}{'学号':<10}{'姓名':<10}{'总分':<10}{'平均分'}")
    print("-" * 50)
    for rank, s in enumerate(ranked, 1):
        print(f"{rank:<6}{s['id']:<10}{s['name']:<10}{student_total(s):<10.2f}{student_avg(s):.2f}")


# 功能5：按每个学生的总分由低到高排出名次表
def sort_by_total_asc():
    if not has_records():
        return
    ranked = sorted(students, key=lambda s: student_total(s))  # 默认升序
    print("\n按总分由低到高名次表:")
    print(f"{'名次':<6}{'学号':<10}{'姓名':<10}{'总分':<10}{'平均分'}")
    print("-" * 50)
    for rank, s in enumerate(ranked, 1):
        print(f"{rank:<6}{s['id']:<10}{s['name']:<10}{student_total(s):<10.2f}{student_avg(s):.2f}")


# 功能6：按学号由小到大排出成绩表
def sort_by_id_asc():
    if not has_records():
        return
    ordered = sorted(students, key=lambda s: s["id"])  # 学号字符串升序
    print("\n按学号由小到大成绩表:")
    header = f"{'学号':<10}{'姓名':<10}" + "".join(f"课程{i + 1:<6}" for i in range(course_count)) + "总分"
    print(header)
    print("-" * len(header))
    for s in ordered:
        row = f"{s['id']:<10}{s['name']:<10}"
        row += "".join(f"{score:<8.2f}" for score in s["scores"])
        row += f"{student_total(s):.2f}"
        print(row)


# 功能7：按姓名的字典顺序排出成绩表
def sort_by_name():
    if not has_records():
        return
    ordered = sorted(students, key=lambda s: s["name"])  # 姓名字典序升序
    print("\n按姓名字典顺序成绩表:")
    header = f"{'学号':<10}{'姓名':<10}" + "".join(f"课程{i + 1:<6}" for i in range(course_count)) + "总分"
    print(header)
    print("-" * len(header))
    for s in ordered:
        row = f"{s['id']:<10}{s['name']:<10}"
        row += "".join(f"{score:<8.2f}" for score in s["scores"])
        row += f"{student_total(s):.2f}"
        print(row)


# 功能8：按学号查询学生排名及其考试成绩（顺序查找）
def search_by_id():
    if not has_records():
        return
    target = input("请输入要查询的学号: ")
    # 先按总分降序排序以确定名次
    ranked = sorted(students, key=lambda s: student_total(s), reverse=True)
    # 顺序查找：逐个比对学号
    for rank, s in enumerate(ranked, 1):
        if s["id"] == target:
            print(f"\n查询结果:")
            print(f"名次: {rank}")
            print(f"学号: {s['id']}")
            print(f"姓名: {s['name']}")
            for i, score in enumerate(s["scores"], 1):
                print(f"第{i}门课成绩: {score}")
            print(f"总分: {student_total(s):.2f}")
            print(f"平均分: {student_avg(s):.2f}")
            return
    print(f"未找到学号为{target}的学生！")


# 功能9：按姓名查询学生排名及其考试成绩（顺序查找）
def search_by_name():
    if not has_records():
        return
    target = input("请输入要查询的姓名: ")
    ranked = sorted(students, key=lambda s: student_total(s), reverse=True)
    # 顺序查找：逐个比对姓名
    for rank, s in enumerate(ranked, 1):
        if s["name"] == target:
            print(f"\n查询结果:")
            print(f"名次: {rank}")
            print(f"学号: {s['id']}")
            print(f"姓名: {s['name']}")
            for i, score in enumerate(s["scores"], 1):
                print(f"第{i}门课成绩: {score}")
            print(f"总分: {student_total(s):.2f}")
            print(f"平均分: {student_avg(s):.2f}")
            return
    print(f"未找到姓名为{target}的学生！")


# 功能10：对每门课程分别统计各等级人数及所占百分比
def statistic_analysis():
    if not has_records():
        return
    print("\n每门课程成绩等级统计:")
    print("等级说明: 优秀(90~100) 良好(80~89) 中等(70~79) 及格(60~69) 不及格(0~59)\n")
    total_stu = len(students)
    for j in range(course_count):
        # 收集该门课所有成绩
        course_scores = [s["scores"][j] for s in students]
        # 按等级统计人数：遍历每个等级，统计分数达到该等级下限的人数
        counts = []
        prev = 101  # 上一个等级的下限+1，用于区间判断
        for name, low in GRADE_LEVELS:
            cnt = sum(1 for sc in course_scores if low <= sc < prev)
            counts.append((name, cnt))
            prev = low

        print(f"第{j + 1}门课程:")
        for name, cnt in counts:
            print(f"  {name}: {cnt}人 ({cnt / total_stu * 100:.2f}%)")
        print()


# 功能11：输出每个学生信息及每门课程的总分和平均分=
def list_records():
    if not has_records():
        return
    print("\n学生成绩表:")
    header = f"{'学号':<10}{'姓名':<10}" + "".join(f"课程{i + 1:<8}" for i in range(course_count)) + "总分      平均分"
    print(header)
    print("-" * len(header))
    for s in students:
        row = f"{s['id']:<10}{s['name']:<10}"
        row += "".join(f"{score:<8.2f}" for score in s["scores"])
        row += f"{student_total(s):<10.2f}{student_avg(s):.2f}"
        print(row)
    # 输出每门课程的总分和平均分
    print("\n每门课程总分:")
    print(" " * 20, end="")
    for j in range(course_count):
        total = sum(s["scores"][j] for s in students)
        print(f"{total:<8.2f}", end="")
    print()
    print("每门课程平均分:")
    print(" " * 20, end="")
    for j in range(course_count):
        total = sum(s["scores"][j] for s in students)
        print(f"{total / len(students):<8.2f}", end="")
    print()


# 主函数：菜单驱动循环
def main():
    actions = {
        "1": input_records,
        "2": calc_course_total_avg,
        "3": calc_student_total_avg,
        "4": sort_by_total_desc,
        "5": sort_by_total_asc,
        "6": sort_by_id_asc,
        "7": sort_by_name,
        "8": search_by_id,
        "9": search_by_name,
        "10": statistic_analysis,
        "11": list_records,
    }
    while True:
        print_menu()
        choice = input("Please enter your choice: ")
        if choice == "0":
            print("\n感谢使用学生成绩管理系统，再见！")
            break
        if choice in actions:
            actions[choice]()
        else:
            print("\n输入无效，请输入0~11之间的数字！")


# 程序入口
if __name__ == "__main__":
    main()
