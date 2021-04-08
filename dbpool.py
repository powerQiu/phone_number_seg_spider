from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

import config


class Pool:
    engine = create_engine(
        config.db_uri,
        pool_size=config.db_pool_size,
        pool_recycle=config.db_pool_recycle,  # 断开处理-乐观
        pool_pre_ping=True,  # 断开连接-悲观
        pool_use_lifo=True,
        poolclass=QueuePool,
        max_overflow=config.db_max_overflow,
    )
    DB_Session = sessionmaker(bind=engine)

    @classmethod
    @contextmanager
    def scope_session(cls):
        session = cls.DB_Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
