import sys                  # 심화2 - 영어단어 정렬
from collections import Counter
input = sys.stdin.readline


n, m = map(int, input().split())
words = []

for i in range(n):
    word = input().strip()
    if len(word) >= m:
        words.append(word)

cnt = Counter(words)   #most_common() x

sorted_words = sorted(                       # 여기가 핵심코드
    cnt.items(),                            # 여기가 핵심코드
    key=lambda x: (-x[1], -len(x[0]), x[0])  # 여기가 핵심코드
)
for word, _ in sorted_words:
    print(word)