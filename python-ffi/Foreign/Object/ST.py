def new():
    return {}


def peekImpl(just):
    def _1(nothing):
        def _2(k):
            def _3(m):
                def _4():
                    return just(m[k]) if k in m else nothing

                return _4

            return _3

        return _2

    return _1


def poke(k):
    def _1(v):
        def _2(m):
            def _3():
                m[k] = v
                return m

            return _3

        return _2

    return _1


def delete(k):
    def _1(m):
        def _2():
            del m[k]
            return m

        return _2

    return _1

