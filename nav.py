import os

class Nav:

    @classmethod
    def get_nav(cls):
        path = 'templates/'
        obj = os.scandir(path)
        list_files = []
        for fl in obj:
            fl = fl.name
            if not fl.startswith("b"):
                i = fl.find('.')
                fl = fl[:i]
                list_files.append(fl)
        return sorted(list_files)

