import os 
import json
cmd = ''' curl http://localhost:5000/a2/api/insertOrder -d "Name=name1&buyer= buyer1&seller=seller1&orderItems=111000" -X POST -v'''
print os.system(cmd)
cmd = ''' curl http://localhost:5000/a2/api/insertOrder -d "Name=name2&buyer= buyer2&seller=seller1&orderItems=101000" -X POST -v'''
print os.system(cmd)
cmd = ''' curl http://localhost:5000/a2/api/insertOrder -d "Name=name3&buyer= buyer3&seller=seller1&orderItems=001000" -X POST -v'''
print os.system(cmd)
cmd = ''' curl http://localhost:5000/a2/api/insertOrder -d "Name=name6&buyer= buyer6&seller=seller1&orderItems=011000" -X POST -v'''
print os.system(cmd)
cmd = ''' curl http://localhost:5000/a2/api/insertOrder -d "Name=name4&buyer= buyer4&seller=seller1&orderItems=110000" -X POST -v'''
print os.system(cmd)
cmd = ''' curl http://localhost:5000/a2/api/insertOrder -d "Name=name5&buyer= buyer5&seller=seller1&orderItems=010000" -X POST -v'''


# result = json.loads( os.system(cmd) )   
print os.system(cmd)