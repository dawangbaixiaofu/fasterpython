from multiprocessing import Pool
from hashlib import sha512


def load_words(path):
    with open(path, mode='r') as f:
        words = f.readlines()
    return words



def hash_word(word):
    hash_obj = sha512()
    byte_data = word.encode('utf-8')
    hash_obj.update(byte_data)
    return hash_obj.hexdigest()


def main1():
    path = r'.\processpool\1m_words.txt'
    words = load_words(path)
    print(f"load {len(words)} words from {path}")
    known_words = {hash_word(word) for word in words}
    print(f"done, with {len(known_words)} hashed.")

# process pool
def main():
    path = r'.\processpool\1m_words.txt'
    words = load_words(path)
    print(f"load {len(words)} words from {path}")
    with Pool(10) as pool:
        known_words = set(pool.map(func=hash_word, iterable=words))
    print(f"done, with {len(known_words)} hashed.")

if __name__ == "__main__":
    main()