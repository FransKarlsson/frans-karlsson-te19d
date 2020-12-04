f=open("C:/Users/Elev/Documents/GitHub/frans-karlsson-te19d/aventofcode/day2/puzzle_input.txt", "r")
legalpasswords=0
text=f.readline()

text=text.split()
print(text)
if text[2].count(int(text[1[0]])) > int(text[0][0]) and text[2].count(text[1[0]]) < int(text[0][2:]):
    legalpasswords+=1
print(legalpasswords)



f.close()

