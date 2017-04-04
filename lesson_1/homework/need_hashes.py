import os
import hashlib


def get_hash(value, alg_name):
    try:
        if alg_name == "md5":
            return hashlib.md5(value).hexdigest()
        elif alg_name == "sha1":
            return hashlib.sha1(value).hexdigest()
        elif alg_name == "sha512":
            return hashlib.sha512(value).hexdigest()
    except:
        return None

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = "need_hashes.csv"
    results = []
    with open(os.path.join(base_dir, file_name)) as f:
        for line in f:
            values = line.strip().split(";")
            value, alg_name = values[0], values[1]
            result = get_hash(value.encode(), alg_name)
            results.append(
                ";".join([value, alg_name, result if result else ""])+"\n")
    with open(os.path.join(base_dir, file_name), "w") as f:
        f.writelines(results)
