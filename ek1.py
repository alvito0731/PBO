class karyawan():
    def tampil(self):
        print(self.id, self.job)

class manager(karyawan):
    def __init__(self):
        self.id = 1
        self.job = "mengatur"

class programmer(karyawan):
    def __init__(self):
        self.id = 2
        self.job = "membuat program"

a = manager()
a.tampil()
b = programmer()
b.tampil()