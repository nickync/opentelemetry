import attridict
f = attridict(a = '1', b = 2, c = None)
print(f.c)
f.pdf = attridict(a = '1', b = 2, c = None, url = None)
print(f.pdf.url)