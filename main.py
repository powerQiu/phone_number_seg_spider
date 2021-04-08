from gouhaowang import GouHaoWang


if __name__ == '__main__':
    # 生成号段
    # 查询号段信息
    ghw = GouHaoWang()
    for number in range(155, 156):
        infos = ghw.get_info(str(number))
        print(f"{number}数量： {len(infos)}")
