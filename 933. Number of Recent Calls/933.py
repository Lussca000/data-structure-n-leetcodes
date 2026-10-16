from collections import deque

class RecentCounter:
    def __init__(self):
        self.chamadas = deque()

    def ping(self, t: int) -> int:
        self.chamadas.append(t)
        while self.chamadas and self.chamadas[0] < t - 3000:
            self.chamadas.popleft()
        return len(self.chamadas)

# n irei considerar pq nao entendi bem o como isso funciona