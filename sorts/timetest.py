import random
from numba import jit

from bubble_sort import bubble_sort
from gnome_sort import gnome_sort
from merge_sort import merge_sort
from merge_sort_fastest import merge_sort as merge_fast

def timed_factory(num_reps=1):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return timed



if __name__ == '__main__':
    sorters = [bubble_sort, gnome_sort, merge_sort, merge_fast]

    lst = [x for x in range(10000)]

    for s in sorters:
        random.shuffle(lst)
        print(f'Sorter:{s.__name__}')
        fact = timed_factory(5)
        srt = fact(s)
        srt(lst)
        random.shuffle(lst)

        jitted = jit(s, nopython=False)
        srt = fact(jitted)
        srt(lst)



