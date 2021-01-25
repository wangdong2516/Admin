"""
    实现了服务器端代码
"""
import os
import sys

cur_path = os.path.abspath(os.path.join(os.path.dirname('__file__'), os.path.pardir))
print(cur_path)
sys.path.append(cur_path)

from example import format_data
from example import ttypes
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.server import TServer

_HOST = 'localhost'
_PORT = 9001


class FormatDataHandler(object):
    """
        handler定义
    """
    def do_format(self, data):
        print(data.text)
        print(data.id)

        return ttypes.Data(data.text.upper(), data.id)


if __name__ == '__main__':
    handler = FormatDataHandler()

    # 定义一个处理器，传递hanler，之后会调用
    processor = format_data.Processor(handler)

    # 设置监听的端口
    transport = TSocket.TServerSocket(_HOST, _PORT)

    # 定义传输方式,使用带有缓冲区的二进制传输
    tfactory = TTransport.TBufferedTransportFactory()

    # 定义传输的数据类型
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # 创建一个thrift服务，单进程阻塞的
    rpcServer = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the rpc server at', _HOST, ':', _PORT)
    rpcServer.serve()
    print('done')