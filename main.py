import time

from dbpool import Pool
from gouhaowang import GouHaoWang
from model import Phone, Region


def get_area():
    area_map = {}
    with Pool.scope_session() as session:
        for province, city, area_code, in session.query(
                Region.province, Region.city, Region.area_code):
            area_map[f"{province}、{city}"] = area_code
    return area_map


area_map = get_area()


def insert_to_db(infos: list):
    with Pool.scope_session() as session:
        session.bulk_insert_mappings(Phone, [{
            'number': info[0],
            'area_code': area_map.get(info[1]),
            'operator_id': info[2]
        } for info in infos])


if __name__ == '__main__':
    # 生成号段
    # 查询号段信息
    ghw = GouHaoWang()
    for number in range(155, 156):
        infos = ghw.get_info(str(number))
        print(f"{number}数量： {len(infos)}")
        if infos:
            insert_to_db(infos)
    # with open("./msisdn_seg.txt", "r") as fr:
    #     data = fr.read()
    #
    # with open("./msisdn.txt", "r") as fr:
    #     data1 = fr.read()
    # data1 = set([s[:7] for s in data1.split("\n")])
    # data = set(data.split("\n"))
    # ip138 = Ip138()
    # print(len(data - data1))
    # for number_seg in data - data1:
    #     if not number_seg:
    #         continue
    #     time.sleep(3)
    #     try:
    #         info = ip138.get_info(number_seg)
    #     except Exception as e:
    #         print(e)
    #         continue
    #     print(info)
    #     with open("./msisdn.txt", "a+") as fw:
    #         fw.write(info + "\n")
