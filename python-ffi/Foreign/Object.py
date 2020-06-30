def _copyST(m):
    def _1():
        r = {}
        for k in m:
            r[k] = m[k]
        return r

    return _1


empty = {}


def runST(f):
    return f()


def _fmapObject(m0, f):
    m = {}
    for k in m0:
        m[k] = f(m0[k])

    return m


def _mapWithKey(m0, f):
    m = {}
    for k in m0:
        m[k] = f(k)(m0[k])

    return m


def _foldM(bind):
    def _1(f):
        def _2(mz):
            def _3(m):
                acc = mz

                def g(k):
                    def _4(z):
                        return f(z)(k)(m[k])

                    return _4

                for k in m:
                    acc = bind(acc)(g(k))

                return acc

            return _3

        return _2

    return _1


def _foldSCObject(m, z, f, fromMaybe):
    acc = z
    for k in m:
        maybeR = f(acc)(k)(m[k])
        r = fromMaybe(None)(maybeR)
        if r is None:
            return acc
        else:
            acc = r
    return acc


def all(f):
    def _1(m):
        for k in m:
            if not f(k)(m[k]):
                return False
        return True

    return _1


def size(m):
    return len(m)


def _lookup(no, yes, k, m):
    return yes(m[k]) if k in m else no


def _lookupST(no, yes, k, m):
    def _1():
        return yes(m[k]) if k in m else no

    return _1


def toArrayWithKey(f):
    def _1(m):
        r = []
        for k in m:
            r.append(f(k)(m[k]))
        return r

    return _1


keys = toArrayWithKey(lambda k: lambda: k)
