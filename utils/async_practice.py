"""
    协程的使用
"""

import asyncio
import time
import logging
import os
import threading

# asyncio使用logging来记录日志，所有的日志记录都是使用asyncio logger来执行的,这里是设置asyncio记录的日志
# 前提是必须开启调试模式
from asyncio import FIRST_COMPLETED

asyncio_logger = logging.getLogger("asyncio")
asyncio_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('./asyncio.log', 'a')
asyncio_logger.addHandler(file_handler)


# async def customer_time():
#     """
#         模拟一个耗时操作
#     :return:
#     """
#     print('start_sleep')
#     await asyncio.shield(asyncio.sleep(2))
#
#
# async def customer_time2(delay):
#     """
#         模拟一个耗时操作
#     :return:
#     """
#
#     await asyncio.shield(asyncio.sleep(delay))
#     print('finish')
#
#
# async def spend_time():
#     await asyncio.sleep(3600)
#
#
# async def add(x, y):
#     if y == 0:
#         raise Exception('zero')
#     print(x / y)
#     return x / y
#
#
# # 定义一个协程函数,协程函数加括号不是函数调用，而是生成了一个协程对象
# async def main():
#     print('hello')
#     # await customer_time()
#     # await customer_time()
#
#     # 当一个协程通过 asyncio.create_task() 等函数被打包为一个任务,该协程将自动排入日程准备立即运行
#     # https://docs.python.org/zh-cn/3/library/asyncio-task.html
#     task1 = asyncio.create_task(customer_time(), name='customer_time')
#     current_loop = asyncio.get_event_loop()
#     print(current_loop)
#     # 获取任务的名称
#     print(task1.get_name())
#     task2 = asyncio.create_task(customer_time())
#     await task1
#     await task2
#
#     # 并发运行任务
#     task_list = [add(1, 2), add(2, 0)]
#     # 并发运行序列中的可等待对象,如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与序列可等待对象的顺序一致。
#     # 如果return_exceptions=False，异常会立即传播，并且不会影响其他协程或者是任务的执行状态，
#     # 如果return_exceptions=True将会和结果一起聚合到结果列表中去
#     # 如果 gather() 被取消，所有被提交 (尚未完成) 的可等待对象也会 被取消
#     result_list = await asyncio.gather(*task_list, return_exceptions=True)
#
#     # 等待序列中的可等待对象完成，指定timeout秒后超时,如果timeout为None，则等待直到完成为止
#     # 如果发生超时，则任务将会被取消,如果等待被取消，则序列中的任务也会被取消
#     try:
#         await asyncio.wait_for(spend_time(), timeout=2)
#     except asyncio.TimeoutError:
#         print('timeout')
#
#     # 并发的运行序列中的可等待对象，直到满足return_when的条件
#     # 常用的return_when的条件包括:ALL_COMPLETED(全部完成或者取消), FIRST_EXCEPTION(遇到第一个异常就取消)
#     # FIRST_COMPLETED(第一个执行完成就取消)
#     # wait在超时发生的时候不会取消可等待对象
#     print('8' * 999)
#     list_task = [customer_time2(2), customer_time2(3)]
#     done, pending = await asyncio.wait(list_task, return_when=FIRST_COMPLETED)
#     print(done, pending)
#     print('&' * 888)
#     # 获取所有的task
#     all_tasks = asyncio.all_tasks()
#     print(all_tasks)
#     print(result_list)
#
#     print('python')
def blocking_io(*args,  **kwargs):
    print(f"start blocking_io at {time.strftime('%X')}")
    print(f'args are {args}')
    print(f'kwargs are {kwargs}')
    time.sleep(1)
    print(f'current thread: {threading.current_thread()}')
    print(f"blocking_io complete at {time.strftime('%X')}")


async def test():
    print(11111)


async def submit_task(new_loop):
    # 向指定的事件循环提交一个线程安全的协程，返回一个Future对象
    asyncio.run_coroutine_threadsafe(test(), new_loop)


def start(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def main():

    print(f"started main at {time.strftime('%X')}")
    a = 1
    print(f'current thread: {threading.current_thread()}')
    await asyncio.gather(
        # 在不同的线程中异步的运行函数，向此函数提供的args和kwargs将会直接传递给该函数
        # 允许在不同的线程中访问来自事件循环的上下文变量。返回一个协程,python3.9新特性
        asyncio.to_thread(blocking_io, 1, 10, name='wangdong'),
        asyncio.sleep(1))

    # 创建一个新的事件循环，交给子线程去运行
    # new_loop = asyncio.new_event_loop()
    # th = threading.Thread(target=start, args=(new_loop,))
    # th.start()
    #
    # main_loop = asyncio.new_event_loop()
    # main_loop.run_until_complete(submit_task(new_loop))

    # 返回当前运行的task实例，没有正在运行的任务就返回None
    print(asyncio.current_task())

    # 返回事件循环中所有未完成的task集合
    print(asyncio.all_tasks())
    print(f"finished main at {time.strftime('%X')}")


if __name__ == '__main__':
    # print(f"started at {time.strftime('%X')}")

    # 一般用来运行最高层级的入口函数
    asyncio.run(main(), debug=False)
    # 创建一个新的事件循环
    loop = asyncio.new_event_loop()

    end_time = time.time()
    # print(f"finished at {time.strftime('%X')}")
