import sys
reload(sys)
sys.setdefaultencoding('utf8')

fr = open('xyj.txt','r')

characers = []
stat = {}

for line in fr:
	line = line.strip()

	if len(line) == 0:
		continue
	
	print type(line)
	line = unicode(line)
	print type(line)

	for x in xrange(0,len(line)):
		if not line[x] in characers:
			characers.append(unicode(line[x]))
		if not stat.has_key(line[x]):
			stat[line[x]] = 0
		stat[line[x]] += 1
print len(characers)
# print characers
# print len(stat)
# for key,value in stat.items():
# 	print key,value
stat = sorted(stat.iteritems(), key=lambda d:d[1],reverse=True)
print type(stat),len(stat)

for x in xrange(0,20):
	print characers[x]
print '*' * 20
for x in xrange(0, 20):
	print stat[x][0],stat[x][1]
fr.close()