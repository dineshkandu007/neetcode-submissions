from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key -> [value, frequency]
        self.cache = {}

        # frequency -> OrderedDict of keys
        self.freq_map = defaultdict(OrderedDict)

        # Smallest frequency currently in cache
        self.min_freq = 0


    def _update_frequency(self, key):
        value, freq = self.cache[key]

        # Remove key from old frequency group
        del self.freq_map[freq][key]

        # If old frequency group becomes empty
        if not self.freq_map[freq]:

            # If this was the minimum frequency,
            # minimum frequency increases
            if self.min_freq == freq:
                self.min_freq += 1

            del self.freq_map[freq]

        # Increase frequency
        new_freq = freq + 1

        # Update cache
        self.cache[key] = [value, new_freq]

        # Add key to new frequency group
        self.freq_map[new_freq][key] = None


    def get(self, key: int) -> int:
        # Key does not exist
        if key not in self.cache:
            return -1

        value, freq = self.cache[key]

        # Increase usage frequency
        self._update_frequency(key)

        return value


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:
            # Update value
            self.cache[key][0] = value

            # put also counts as usage
            self._update_frequency(key)
            return

        # Cache is full
        if len(self.cache) >= self.capacity:

            # Get frequency group with smallest frequency
            keys = self.freq_map[self.min_freq]

            # Remove least recently used key
            lru_key, _ = keys.popitem(last=False)

            del self.cache[lru_key]

            # Clean empty frequency group
            if not keys:
                del self.freq_map[self.min_freq]

        # New key always starts with frequency 1
        self.cache[key] = [value, 1]

        # Add as most recently used in frequency 1
        self.freq_map[1][key] = None

        # New minimum frequency is always 1
        self.min_freq = 1