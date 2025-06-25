inp = str(input())

print("YES" if any(c in ("H", "Q", "9") for c in inp) else "NO")