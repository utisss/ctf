def check_hash(tree, hash):
    root_hash = tree[0]
    if isinstance(tree[1], tuple):
        left_hash = check_hash(tree[1], hash)
        right_hash = tree[2]
    elif isinstance(tree[2], tuple):
        left_hash = tree[1]
        right_hash = check_hash(tree[2], hash)
    elif tree[1] == "_":
        left_hash = hash
        right_hash = tree[2]
    else:
        left_hash = tree[1]
        right_hash = hash
    
    # concat hashes and compute parent hash
    concat_hashes = left_hash + right_hash
    parent_hash = hashlib.sha256(concat_hashes.encode("utf-8")).hexdigest()
    # comparing to root node?
    if root_hash != "_":
        return root_hash == parent_hash
    else:
        return parent_hash

in_folder = "monopoly_flags"
out_folder = "monopoly_flags_meta/"

# iterate over all flag files
for filename in os.listdir(in_folder):
    file = os.path.join(in_folder, filename)
    meta_file = os.path.join(out_folder, filename + ".meta")
    file_hasher = hashlib.sha256()
    # hash the file
    with open (file, 'rb') as f:
        file_bytes = f.read(1024)
        file_hasher.update(file_bytes)
        hash = file_hasher.hexdigest()
    # parse the nested tuple tree
    with open (meta_file, 'rb') as f:
        meta_bytes = f.read(2048)
        tree = eval(meta_bytes)
    # verify the hash
    if not check_hash(tree, hash):
        print(filename)
        print(file_bytes)
