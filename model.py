from sqlalchemy import Column, VARCHAR, Integer
from sqlalchemy.ext.declarative import declarative_base
Model = declarative_base()


class Region(Model):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, comment="序号")
    area_code = Column(VARCHAR(20), comment="区域编码")
    province = Column(VARCHAR(10), comment="省份")
    city = Column(VARCHAR(10), comment="城市")
    zip_code = Column(VARCHAR(50), comment="邮编")

    __table_args__ = {
        "mysql_charset": "UTF8MB3",
        "mysql_engine": "InnoDB",
        "comment": "区域信息"
    }


class Phone(Model):
    __tablename__ = "phone_number_info"

    number = Column(VARCHAR(7), primary_key=True, comment="号码段")
    area_code = Column(VARCHAR(20), comment="区域编码")
    operator_id = Column(VARCHAR(10), comment="运营商编码")

    __table_args__ = {
        "mysql_charset": "UTF8MB3",
        "mysql_engine": "InnoDB",
        "comment": "号段信息"
    }


if __name__ == '__main__':
    from sqlalchemy import create_engine
    import config

    engine = create_engine(config.db_uri)
    Model.metadata.create_all(engine)
