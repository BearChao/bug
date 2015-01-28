# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
import sqlite3


class JsonPipeline(object):
	def __init__(self):
		self.file = codecs.open('out.json','wb',encoding='utf-8')


	def process_item(self,item,spider):
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line.decode('unicode_escape'))
		return item
	
	
class SqlitePipeline(object):
	conn = []
	cursor = []
	def open_spider(self,spider):
		self.conn = sqlite3.connect('f:\data.db')
		self.cursor = self.conn.cursor()
		
	def process_item(self,item,Spider):
		sql = "insert into appinn (title,link) values ('"+item['title'][0]+"','"+item['link'][0]+"')"
		print sql
		self.cursor.execute(sql)

		return item
	def close_spider(self,spider):
		self.conn.commit()
		self.conn.close()