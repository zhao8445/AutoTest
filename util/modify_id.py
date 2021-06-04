import socket
from struct import *

SOCKET_IP = "192.168.7.40"
SOCKET_PORT = 30070


def modify_id(dwUserID, dwGrowID, nValue):
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
    dwLength = 140

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
    socket_data = pack(pack_format, dwMagic, dwSerial, wOrigine, wReserve, dwType, dwParam, dwLength,
                       dwUserID, dwMPID, dwGameID, dwPlatType, dwReserve1, dwReserve2, dwReserve3,
                       dwPort, tMatchBegin, dwTourneyID, dwMatchID, wGrowDomainID, dwRank,
                       dwGrowID, nValue, szNote, byOSType, dwAppID, dwSiteID, dwMoneyAcctType)

    s.send(socket_data)
    chunk = s.recv(1024)
    unpack_format = '9L'
    result = unpack(unpack_format, chunk)
    print(result)
    s.close()


if __name__ == "__main__":
    dwUserID = 210354482
    dwGrowID = 40160101
    nValue = 5
    modify_id(dwUserID, dwGrowID, nValue)
