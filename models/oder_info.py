from models.model_base import *


class Order(db.Model):
    """
    手机数据库内各列参数
    """
    __tablename__ = "order"
    id = db.Column(db.Integer(),primary_key=True)
    shop_id = db.Column(db.Integer())  # 店铺id
    shop_name = db.Column(db.String(255))  # 店铺名称
    order_num = db.Column(db.Integer())  # 订单号
    hw_order_num = db.Column(db.Integer())  # 花娃订单号
    zhuandan_price = db.Column(db.Integer())  # 转单价格
    sale_price = db.Column(db.Integer())  # 销售价格
    order_status = db.Column(db.String(255))  # 订单状态
    order_detail = db.Column(db.String(255))  # 订单详情
    order_pic = db.Column(db.String(255))  # 订单图片链接
    order_time = db.Column(db.String(255))  # 订单时间

