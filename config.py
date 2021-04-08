# 数据库配置
db_pool_size = 10
db_max_overflow = 100
db_pool_recycle = 1 * 60 * 60
# 数据库用户名
db_user = "root"
# 数据库密码
db_pwd = ""
# 数据库端口
db_port = "3306"
# 数据库名
db_name = "mydb"
# 数据库IP
db_host = "127.0.0.1"
# 数据库连接
db_uri = (
    f'mysql+pymysql://'
    f'{db_user}:{db_pwd}@{db_host}:{db_port}/'
    f'{db_name}?charset=utf8'
)

