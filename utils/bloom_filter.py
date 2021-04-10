import pybloom_live

# 布隆过滤器的简单使用
f = pybloom_live.BloomFilter(capacity=1000, error_rate=0.001)
[f.add(x) for x in range(10)]

# 可以自动扩容的布隆过滤器
sbf = pybloom_live.ScalableBloomFilter(mode=pybloom_live.ScalableBloomFilter.SMALL_SET_GROWTH)
[sbf.add(x) for x in range(10)]
print(1 in sbf)
print(11 in sbf)
