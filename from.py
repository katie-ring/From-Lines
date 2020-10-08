count = 0
han = open('mbox-short.txt')
for line in han:
  line = line.rstrip()
  wds = line.split()
  if len(wds) < 3 or wds[0] != 'From':
    continue
  count += 1
  print(wds[1])
print('There were', count, 'lines in the file with From as the first word')
