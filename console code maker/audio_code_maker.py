import string


def name_maker(s):
    new_s = ""
    for i in s:
        if i not in string.punctuation and i != "\n" and i != " ":
            new_s += i
        if i == " ":
            i = "_"
            new_s += i
    if new_s[-1] == "_":
        new_s = new_s[0:-1]
    return new_s

source = open("audio.txt", "r")
code = open("audio_code.txt", "w")

while True:
    new_line = ""
    line = source.readline()
    if len(line) != 0 and line[-1] == " ":
        line[-1] = ""
    if len(line) == 0:
        break
    new_line = name_maker(line)
    code.write("public var  {0}: AudioClip;\n".format(new_line))

source.close()
code.close()
