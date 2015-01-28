#-*- coding: UTF-8 -*- 

import json
import codecs
f = file('test.json')
jsonobj = json.load(f)
print jsonobj['link']
f.close()