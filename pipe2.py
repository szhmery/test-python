from multiprocessing import Pool, Process, Pipe
from itertools import izip


def spawn(f):
    def func(pipe, item):
        pipe.send(f(item))
        pipe.close()

    return func


def parmap(f, items):
    pipe = [Pipe() for _ in items]
    proc = [Process(target=spawn(f),
                    args=(child, item))
            for item, (parent, child) in izip(items, pipe)]
    [p.start() for p in proc]
    [p.join() for p in proc]
    return [parent.recv() for (parent, child) in pipe]


class CalculateFib(object):
    # ...

    def parmap_run(self):
        print parmap(self.fib, [35] * 2)


cl = CalculateFib()
cl.parmap_run()