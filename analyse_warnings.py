import re
from collections import defaultdict, Counter

with open("warnings.log", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Regex to extract warning number and message
warning_re = re.compile(r'warning\s+(C\d+):\s(.*)')

warning_counts = Counter()
warning_message_counts = defaultdict(Counter)

for line in lines:
    match = warning_re.search(line)
    if match:
        warning_number = match.group(1)
        message = match.group(2).rstrip()

        # Skip continuation lines (message starts with whitespace)
        if message and message[0].isspace():
            continue

        warning_counts[warning_number] += 1
        warning_message_counts[warning_number][message] += 1

print("=== Warning counts ===")
for warning_number, count in warning_counts.most_common():
    print(f"{warning_number}: {count}")

print("\n=== Unique messages per warning ===")
for warning_number in warning_counts:
    print(f"\n{warning_number} ({warning_counts[warning_number]} times):")
    for message, msg_count in warning_message_counts[warning_number].most_common():
        print(f"  [{msg_count}] {message}")
