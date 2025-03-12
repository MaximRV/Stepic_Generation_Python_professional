import sys

total_sum = 0
count = 0
for line in sys.stdin:
    try:
        total_sum += int(line)
    except ValueError:
        try:
            total_sum += float(line)
        except ValueError:
            count += 1
print(total_sum)
print(count)
