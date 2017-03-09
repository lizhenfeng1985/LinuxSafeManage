import socket
import struct


# 808 4
def TCPGetMesg(op_type, uid, sub_pid, obj_pid, sub_path, obj_src_path, obj_dst_path):
    addr = ('localhost', 9002)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)

    data = struct.pack("4I264s264s264s", op_type, uid, sub_pid, obj_pid, sub_path, obj_src_path, obj_dst_path)
    s = client.send(data)
    recvdata = client.recv(4)
    rt = struct.unpack("I", recvdata)[0]
    return rt

