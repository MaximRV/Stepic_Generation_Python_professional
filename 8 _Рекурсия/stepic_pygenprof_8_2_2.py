def subsequence():
    def number(n):
        if n <= 100:
            print(n)
            number(n + 1)

    number(1)
