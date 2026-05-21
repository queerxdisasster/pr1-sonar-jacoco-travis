import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"





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
    phone = parts[2]
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