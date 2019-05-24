import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

# a = {1,2,1,'hello'}
# c = 2;
# b = {'k1':1,'k2':2,'k2':2.1,'k4':'Hello'}
# if c == 1:
# 	print 1111
# elif c == 2:
# 	print 2222
# else:
# 	print 3333

# #while c < 10:
# 	print c
# 	c += 1;

# #for x in xrange(1,5):
# #	print x

# #for key,value in b.items():
# #	print key, value

# #for key in b.keys():
# #	print key

# for i in xrange(1,10):
# 	if (i == 5):
# 		continue
# 	print i

# a = time.time()
# print a
# print type(a)

# fw = open('data.txt','w')

# for x in xrange(1,10):
# 	fw.write(str(x))
# fw.close()

# fr = open('data.txt','r')
# for line in fr:
# 	line = line.strip()
# 	print line

# fr.close()

#/exception code -->try:
# try:
# 	print i
# except Exception, e:
# 	print e
# else:
# 	print 'No Error'
# finally:
# 	print 'it will be implemented'

def hello(name):
	print 'Hello' + name

hello('mmc')
hello('python')