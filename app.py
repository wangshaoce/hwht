import json
import time
from flask import Flask, request, make_response
from flask_cors import *
# app = Flask(__name__)
from business.get_order_info import MobileBusiness
from models.model_base import app
from business.get_shop_info import AdminBusiness
from business.statistics import *


@app.route('/')
@cross_origin()
def hello_world():
    return "hello world"


@app.route('/mobile/query', methods=['POST'])
@cross_origin()
def query_all_mobile():
    """
    全体设备查询
    :return: 所有设备信息
    """
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return MobileBusiness().all_mobile_query(**data)


@app.route('/mobile/key_query', methods=['POST'])
@cross_origin()
def query_key_mobile():
    """
    设备关键字查询，支持前端post自定义key与value，如：{"platform":"Android"}
    :return:所有匹配设备信息
    """
    print(request.get_json())
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return MobileBusiness().query_by_mobile_key_words(**data)


@app.route('/mobile/add', methods=['POST'])
@cross_origin()
def add_mobile():
    """
    全体设备查询
    :return: 所有设备信息
    """
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return MobileBusiness().add_mobile_info(**data)


@app.route('/mobile/update', methods=['POST'])
@cross_origin()
def update_mobile():
    """
    修改设备数据，使其与post数据一致，ps：不支持修改唯一确定值 shop_id
    :return:成功与否
    """
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return MobileBusiness().edit_mobile_info(**data)
@app.route('/mobile/update_dim', methods=['POST'])
@cross_origin()
def dim_update_mobile():
    """
    修改设备数据，使其与post数据一致，ps：不支持修改唯一确定值 shop_id
    :return:成功与否
    """
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return MobileBusiness().edit_mobile_info_with_dim(**data)


@app.route('/mobile/delete', methods=['POST'])
@cross_origin()
def delete_mobile():
    """
    删除指定手机设备，使其状态变为"deleted"
    :return:成功与否
    """
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return MobileBusiness().delete_mobile_info(**data)


@app.route('/borrow/query', methods=['GET'])
@cross_origin()
def query_all_borrow():
    """
    全体借用记录查询
    :return: 所有借用记录
    """
    return BorrowBusiness().all_borrow_query()


@app.route('/mobile/borrow_key_query', methods=['POST'])
@cross_origin()
def query_key_borrow():
    """
    设备关键字查询，支持前端post自定义key与value，如：{"mobile_name": "锤子"}
    :return:所有匹配借用记录
    """
    data = request.get_json()
    print(request.get_json())
    if not data:
        data = {}
    return BorrowBusiness().query_by_borrow_key_words(**data)

@app.route('/mobile/check_key_query', methods=['POST'])
@cross_origin()
def query_key_check():
    """
    设备关键字查询，支持前端post自定义key与value，如：{"mobile_name": "锤子"}
    :return:
    """
    data = request.get_json()
    print(request.get_json())
    if not data:
        data = {}
    return CheckBusiness.query_by_check_key_words(**data)

@app.route('/mobile/check_key_info', methods=['POST'])
@cross_origin()
def check_key_info():
    """
    设备关键字查询，支持前端post自定义key与value，如：{"mobile_name": "锤子"}
    :return:所有匹配借用记录
    """
    data = request.get_json()
    print(request.get_json())
    if not data:
        data = {}
    return BorrowBusiness().query_by_borrow_key_words(**data)


@app.route('/mobile/adminList', methods=['POST'])
@cross_origin()
def query_admin():
    """
    管理员列表查询
    """
    return AdminBusiness.all_admin_query()


@app.route('/mobile/borrow', methods=['POST'])
@cross_origin()
def borrow_mobile():
    """
    借用手机
    :return:
    """
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return BorrowBusiness().add_borrow_info(data)

@app.route('/mobile/check', methods=['POST'])
@cross_origin()
def check_info():
    """
    设备盘点
    :return:
    """
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return CheckBusiness.add_check_info(data)

@app.route('/mobile/check_borrow', methods=['POST'])
@cross_origin()
def check_borrow():
    """
    借用手机
    :return:
    """
    data = request.get_json()
    print(data)
    if not data:
        data = {}
    return BorrowBusiness().check_borrow_info(**data)


@app.route('/mobile/revert', methods=['POST'])
@cross_origin()
def revert_mobile():
    """
    归还手机
    :return:
    """
    data = request.get_json()
    return BorrowBusiness.revert_borrow_info(**data)


@app.route('/mobile/tongji_platform', methods=['POST'])
@cross_origin()
def statistics_platform():
    """
    平台饼状图数据
    :return:
    """
    return Statistics.platform_pie_chart()


@app.route('/mobile/tongji_group', methods=['POST'])
@cross_origin()
def statistics_group():
    """
    各个部门各个平台的饼状图统计信息
    :return:
    """
    return Statistics.group_pie_chart()


@app.route('/monitor/ping', methods=['GET'])
@cross_origin()
def monitor_ping():
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug='True')
