def normalize(file_obj):
    file_obj.seek(0)
    lines = set()

    for line in file_obj:
        decoded = line.decode("utf-8").strip()
        if decoded:
            lines.add(decoded)

    return lines


def semantic_compare(file1, file2):
    lines1 = normalize(file1)
    lines2 = normalize(file2)

    added = sorted(lines2 - lines1)
    removed = sorted(lines1 - lines2)

    diff = []

    for line in removed:
        diff.append({"type": "removed", "content": line})

    for line in added:
        diff.append({"type": "added", "content": line})

    return {"diff": diff}