  #We need to import this to use the tkinter code (for a gui)
import tkinter

  # This if statment just says "if this python script is the 'main' one, do this"
if __name__ == "__main__":
    print("hello world, it's time to click")
    
      #I thought about not storing the counter value in an integer, but then I figured that would be too confusing
    counter = 0
    
      #this object, tkroot, is our root tkinter object.  you can kinda think of it as the window itself
    tkroot = tkinter.Tk()
    tkroot.title("currently unnamed clicker game")
    
      #this line sets the size window "spawns" at as well at the location 'width in pixels' x 'height in pixels' + 'pixels down from upper left corner of screen' + 'pixels over from upper left corner of screen'
    tkroot.geometry('800x600+150+100')
    
      #in order to pass text to a tkinter Label object we nee to use a special string variable.  It seems to be a string in a "wrapper class".  Fastinationingly, we cannot declare this variable until after wee have made tkroot, for some reason
    counter_string_var = tkinter.StringVar()
    
      #this is how you change the value of the counter_string_var, but using one of its methods, because counter_string_var is an object
    counter_string_var.set("0")
    
      #this function will run every time the button is clicked
    def button_clicked_function():
          #this line makes it so we can access the variable "counter" because usually you can't because of "scoping".  "Scoping" is actually a feature that helps keep different parts of massive prjects from bumping into eachother
        global counter 
          #make counter go up by one
        counter = counter + 1
          #print a hilarious message
        print("yo mama just got clicked and the counter is at " + str(counter))
          #this one involves two methods, str(counter) turns counter into a string (from numbers to words, so to speak) and then sets counter_string_var to that new string.  the reason for this is that counter_string_var has to be a string, it cannot be an integer/number
        counter_string_var.set(str(counter))
    
      #this line makes the main button, the first arguement is the tkinter object the button is anchored to, the second the display text, and the third the function called when clicked
    main_button = tkinter.Button(tkroot, text = "click me", command = button_clicked_function)
    
      #this function/method actually adds the button to the anchor it is set to, in this case tkroot aka the window
    main_button.pack()
    
      #this line makes the "Label" that will display the count of how many times you have clicked the button, the first arguement is the tkinter object the button is anchored to, the second the display text, which needs to be a string in a special wrapper class in order to be able to be changed once the tkinter mainloop starts
    counter_label = tkinter.Label(tkroot, textvariable = counter_string_var)
    
      #this function/method actually adds the Label to the anchor it is set to, in this case tkroot aka the window
    counter_label.pack()
    
      #this command starts up the whole tkinter engine I guess
    tkroot.mainloop()

