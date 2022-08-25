#We will use tkinter later, right now it's important to make sure we can import it
import tkinter

# This if statment just says "if this python script is the 'main' one, do this"
if __name__ == "__main__":
    print("hello world, it's time to click")
    
    tkroot = tkinter.Tk()
    tkroot.title("currently unnamed clicker game")
    
    tkroot.geometry('800x600+150+100')
    
    tkroot.mainloop()
