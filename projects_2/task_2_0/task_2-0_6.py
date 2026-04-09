name = "Инес Надира Леон Пуэнте"
group = "4731204/50001"
year = 2026

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Информация о студенте\n")
    file.write("=" * 30 + "\n")
    file.write(f"Имя: {name}\n")
    file.write(f"Группа: {group}\n")
    file.write(f"Год поступления: {year}\n")

print("✅ Информация успешно записана в файл output.txt")