from tkinter import Tk
from Views.HomeView import HomeView

def main(args):
    root = Tk()
    app = HomeView(root)
    root.mainloop()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
