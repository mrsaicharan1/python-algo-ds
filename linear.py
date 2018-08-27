def search(a,X):
    found = False
    for i in a:
        if i == X:
            found=True
            print(a.index(X))

def main():
    fruits = ['apples','oranges','pineapples']
    X = 'apples'
    search(fruits,'apples')

if __name__ =='__main__':
    main()
