"""with open("maniupalacionTxt/cuento.txt", "r") as file:
    # Leemos cada línea y eliminamos los saltos de línea al final
    for line in file:
        print(line.strip())

print("------------------------------------------------------------------")
with open("maniupalacionTxt/cuento.txt", "r") as file:
    lines = file.readlines()
    print(lines)"""

print("------------------------------------------------------------------")
with open("caperucita.txt", "a") as file:
    file.write("\n\nBy:ChatGPT.")