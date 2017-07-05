from shutil import copyfile
from distutils.dir_util import copy_tree
import DBmodel


class Controller:
    def __init__(self, x, f, ob):
        self.ledit = x
        self.ledit2 = f
        DBmodel.make_db()
        self.last = DBmodel.get_last_element()
        self.pop = ob
        if self.last:
            self.ledit.setText(self.last[0][0])
            self.ledit2.setText(self.last[0][1])

    def copy_it(self, fromm, too):
        try:
            x = fromm
            y = too
            if x and y:
                copy_tree(x, y)
                self.messanger("Επιτυχής Μεταφορά")
                if not self.last:
                    DBmodel.insert(x, too)
                elif x != self.last[0][0] or too != self.last[0][1]:
                    DBmodel.insert(x, too)
                else:
                    self.messanger("Παρακαλώ ελέγξτε τα πεδία")
        except Exception as e:
            self.messanger(str(e))

    def messanger(self, x):
        self.pop.textBrowser.setText(x)
        self.pop.show()
