# Exercise 1
def save_scores(names, scores, filename):
    file=open(filename, "w")
    r = len(names)
    for i in range(r):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()

# Exercise 2
def average_score(filename):
    file=open(filename,"r")
    total = 0
    count = 0
    for line in file:
        line=line.strip()
        if line!="":
            p=line.split(',')
            total=total+int(p[1])
            count+=1
    file.close()
    if count==0:
        return 0
    return round(total/count,1)
    pass

# Exercise 3
def filter_passed(source, destination, pass_mark):
    file=open(source,"r")
    lines = file.readlines()
    file.close()
    file=open(destination,"w")
    passed_count=0
    for line in lines:
        line=line.strip()
        if line=="":
            continue
        parts=line.split(",")
        if int(parts[1])>=pass_mark:
            passed_count+=1
            file.write(line+"\n")
            passed_count += 1
    file.close()
    return passed_count
    pass

# Exercise 4
def replace_word(filename, old_word, new_word):
  file = open(filename, "r")
  content = file.read()
  file.close()
  count = content.count(old_word)
  new_content = content.replace(old_word, new_word)
  file = open(filename, "w")
  file.write(new_content)
  file.close()
  return count

# Exercise 5
def remove_line(filename, line_number):
  file=open(filename, "r")
  lines=file.readlines()
  file.close()
  if line_number<1 or line_number>len(lines):
    return False
  lines.pop(line_number-1)
  file = open(filename,"w")
  for line in lines:
    file.write(line)
  file.close()

  return True
