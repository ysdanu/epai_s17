
from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    merged = defaultdict(int)
    for d in dicts:
        for word, freq in d.items():
            merged[word] += freq
    # Optional: sort by frequency in descending order
    return dict(sorted(merged.items(), key=lambda item: item[1], reverse=True))

def merge_with_counter(*dicts):
    merged = Counter()
    for d in dicts:
        merged.update(d)
    # Optional: sort by frequency in descending order
    return dict(sorted(merged.items(), key=lambda item: item[1], reverse=True))
