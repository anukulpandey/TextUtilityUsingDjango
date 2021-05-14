# capitalize first
# capitalize all
# new line remove
# space remove 
# charcount

# 1. Capitalize first
def capfirst(text):
    final = ""
    for index,char in enumerate(text):
        if index==0:
            final = final + char.upper()
        else:
            final = final + char
    return final

# 2. Capitalize all
def capall(text):
    final = text.upper()
    return final

# 3. New Line remove
def newlineremover(text):
    final=""
    for char in text:
        if char!='\n':
            final=final+char
    return final

# 4. Extra space remover
def xtsprem(text):
    final=''
    for index,char in enumerate(text):
        if not(text[index]==' ' and text[index+1]==' '):
            final=final+char
    return final

# 5. Character counter
def charcount(text):
    final = 0
    for char in text:
        final+=1
    return final