print(bool("bibhu"))
print(bool(4))
print(bool([]))
print(bool({}))
print(bool("b"))
class myclass():
    def _len_(self):
        return 0
myobj=myclass()
print(bool(myobj))