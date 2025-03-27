from tkinter import *
import random

class canvas_manipulation:
    def __init__(self):
        self.list_of_label = []
        self.present_info_label = ''
        self.master = Tk()
        self.create_title()
        self.create_entry()
        self.create_button()
        mainloop()


    def create_title(self):
        self.master.title('Help you make a choice')

    def create_entry(self):
        all_label = []
        for i in range(10):
            Label(self.master, text= f'{i+1}').grid(row=i, column=0)
            ele = Entry(self.master)
            all_label.append(ele)
            ele.grid(row=i, column=1)
        self.list_of_label = all_label

    def get_valid_input(self):

        valid_value = []
        for ele in self.list_of_label:
            value = ele.get()
            if value:
                valid_value.append(value)
        random.shuffle(valid_value)
        return self.present_information(valid_value)

    def present_information(self, values):
        result = "\n".join(values)
        self.present_info_label.config(text = result)


    def create_button(self):
        button = Button(self.master, text = 'Begin', width = 25, command = self.get_valid_input)
        button.grid()
        self.present_info_label = Label(self.master, text = '')
        self.present_info_label.grid()




if __name__ == '__main__':
    canvas_manipulation()
