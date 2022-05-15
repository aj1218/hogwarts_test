import sys

import requests
import time

from jsonpath import jsonpath


url = "https://testgw.ininin.com"
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'applicationId': '1621914135658',
    'access_token': '226fcdf1-aac0-46ee-b51f-a4fea84bcd19',
    'Authorization': 'bearer 226fcdf1-aac0-46ee-b51f-a4fea84bcd19'
}


# 检查物流配置自动入库是否开启
def check_config():
    check_config_url = url + "/logistics/logistics_config/config_query"
    check_config_res = requests.request(url=check_config_url, method="GET", headers=headers).json()
    auto_stock_in = jsonpath(check_config_res, "$..autoStockIn")[0]
    if auto_stock_in == 0:
        print("物流配置没有开启自动入库，请开启！！！")
        sys.exit()
    else:
        print("物流配置已开启")


# 获取自动入库所需要的数据，组装入参（订单必须发送生管）
def auto_in_stock_data(po_no):
    # 排程列表查询数据
    collect_result_url = url + "/schedule/p_sch_collect/collect_result_summary"
    collect_result_data = {"sort_type":1,"start_create_time":"","end_create_time":"","c_mac_id":"","search_order_no":po_no,"start_plan_time":"","end_plan_time":"","current_page":1,"page_size":100}
    collect_result_res = requests.request(url=collect_result_url, method="POST", headers=headers, json=collect_result_data).json()
    p_sch_collect_id = jsonpath(collect_result_res, "$..p_sch_collect_id")[0]
    # 排程列表点击查询到的数据获取详细信息
    collect_result_detail_url = url + "/schedule/p_sch_scheme/list_sch_scheme_statistics"
    collect_result_detail_data = {"p_sch_collect_id":p_sch_collect_id,"search_ptname_st":"","search_order_no":po_no,"cor_type":"","query_pa_type":"","prod_fk":None,"send_flag":""}
    collect_result_detail_res = requests.request(url=collect_result_detail_url, method="POST", headers=headers, json=collect_result_detail_data).json()
    print("{} 获取到详请，生成自动入库参数".format(po_no))
    # 自动入库参数组装
    data = {"avg_speed":12,"band_no":"B","index_no":0,"line":"9","order_remark":"平压，重点客户，保证质量，不能少数","ph1":503,"ph10":0,"ph11":0,"ph12":0,"ph2":300,"ph3":503,"ph4":0,"ph5":0,"ph6":0,"ph7":0,"ph8":0,"ph9":0,"press_type":"2","ptname_st":"中山横栏瑞影","quantity_bad":12,"stop_time":"0","stop_time_sec":0,"stop_times":0,"total_len":662,"work_date":"2022-01-07","worktime_sec":221}
    fk = jsonpath(collect_result_detail_res, "$..fk_inch")[0]
    if "/" in fk:
        data["borda_fk"] = fk.split("/")[0]  # 幅宽
        data["borda_inch"] = fk.split("/")[1]  # 纸度
    else:
        data["borda_fk"] = fk
        data["borda_inch"] = 0
    data["borda_ks"] = jsonpath(collect_result_detail_res, "$..u_zk")[0]  # 开数
    data["borda_l"] = jsonpath(collect_result_detail_res, "$..u_borda_l")[0]  # 长
    data["borda_w"] = jsonpath(collect_result_detail_res, "$..u_borda_w")[0]  # 宽
    data["borda_quantity"] = jsonpath(collect_result_detail_res, "$..u_order_quantity")[0]  # 订单数量
    data["borda_xb"] = jsonpath(collect_result_detail_res, "$..prod_xb")[0]  # 修边
    data["cor_type"] = jsonpath(collect_result_detail_res, "$..cor_type")[0]  # 楞型

    data["p_sch_collect_no"] = jsonpath(collect_result_detail_res, "$..p_sch_collect_no")[0]  # 排程单号
    pa_work_list = ["pa1_work", "pa2_work", "pa3_work", "pa4_work", "pa5_work", "pa6_work", "pa7_work"]
    for pa_work in pa_work_list:
        data[pa_work] = jsonpath(collect_result_detail_res, "$..{}".format(pa_work))[0]  # pa1 -- pa7 纸占
        if not data[pa_work]:
            data[pa_work] = ""

    data["pa_type_work"] = jsonpath(collect_result_detail_res, "$..work_pa_type_order")[0]  # 材质
    data["po_no"] = jsonpath(collect_result_detail_res, "$..u_order_no")[0]  # 订单号
    data["quantity_good"] = jsonpath(collect_result_detail_res, "$..u_hk")[0]  # 横开  横开 * 开数 = 订单数
    data["start_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))  # 开始时间
    data["end_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 结束时间
    print("{} 自动入库参数：{}".format(po_no, data))
    return data


# 自动入库
def auto_in_stocking(po_no):
    stock_data = auto_in_stock_data(po_no)
    print("开始调用自动入库接口...")
    auto_in_stocking_url = url + "/schedule/production_management/sync_finish_recycle_erp"
    auto_in_stocking_res = requests.request(url=auto_in_stocking_url, method="POST", headers=headers, json=stock_data).json()
    print("自动入库返回结果：", auto_in_stocking_res)


if __name__ == "__main__":
    check_config()
    auto_in_stocking("2203285437")
