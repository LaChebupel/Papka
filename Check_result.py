def test_substring(full_string, substring):
    if substring in full_string:
        print("")
    else:
        print(f"expected {substring} to be substring of {full_string}")