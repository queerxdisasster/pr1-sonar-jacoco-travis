import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"




def normalize_phone(value: str) -> str:
    digits = re.sub(r"\D", "", value)

    if len(digits) == 11 and digits[0] in ("7", "8"):
        digits = "7" + digits[1:]
    elif len(digits) == 10:
        digits = "7" + digits
    else:
        return ""

    return f"+7 ({digits[1:4]}) {digits[4:]}"


def normalize_email(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"@+", "@", value)
    value = re.sub(r"\.{2,}", ".", value)
    value = value.strip(".")

    pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    if re.fullmatch(pattern, value):
        return value
    return ""


def process_line(line: str) -> str:
    parts = line.strip().split("|")
    while len(parts) < 4:
        parts.append("")

    name = parts[0]
    age = parts[1]
    phone = normalize_phone(parts[2])
    email = normalize_email(parts[3])

    return f"{name}|{age}|{phone}|{email}"


def main() -> None:
    with open(INPUT_FILE, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    result = [process_line(line) for line in lines if line.strip()]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(result))


if __name__ == "__main__":
    main()