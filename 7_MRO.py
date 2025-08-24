#si hay varias herencias, estable el orden de métodos con el mismo nombre
class A:
    def hablar(self):
        print("A")

class B(A):
    def hablar(self):
        print("B")

class C(A):
    def hablar(self):
        print("C")

class D(B, C):
    def hablar(self):
        print("D")

class F(D):
    def hablar(self):
        print("F")

# orden de resolución de métodos
print(F.mro())  

f = F()
f.hablar()

