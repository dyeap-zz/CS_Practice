def processLogFile(logs, threshold):
    def update_dict(d, t):
        if t not in d:
            d[t] = 1
        else:
            d[t] += 1

    res = []
    d = {}
    print(logs)
    for transaction in logs:
        t1, t2, _ = transaction.split(" ")
        if t1 == t2:
            update_dict(d, t1)
        else:
            update_dict(d, t1)
            update_dict(d, t2)

    for t, occ in d.items():
        if occ >= threshold:
            res.append(t)

    res.sort(key=lambda x: (x[0]))
    return res