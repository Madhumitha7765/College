def rl_encode(line):
    n = len(line)
    i = 0
    while i < n - 1:

        # Count occurrences of
        # current character
        count = 1
        while (i < n - 1 and
               line[i] == line[i + 1]):
            count += 1
            i += 1
        i += 1

        # Print character and its count
        print( str(count) + line[i - 1], end="")

st = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
rl_encode(st)
