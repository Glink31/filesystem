from File import File
from folder import Folder
from filesystem import Filesystem
from memento import Memento
from mementoreal import MementoReal
from caretaker import Caretaker

C = Filesystem()
a = File('Tardis.png')
b = Folder('Doctors')
d = File('Tennant.png')
e = File('Capaldi.png')
f = Folder('Stuff')
g = File('Box.png')
h = File('Story.txt')

C.additem(a)
b.additem(d)
b.additem(e)
C.additem(b)
C.root.prnt(0)
l = C.creatememento()
m = Caretaker()
m.savestate(l)
f.additem(g)
C.additem(f)
C.root.prnt(0)
n = C.creatememento()
m.savestate(n)
C.additem(h)
C.root.prnt(0)
o = C.creatememento()
m.savestate(o)
C.restore(m.restorestate(0))
C.root.prnt(0)
C.restore(m.restorestate(2))
C.root.prnt(0)
C.restore(m.restorestate(1))
C.root.prnt(0)
