from analyze import q1a
from analyze import q1b
from analyze import q2a
from analyze import q2b
import os


if __name__ == "__main__":
    if not os.path.exists("figs/"):
        os.mkdir('figs/')
    q1a.graph()
    q1b.graph()
    q2a.graph()
    q2b.graph()
