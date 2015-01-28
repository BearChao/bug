# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义对象:
class Item(Base):
    # 表的名字:
    __tablename__ = 'appinn'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    title = Column(String(20))
    link = Column(String(100))

# 初始化数据库连接:
engine = create_engine('sqlite:///f:\data.db', echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()
# item = session.query(Item).filter(Item.id=='1').one()
# print item.title
# print item.link
new_item = Item(title='title',link='link')
session.add(new_item)
session.commit()
session.close()