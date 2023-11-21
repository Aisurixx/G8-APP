import tkinter as tk
from ttkbootstrap import Style
from feelings_outlet_ui import FeelingsOutletUI

if __name__ == "__main__":
    root = tk.Tk()
    style = Style(theme="minty")
    app = FeelingsOutletUI(root)

    root.mainloop()
