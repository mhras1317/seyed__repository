
console = open("console.txt", "r")
console_code = open("console_code.txt", "w")

while True:
    line1 = console.readline()
    line = line1[0:-1]
    if len(line) == 0:
        break
    if line[0:4] == "-r- ":
        console_code.write('<ListBoxItem Foreground="Red" Content="{0}"/>\n'.format(line[4:]))
    if line[0:4] == "-g- ":
        console_code.write('<ListBoxItem Foreground="Green" Content="{0}"/>\n'.format(line[4:]))
    if line[0:4] == "-b- ":
        console_code.write('<ListBoxItem Foreground="Black" Content="{0}"/>\n'.format(line[4:]))
    if line[0:4] == "-f- ":
        console_code.write("Test\n")
    if line[0:4] == "----":
        console_code.write('<System:String xml:space="preserve"> ------------------------------------- </System:String>\n')
    if line[0:4] == "-s- ":
        console_code.write("\n")


console.close()
console_code.close()
