class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        print('inside enter')
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        print('inside exit')
        self.file.close()

with CustomOpen('data.txt') as f:
    contents = f.read()
#same as     
#with open('data.txt') as f:
#    contents = f.read()

print(contents)