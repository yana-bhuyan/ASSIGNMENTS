seconds = 3667
hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(hours, "hours", minutes, "minutes", seconds, "seconds")