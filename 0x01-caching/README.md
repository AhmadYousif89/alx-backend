# Caching Algorithms

## What is a caching system

A caching system is a temporary storage system that allows you to store the most frequently accessed data in a cache.
By storing this data in a cache, we can access it more quickly than if we were to access it from the original storage location.
This can help to improve the performance of our application.

### Belady's Anomaly in Page Replacement Algorithms

-

## Caching algorithms and data structures

There are many different caching algorithms and data structures that can be used to implement a caching system.

Some of the most common caching algorithms include:

- **Random Replacement**: This's the most basic caching algorithm that removes items from the cache at random when the cache is full or when an item needs to be added to the cache without specifiying a max limit.

- **FIFO (First In, First Out)**: This algorithm removes the items from the cache in the order that they were added.

- **LIFO (Last In, First Out)**: This algorithm removes the items from the cache in the reverse order that they were added.

- **LRU (Least Recently Used)**: This algorithm removes the least recently used items from the cache when the cache is full.

- **MRU (Most Recently Used)**: This algorithm removes the most recently used items from the cache when the cache is full.

- **LFU (Least Frequently Used)**: This algorithm removes the least frequently used items from the cache when the cache is full.

Some of the most common data structures used to implement a caching system include:

- **Array**: An array can be used to implement a cache with a fixed size. When a new item is added to the cache, the least recently used item can be removed from the cache.

- **Linked List**: A linked list can be used to implement a cache with a fixed size. When a new item is added to the cache, the least recently used item can be removed from the cache.

- **Hash Table**: A hash table can be used to implement a cache with a fixed size. When a new item is added to the cache, the least recently used item can be removed from the cache.

## What limits a caching system have

A caching system has a few limitations that you should be aware of:

- **Cache Size**: The size of the cache is limited, so you can only store a certain amount of data in the cache at any given time.

- **Cache Hit Rate**: The cache hit rate is the percentage of requests that are served by the cache. A high cache hit rate is desirable, as it means that the cache is serving a large percentage of requests.

- **Cache Miss Rate**: The cache miss rate is the percentage of requests that are not served by the cache. A high cache miss rate is undesirable, as it means that the cache is not serving a large percentage of requests.

- **Cache Eviction Policy**: The cache eviction policy determines which items are removed from the cache when the cache is full. Different caching algorithms use different eviction policies to determine which items are removed from the cache.

## Conclusion

Caching algorithms and data structures are an important part of building a caching system. By understanding the different caching algorithms and data structures that are available, you can choose the best caching system for your application.
