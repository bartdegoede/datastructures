from queue import BasicQueue


def hot_potato(players, n):
    q = BasicQueue()
    for player in players:
        q.enqueue(player)

    while q.size > 1:
        # pass around the potato n times
        for _ in range(n):
            q.enqueue(q.dequeue())
        # remove player that holds the potato
        q.dequeue()

    return q.dequeue()


if __name__ == '__main__':
    assert(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7) == 'Susan')
    assert(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 1) == 'Kent')
