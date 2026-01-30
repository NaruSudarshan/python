
# How Python iteration works (a short story)

Imagine a list like `[1, 2, 3, 4]` is a bookshelf. It is **iterable** (lists, file) — you can ask it for a special helper that knows how to walk across its items.

That helper is the **iterator** (for, comprehension). Python creates it with `iter()`.

Once the iterator exists, Python keeps asking it for the next item using `next()` (which calls the iterator’s internal `__next__()` method). Each call hands back the next value: first `1`, then `2`, then `3`, then `4`.

When the iterator has nothing left, it raises `StopIteration`. That is the signal to stop the loop.

So when you write a `for` loop or a comprehension, Python is quietly doing this dance:

1. Call `iter()` on the iterable to get an iterator.
2. Repeatedly call `next()` on that iterator.
3. Stop when `StopIteration` is raised.

That is the whole story: **iterables** give you **iterators**, and **iterators** produce values one by one through `__next__()` until they are done.





