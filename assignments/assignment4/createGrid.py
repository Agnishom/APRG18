import random

randomGrid = "\n".join(["".join(['0' if random.random() > 0.5 else '1' for _ in range(1000)]) for _ in range(1000)])

with open("grid.txt", "w") as f:
    f.write(randomGrid)
