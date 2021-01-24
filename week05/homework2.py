import redis
import datetime



def dealTimeStamp(oldTimeStr1, youngTimeStr2):
    time2 = datetime.datetime.strptime(youngTimeStr2.split('.')[0], "%Y-%m-%d %H:%M:%S")
    time1 = datetime.datetime.strptime(oldTimeStr1.split('.')[0], "%Y-%m-%d %H:%M:%S")
    seco = (time2 - time1).seconds
    return seco


def splitContext(context, strLen):  # 发送内容超70，拆成多条发送,每条长度为 strLen
    ret = []
    r = ''
    step = 1
    # strLen = 2
    for idx, char in enumerate(context):
        if len(context) - idx >= strLen:
            if step < strLen:
                r = r + char
                step += 1
            else:
                step = 1
                r = r + char
                ret.append(r)
                r = ''
        else:
            ret.append(context[idx:])
            break

    return ret


def sendsms(redisClient, telephone_number, content):
    counterInfo = redisClient.get(telephone_number).decode('utf-8')
    timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(counterInfo)
    count, timeSecond = counterInfo.split('_')
    sec = dealTimeStamp(timeSecond, timenow)

    if int(sec) < 5:
        if int(count) >= 5:
            print('wait 60s')
        else:
            if len(content) > 10: # 大于10 拆开发送
                for line in splitContext(context=content, strLen=5):
                    print("sendto:{} msg:{}".format(telephone_number, line))
                    # 此处，拆分开的多条还是当成一次发送
                    # 若要将多条单独判断发送条数，则需要在此处获取 redis中 之前的发送次数及时间
                    # 需将 判断发送次数及时间的动作 再次进行封装 调用
                    redisClient.set(telephone_number, str(int(count) + 1) + '_' + timenow)
            else:
                print("sendto:{} msg:{}".format(telephone_number, content))
                redisClient.set(telephone_number, str(int(count) + 1) + '_' + timenow)
    else:
        count = 0
        if len(content) > 10:
            for line in splitContext(context=content, strLen=5):
                print("sendto:{} msg:{}".format(telephone_number, line))
                redisClient.set(telephone_number, str(int(count) + 1) + '_' + timenow)
        else:
            print("sendto:{} msg:{}".format(telephone_number, content))
            redisClient.set(telephone_number, str(int(count) + 1) + '_' + timenow)



if __name__ == '__main__':
    client = redis.Redis(host='192.168.109.140', password='tmppass1234')
    # 问题：redis 保存 k - v 键值对，这个v 怎么保存 复合数据 如 k ：[count,updateTime]
    client.set('12345654321', '0_{}'.format(datetime.datetime.now()), nx=True)

    sendsms(redisClient=client, telephone_number='12345654321', content='halo hello nihao abcdefghijk')

    print(client.get('12345654321'))

    
