# util/disk.py

def getCache(cache_name):
    # 实现你的缓存功能，这只是一个示例
    from diskcache import Cache
    return Cache(f'./{cache_name}_cache')
