import random
import datetime

from models.oder_info import *
from flask import current_app


class MobileBusiness(object):
    """
    增查：手机设备表
    """
    # 数据库所有相关字段
    key_words = ["shop_id", "shop_name", "order_num", "hw_order_num", "zhuandan_price", "sale_price", "order_status",
                 "order_detail",
                 "order_pic", "order_time"]
    per_page = 50

    @classmethod
    def base_mobile_query(cls):
        # 基础查询语句
        query = Order.query.add_columns(
            Order.shop_id.label('shop_id'),
            Order.shop_name.label('shop_name'),
            Order.order_num.label('order_num'),
            Order.hw_order_num.label('hw_order_num'),
            Order.zhuandan_price.label('zhuandan_price'),
            Order.sale_price.label('sale_price'),
            Order.order_status.label('order_status'),
            Order.order_detail.label('order_detail'),
            Order.order_pic.label('order_pic'),
            Order.order_time.label('order_time')
        )
        return query

    @classmethod
    def all_mobile_query(cls, **kwargs):
        """
        全体查询
        """
        if kwargs.get("page"):
            page = int(kwargs.get("page"))
        else:
            page = 1
        query = cls.base_mobile_query()
        # 这里对数据库做第一次查询
        data = query.filter(Order.order_status is not None).limit(cls.per_page).offset((page - 1) * cls.per_page).all()
        print(data)
        length = len(query.filter(Order.order_status is not None).all())
        data_list = []
        for i in data:
            data_list.append(list(i[1:]))
        res = {
            "code": 20000,
            "message": "订单查询成功",
            "data": {
                "total": length,
                "items": []
            }
        }
        for row in data_list:
            res["data"]["items"].append({
                "shop_id": row[0],
                "shop_name": row[1],
                "order_num": row[2],
                "hw_order_num": row[3],
                "zhuandan_price": row[4],
                "sale_price": row[5],
                "order_status": row[6],
                "order_detail": row[7],
                "order_pic": row[8]
            })
        db.session.close()
        return res

    @classmethod
    def query_by_mobile_key_words(cls, **kwargs):
        """
        根据关键字查询
        :param kwargs: 包含查询字段key_words和value值,支持多个字段，如：{"hw_order_num":"Android","order_num": "三星"}
        :return: 若所有key不存在于设备列中，返回False,否则返回查询结果
        """
        if kwargs.get("page"):
            page = int(kwargs.get("page"))
        else:
            page = 1
        data = cls.base_mobile_query().filter(Order.order_status is not None)
        if kwargs.get("start_time"):
            data = data.filter(Order.order_time < kwargs.get('end_time')).filter(Order.order_time >=
                                                                                 kwargs.get('start_time'))
        else:
            data = cls.base_mobile_query().filter(Order.order_status is not None)
        # data = cls.base_mobile_query().filter(Order.order_status is not None)
        for i in cls.key_words:

            if kwargs.get(i):
                if i == 'hw_order_num' or i == 'order_pic':  # 精准匹配
                    if i == 'hw_order_num' and kwargs.get(i) == '其他':
                        data = data.filter(getattr(Order, i).notlike("%" + 'iOS' + "%"))
                        data = data.filter(getattr(Order, i).notlike("%" + 'Android' + "%"))
                        data = data.filter(getattr(Order, i).notlike("%" + 'iPad' + "%"))
                        data = data.filter(getattr(Order, i).notlike("%" + 'Android-Pad' + "%"))
                    else:
                        data = data.filter(getattr(Order, i) == kwargs.get(i))
                    continue
                else:  # 模糊匹配
                    data = data.filter(getattr(Order, i).like("%" + kwargs.get(i) + "%"))
        length = len(data.all())
        data = data.limit(cls.per_page).offset((page - 1) * cls.per_page).all()
        data_list = []
        for j in data:
            data_list.append(list(j[1:]))
        res = {
            "code": 20000,
            "data": {
                "total": length,
                "items": []
            },
            "message": "查询数据成功"
        }
        for row in data_list:
            # row[9] =row[9].strftime('%Y-%m-%d')
            res["data"]["items"].append({
                "shop_id": row[0],
                "shop_name": row[1],
                "order_num": row[2],
                "hw_order_num": row[3],
                "zhuandan_price": row[4],
                "sale_price": row[5],
                "order_status": row[6],
                "order_detail": row[7],
                "order_pic": row[8],
                "order_time": row[9].strftime('%Y-%m-%d')

            })
        print(res)
        return res

    @classmethod
    def add_mobile_info(cls, **context):
        """
        :param context: dict形式，必须拥有上面key_words关键字
        :return: 添加结果
        """
        try:
            addinfo = Order(shop_id=context["shop_id"],
                            shop_name=context["shop_name"], order_num=context["order_num"],
                            hw_order_num=context["hw_order_num"],
                            zhuandan_price=context["zhuandan_price"],
                            device_version=context["device_version"], order_status=context["order_status"],
                            remarks=context["remarks"], sale_price=context["sale_price"],
                            order_detail=context["order_detail"],
                            order_pic=context["order_pic"], user_person=context["user_person"],
                            borrow=False)
            db.session.add(addinfo)
            db.session.commit()
            return {
                "code": 20000,
                "message": True,
                "data": "数据库添加成功"
            }
        except Exception as e:
            return {
                "code": 202,
                "message": "123",
                "data": "手机设备信息添加失败"
            }

    @classmethod
    def edit_mobile_info(cls, **kwargs):
        try:
            kwargs["borrow"] = False
            data = Order.query.filter_by(shop_id=kwargs.get("shop_id"))
            data.update(kwargs)
            db.session.commit()
            return {
                "code": 20000,
                "message": True,
                "data": "手机设备信息更新成功"
            }
        except Exception as e:
            print(e)
            return {
                "code": 202,
                "message": "手机设备信息更新失败",
                "data": "手机设备信息更新失败"
            }

    @classmethod
    def edit_mobile_info_with_dim(cls, **kwargs):
        # data = cls.base_mobile_query().filter(Order.order_status != "deleted")
        try:
            datas = cls.query_by_mobile_key_words(**kwargs)
            for data in datas['data']['items']:
                union = Order.query.filter_by(shop_name=data['shop_name'])
                # print('循环里的数据是'+data['shop_name'])
                kwargs['shop_name'] = data['shop_name']
                print('************')
                print(kwargs)
                print('*************')
                union.update(kwargs)
            db.session.commit()
            return {
                "code": 20000,
                "message": True,
                "data": "手机设备信息更新成功"
            }
        except Exception as e:
            print(e)
            return {
                "code": 202,
                "message": "手机设备信息更新失败",
                "data": "手机设备信息更新失败"
            }

    @classmethod
    def delete_mobile_info(cls, **kwargs):
        try:
            data = Order.query.filter_by(shop_id=kwargs.get("shop_id"))
            data.update({"order_status": "deleted"})
            data.update({"shop_id": kwargs.get("shop_id") + str(random.randint(100000, 999999))})
            db.session.commit()
            return {
                "code": 20000,
                "message": "手机设备信息删除成功",
                "data": "手机设备信息删除成功"
            }
        except Exception as e:
            return {
                "code": 202,
                "message": "123",
                "data": "手机设备信息删除失败"
            }
