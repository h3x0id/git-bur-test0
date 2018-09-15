def call(varT):
    while varT<3:
        print(varT)
        varT=varT+1
        call(varT)

call(0)