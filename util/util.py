import collections
import copy
import datetime
import gc
import time

import numpy as np

from util.logconf import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# import logging

# # 配置日志记录
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
#     level=logging.DEBUG  # 设置日志级别为 DEBUG
# )

# # 获取一个日志记录器对象
# logger = logging.getLogger(__name__)  # 使用当前模块的名称作为日志记录器的名称

# def log_message():
#     logger.info("This is an info message.")
#     logger.error("This is an error message.")
#     logger.debug("This is a debug message.")


# # # 配置日志记录器
# # logging.basicConfig(
# #     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
# #     level=logging.INFO  # 设置日志级别为 INFO
# # )

# # # 获取一个日志记录器对象
# # logging = logging.getLogger(__name__)  # 使用当前模块的名称作为日志记录器的名称

IrcTuple = collections.namedtuple('IrcTuple', ['index', 'row', 'col'])
XyzTuple = collections.namedtuple('XyzTuple', ['x', 'y', 'z'])


def ire2xyz(coord_irc, origin_xyz, vxSize_xyz, direction_a):
    """
    Converts IRC coordinates to XYZ coordinates.
    """
    cri_a = np.array(coord_irc)[::-1]  # Reverse the order of IRC coordinates
    origin_a = np.array(origin_xyz)
    vxSize_a = np.array(vxSize_xyz)
    
    # Apply the transformation
    coords_xyz = (direction_a @ (cri_a * vxSize_a)) + origin_a
    
    return XyzTuple(*coords_xyz)

# def xyz2irc(coord_xyz, origin_xyz, vxSize_xyz, direction_a):
#     """
#     Converts XYZ coordinates to IRC coordinates.
#     """
#     coords_xyz = np.array(coord_xyz)
#     origin_a = np.array(origin_xyz)
#     vxSize_a = np.array(vxSize_xyz)
    
#     # Apply the transformation
#     cri_a = ((coords_xyz - origin_a) @ np.linalg.inv(direction_a)) / vxSize_a
    
#     # Round and return as IrcTuple
#     cri_a = np.round(cri_a)
#     return IrcTuple(int(cri_a[2]), int(cri_a[1]), int(cri_a[0]))

def xyz2irc(center_xyz, origin_xyz, vxSize_xyz, direction_a):
    """
    Converts XYZ coordinates to IRC coordinates.
    """
    coords_xyz = np.array(center_xyz)
    origin_a = np.array(origin_xyz)
    vxSize_a = np.array(vxSize_xyz)
    
    # Apply the transformation
    coords_irc = (np.dot(np.linalg.inv(direction_a), (coords_xyz - origin_a))) / vxSize_a
    
    # Ensure coordinates are valid
    coords_irc = np.clip(coords_irc, 0, None)  # Ensure non-negative values

    return IrcTuple(*np.round(coords_irc).astype(int))


def importstr(module_str,from_=None):
    # if from_ is None and ':' in module_str:
    #     module_str,from_=module_str.rsplit(':')
    # module = __import__(module_str)
    if from_ is None and ':' in module_str:
        # Split the string into module and class names if colon is found
        module_str, from_ = module_str.rsplit(':', 1)

    # Import the module first
    module = __import__(module_str, fromlist=[from_])

    if from_:
        # If there's a class or object name after the colon, return it
        return getattr(module, from_)
    
    # Otherwise, just return the module
    return module
# util.py

def enumerateWithEstimate(iterable, description='', start_ndx=0):
    # 示例：返回带有进度估计的 enumerate 版本
    total = len(iterable)
    for idx, item in enumerate(iterable, start=start_ndx):
        yield idx, item
        # 打印进度估计
        print(f"{description} {idx+1}/{total} processed")



# import collections
# import copy
# import datetime
# import gc
# import time

# import numpy as np

# # 配置日志记录
# import logging

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
#     level=logging.DEBUG  # 设置日志级别为 DEBUG
# )

# # 获取一个日志记录器对象
# logger = logging.getLogger(__name__)  # 使用当前模块的名称作为日志记录器的名称

# IrcTuple = collections.namedtuple('IrcTuple', ['index', 'row', 'col'])
# XyzTuple = collections.namedtuple('XyzTuple', ['x', 'y', 'z'])

# def ire2xyz(coord_irc, origin_xyz, vxSize_xyz, direction_a):
#     """
#     Converts IRC coordinates to XYZ coordinates.
#     """
#     cri_a = np.array(coord_irc)[::-1]  # Reverse the order of IRC coordinates
#     origin_a = np.array(origin_xyz)
#     vxSize_a = np.array(vxSize_xyz)
    
#     # Apply the transformation
#     coords_xyz = (direction_a @ (cri_a * vxSize_a)) + origin_a
    
#     return XyzTuple(*coords_xyz)

# def xyz2irc(coord_xyz, origin_xyz, vxSize_xyz, direction_a):
#     """
#     Converts XYZ coordinates to IRC coordinates.
#     """
#     coords_xyz = np.array(coord_xyz)
#     origin_a = np.array(origin_xyz)
#     vxSize_a = np.array(vxSize_xyz)
    
#     # Apply the transformation
#     cri_a = ((coords_xyz - origin_a) @ np.linalg.inv(direction_a)) / vxSize_a
    
#     # Round and return as IrcTuple
#     cri_a = np.round(cri_a)
#     return IrcTuple(int(cri_a[2]), int(cri_a[1]), int(cri_a[0]))

# def importstr(module_str, from_=None):
#     if from_ is None and ':' in module_str:
#         # Split the string into module and class names if colon is found
#         module_str, from_ = module_str.rsplit(':', 1)

#     # Import the module first
#     module = __import__(module_str, fromlist=[from_])

#     if from_:
#         # If there's a class or object name after the colon, return it
#         return getattr(module, from_)
    
#     # Otherwise, just return the module
#     return module




# import collections
# import copy
# import numpy as np
# import logging

# # 配置日志记录
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
#     level=logging.DEBUG  # 设置日志级别为 DEBUG
# )

# # 获取一个日志记录器对象
# logger = logging.getLogger(__name__)  # 使用当前模块的名称作为日志记录器的名称

# IrcTuple = collections.namedtuple('IrcTuple', ['index', 'row', 'col'])
# XyzTuple = collections.namedtuple('XyzTuple', ['x', 'y', 'z'])

# def ire2xyz(coord_irc, origin_xyz, vxSize_xyz, direction_a):
#     """
#     Converts IRC coordinates to XYZ coordinates.
#     """
#     cri_a = np.array(coord_irc)[::-1]  # Reverse the order of IRC coordinates
#     origin_a = np.array(origin_xyz)
#     vxSize_a = np.array(vxSize_xyz)
    
#     # Apply the transformation
#     coords_xyz = (direction_a @ (cri_a * vxSize_a)) + origin_a
    
#     return XyzTuple(*coords_xyz)

# def xyz2irc(coord_xyz, origin_xyz, vxSize_xyz, direction_a):
#     """
#     Converts XYZ coordinates to IRC coordinates.
#     """
#     coords_xyz = np.array(coord_xyz)
#     origin_a = np.array(origin_xyz)
#     vxSize_a = np.array(vxSize_xyz)
    
#     # Apply the transformation
#     cri_a = ((coords_xyz - origin_a) @ np.linalg.inv(direction_a)) / vxSize_a
    
#     # Round and return as IrcTuple
#     cri_a = np.round(cri_a)
#     return IrcTuple(int(cri_a[2]), int(cri_a[1]), int(cri_a[0]))

# def importstr(module_str, from_=None):
#     """
#     Import a module or class dynamically.
    
#     :param module_str: The module or class string to import, can include `:` to specify the class name.
#     :param from_: If provided, specifies the attribute (e.g., class or function) to return from the module.
#     :return: The imported module or class.
#     """
#     if from_ is None and ':' in module_str:
#         # Split the string into module and class names if colon is found
#         module_str, from_ = module_str.rsplit(':', 1)

#     # Import the module first
#     module = __import__(module_str, fromlist=[from_])

#     if from_:
#         # If there's a class or object name after the colon, return it
#         return getattr(module, from_)
    
#     # Otherwise, just return the module
#     return module
