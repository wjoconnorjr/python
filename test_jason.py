#!/usr/local/bin/python3

import json

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}
loopcount = 0

def display_two(obj):
   global loopcount
   loopcount += 1
   leading = "->" * loopcount
   try:
      for key,val in obj.items():
         if isinstance(val,dict):
            print("{} {} ->".format(leading,key))
            display_two(val)
         elif isinstance(val, list):
            listcount = 0
            for i in val:
               listcount += 1
               print ("{} {} -> [{}]".format(leading,key,listcount))
               display_two(i)
         else:
            print ('{} {} = {}'.format(leading,key,val ))
   except AttributeError:
      print ("------ Leading with list --------")
      listcount = 0
      for i in obj:
          listcount += 1
          print ("{} List Count -> [{}]".format(leading,listcount))
          display_two(i)
   loopcount -= 1

# data
#
#print ('Data')
#json_str = json.dumps(data)
#display_two(data)
#for key, val in data.items():
#    print ('{0} = {1}'.format(key, val))

# data1
#
#print ('\nData1')
#with open('data1.json', 'r') as f:
#     data1 = json.load(f)
#display_two(data1)

# data2
#
#print ('\nData2')
#with open('data2.json', 'r') as f:
#     data2 = json.load(f)
#
#display_two(data2)
#
# data3
#
#print ('\nData3')
#with open('data3.json', 'r') as f:
#     data3 = json.load(f)
#
#display_two(data3)
#
#
# data4
#
#print ('\nData4')
#with open('data4.json', 'r') as f:
#     data4 = json.load(f)
#
#display_two(data4)
#
# data5
#
#print ('\nData5')
#with open('data5.json', 'r') as f:
#     data5 = json.load(f)
#
#display_two(data5)
#
# UC
#
print ('\nUC')
with open('uc.json', 'r') as f:
     uc = json.load(f)
display_two(uc)

