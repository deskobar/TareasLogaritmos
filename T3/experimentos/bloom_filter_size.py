from src.bloom_filter import BloomFilter
import tracemalloc
import sys
M = 5000
K = 7

tracemalloc.start()
bf = BloomFilter(M, K)
antes = sys.getsizeof(bf)
snapshot_after_create_bf = tracemalloc.take_snapshot()

to_insert = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'.split()*100


snapshot_before_insert = tracemalloc.take_snapshot()

for w in to_insert:
    bf.insert(w)
despues = sys.getsizeof(bf)
snapshot_after_insert = tracemalloc.take_snapshot()
for memo in snapshot_after_create_bf.statistics('filename')[:10]:
    print(memo)
print("entremedio")
for memo in  snapshot_after_insert.statistics('filename')[:10]:
    print(memo)
print("fin")
print(antes, despues)
