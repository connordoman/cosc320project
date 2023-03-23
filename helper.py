

script_lines = []

with open("bee_movie.html", "r") as file:
    save = False
    lastLine = ""

    for line in file:
        line = line.strip()
        if "</pre>" in line:
            save = False

        if line == lastLine:
            continue

        if save:
            script_lines.append(line)

        if "<pre>" in line:
            save = True

        lastLine = line

with open("script_data.txt", "w") as file:
    for line in script_lines:
        file.write(line + "\n")

num_words = 0
num_lines = 0
for line in script_lines:
    if line == "" or line == "\n":
        continue
    
    num_lines += 1

    for word in line.split(" "):
        num_words += 1

print("Number of lines: " + str(num_lines))
print("Number of words: " + str(num_words))

