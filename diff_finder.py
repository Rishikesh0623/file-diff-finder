def compare_files(file1, file2):
    """
    Compare two config-like files.
    Ignores order and duplicate lines.
    Ignores empty lines.
    """

    lines1 = {line.decode("utf-8").strip() for line in file1 if line.decode("utf-8").strip()}

    lines2 = {line.decode("utf-8").strip() for line in file2 if line.decode("utf-8").strip()}

    added = sorted(lines2 - lines1)
    removed = sorted(lines1 - lines2)

    return {"added": added, "removed": removed}
