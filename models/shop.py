from models.model_base import *


class AdminInfo(db.Model):
    """
    手机数据库内各列参数
    """
    __tablename__ = "shop"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255)) #店铺名称
    owner = db.Column(db.String(255))# 店铺管理员名称
