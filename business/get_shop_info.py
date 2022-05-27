from models.shop import *


class AdminBusiness(object):
    """
    查：管理员列表
    """
    # 数据库所有相关字段
    key_words = ["admin_name"]

    @classmethod
    def base_admin_query(cls):
        # 基础查询语句
        query = AdminInfo.query.add_columns(
            AdminInfo.admin_name.label('admin_name'),
        )
        return query

    @classmethod
    def all_admin_query(cls):
        data_list = cls.base_admin_query().all()
        length = len(data_list)
        res = {
            "code": 20000,
            "message": "管理员查询成功",
            "data": {
                "total": length,
                "items": []
            }
        }
        for row in data_list:
            res["data"]["items"].append(row[1])
        db.session.close()
        return res