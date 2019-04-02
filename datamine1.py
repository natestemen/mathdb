import re
def stringGetter():
    theoremLi = []
    fh = open("TRENCH_REAL_ANALYSIS.tex.txt", "r")
    textString = fh.read()
    fh.close()
    stringList = re.findall(r'begin{corollary}(.*?)\\end{corollary}',textString, re.S)
    return stringList

stringList = stringGetter()

fh = open("realCorollary.txt", "w")
count = 1
for i in stringList:
    fh.write("\\begin{corollary}\n")
    fh.write(i)
    fh.write("\\end{corollary}\n\n")
    
fh.close()
            
