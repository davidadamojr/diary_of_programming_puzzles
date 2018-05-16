##This Program Converts a given decimal to the given base.

def cBase(n, base):
    stri = ""
    if n == 0:
        return
    print(n)
    r = n % base
    cBase(n / base, base)
    if r < 10:
        stri += str(r)
    else:
        stri += chr(r - 10 + ord('A'))
    return stri


n, base = list(map(int, input("Enter Decimal Followed By The Base You Want it To Be Converted :\n").split()))
print(cBase(n, base))
