import socket
from struct import *
from time import sleep

from data.user import user

# SOCKET_IP = "192.168.7.40"
# SOCKET_PORT = 30070

SOCKET_IP = "192.168.6.145"
SOCKET_PORT = 30080

"""
DWORD   L
WORD    H
BYTE    n
int     i
char    s
"""


def modify_growid(dwUserID, dwGrowID, nValue):
    """
    通过socket连接修改积分id
    :param dwUserID: 用户ID
    :param nValue: 积分增量修改值
    :param dwGrowID: 积分ID
    :return:
    """
    s = socket.socket()
    s.connect((SOCKET_IP, SOCKET_PORT))

    # 消息头
    dwMagic = 0
    dwSerial = 0
    wOrigine = 4
    wReserve = 0
    dwType = 207875
    dwParam = 0
    dwLength = 120

    # 消息体
    dwUserID = dwUserID
    dwMPID = 0
    dwGameID = 0
    dwPlatType = 0
    dwReserve1 = 0
    dwReserve2 = 0
    dwReserve3 = 0
    dwPort = 0

    tMatchBegin = b'0'
    dwTourneyID = 0
    dwMatchID = 0
    wGrowDomainID = 0
    dwRank = 0

    dwGrowID = dwGrowID
    nValue = nValue
    szNote = b'0'
    byOSType = 0
    dwAppID = 0
    dwSiteID = 0
    dwMoneyAcctType = 0

    pack_format = "2L2H3L8L4s2L1H2L1i64s1n3L"
    socket_data = pack(
        pack_format, dwMagic, dwSerial, wOrigine, wReserve, dwType, dwParam, dwLength, dwUserID, dwMPID, dwGameID,
        dwPlatType, dwReserve1, dwReserve2, dwReserve3, dwPort, tMatchBegin, dwTourneyID, dwMatchID, wGrowDomainID,
        dwRank, dwGrowID, nValue, szNote, byOSType, dwAppID, dwSiteID, dwMoneyAcctType
    )

    s.send(socket_data)
    chunk = s.recv(36)
    unpack_format = '2L2H3L3L'
    result = unpack(unpack_format, chunk)
    print(result)
    s.close()


def get_value_by_growid(dwUserID, dwGrowID):
    """
    通过socket连接获取积分id对应的值
    :param dwUserID: 用户ID
    :param dwGrowID: 积分ID
    :return:
    """
    s = socket.socket()
    s.connect((SOCKET_IP, SOCKET_PORT))

    # 消息头
    dwMagic = 0
    dwSerial = 0
    wOrigine = 4
    wReserve = 0
    dwType = 207881
    dwParam = 0
    dwLength = 52

    # 消息体
    dwUserID = dwUserID
    dwGrowID = dwGrowID

    dwMPID = 0

    dwGameID = 0
    dwPlatType = 0

    wReserve1 = 0
    byOSType = 0
    byReserve1 = 0
    dwAppID = 0
    dwSiteID = 0
    dwPort = 0

    pack_format = "2L2H3L5LH2n3L"
    socket_data = pack(
        pack_format, dwMagic, dwSerial, wOrigine, wReserve, dwType, dwParam, dwLength,
        dwUserID, dwGrowID, dwMPID, dwGameID, dwPlatType, wReserve1, byOSType, byReserve1, dwAppID,
        dwSiteID, dwPort
    )

    s.send(socket_data)
    chunk = s.recv(1024)
    unpack_format = '2L2H3L2L2H4L2L'
    result = unpack(unpack_format, chunk)
    print(result)
    s.close()


if __name__ == "__main__":
    dwUserID = 682033063
    dwGrowID = 49881005
    nValue = 1000
    get_value_by_growid(dwUserID, dwGrowID)
    modify_growid(dwUserID, dwGrowID, nValue)
    get_value_by_growid(dwUserID, dwGrowID)