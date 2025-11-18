def read_employees(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    employees = []
    i = 3  # از بعد از عناوین شروع می‌کنیم

    while i < len(lines):
        height = int(lines[i])
        weight = int(lines[i + 1])
        name = lines[i + 2]

        employees.append({
            "name": name,
            "height": height,
            "weight": weight
        })

        i += 3  # برو سراغ فرد بعدی

    return employees


def main():
    employees = read_employees("employees.txt")

    # مرتب‌سازی
    employees_sorted = sorted(
        employees,
        key=lambda x: (-x["height"], x["weight"])
    )

    # چاپ خروجی
    for emp in employees_sorted:
        print(emp["name"], emp["height"], emp["weight"])


if __name__ == "__main__":
    main()
