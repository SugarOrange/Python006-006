import redis

def counter(redisClient,vedioID):
    redisClient.incr(vedioID)
    return redisClient.get(vedioID)

if __name__ == '__main__':
    client = redis.Redis(host='192.168.109.140', password='tmppass1234')

    client.set(1001, 1, nx=True)
    client.set(1002, 7, nx=True)
    client.set(1003, 13, nx=True)

    for id in [1001,1002,1003]:
        print(counter(redisClient=client,vedioID=id))

        