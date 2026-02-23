import difflib


def structural_compare(file1, file2):
    file1.seek(0)
    file2.seek(0)

    lines1 = file1.read().decode("utf-8").splitlines()
    lines2 = file2.read().decode("utf-8").splitlines()

    differ = difflib.HtmlDiff(tabsize=4, wrapcolumn=80)

    html_diff = differ.make_table(
        lines1,
        lines2,
        fromdesc="Original",
        todesc="Modified",
        context=False,
        numlines=3
    )

    return {"html": html_diff}