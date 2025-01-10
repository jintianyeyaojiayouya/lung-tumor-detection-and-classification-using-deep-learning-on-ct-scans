# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# logconf.py
import logging

# 配置日志的格式
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
    level=logging.DEBUG  # 设置日志级别为 DEBUG，可以根据需求改为INFO、ERROR等
)

# 创建一个日志记录器
logger = logging.getLogger(__name__)

# 这个logger可以在其他模块中导入并使用
def log_message():
    logger.info("This is an info message.")
    logger.error("This is an error message.")
    logger.debug("This is a debug message.")