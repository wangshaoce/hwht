import random

from business.get_order_info import *


class Statistics(object):
    """
    这里罗列了各个数据统计函数，为前端的统计图提供合法数据
    """
    hw_order_num = ["Android", "iOS", "iPad", "Android-Pad", "其他"]
    group = ["用户组", "专项质量组", "播端组", "营收活动组", "质量运营组"]

    @classmethod
    def hw_order_num_pie_chart(cls):
        """
        各个平台的饼状图统计信息
        :return: [{value: XX, name: '设备平台'},{value: XX, name: '设备平台'}]
        """
        res = {
            "code": 20000,
            "message": "平台饼状图数据查询成功",
            "data": {
                "items": []
            }
        }
        mobile = MobileBusiness()
        for i in cls.hw_order_num:
            count = mobile.query_by_mobile_key_words(**{"hw_order_num": i})['data']["total"]
            res["data"]["items"].append({"value": count, "name": i})
        return res

    @classmethod
    def group_pie_chart(cls):
        """
        各个部门各个平台的饼状图统计信息
        :return:
        [
      ['XXX', '平台1', '平台2', '平台3', '平台4','平台5','平台6'],
      ['部门1', 41.1, 30.4, 65.1, 53.3,12,34],
      ['部门2', 86.5, 92.1, 85.7, 83.1,45,34],
      ['部门3', 24.1, 67.2, 79.5, 86.4,18,02],
      ['部门4', 24.1, 67.2, 79.5, 86.4,18,87],
      ['部门5', 24.1, 67.2, 79.5, 86.4,18,75]
      .......
        ]
        """
        res = {
            "code": 20000,
            "message": "各个部门各个平台的饼状图数据查询成功",
            "data": {
                "items": []
            }
        }
        mobile = MobileBusiness()
        res["data"]["items"].append(['hw_order_num']+cls.hw_order_num)
        for g in cls.group:
            temp = [g]
            for p in cls.hw_order_num:
                temp.append(mobile.query_by_mobile_key_words(**{"hw_order_num": p, "order_pic": g})['data']["total"])
            res["data"]["items"].append(temp)
        return res

