import os 
for x in xrange(11,20):
	cmd = ''' curl http://localhost:5000/a2/api/insertOrder -d "ID=7&Name=2&buyer=3&seller=4&orderItems=5" -X POST -v'''
result = json.loads( os.system(cmd) )   
print result