import threading
import tkinter
import random
import time


class SpeedTyping():

    def __init__(self):
        # create the gui
        self.window = tkinter.Tk()
        self.window.title('Test your speed in typing!')
        self.window.geometry('700x700')
        self.window.configure(bg="pink")

        self.frame = tkinter.Frame(self.window)

        # open the sample texts
        self.text = open('text.txt', 'r').read().split("\n")

        # create a label
        self.label = tkinter.Label(self.frame, text=random.choice(self.text))
        self.label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # create a entry widget for the user
        self.input_entry = tkinter.Entry(self.frame, width=50, font=('Helvetica', 20))
        self.input_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.input_entry.bind("<KeyRelease>", self.start)

        # create a label for speed
        self.speed_label = tkinter.Label(self.frame, text="Typing Speed: 0.00 words per minute", font=('Helvetica', 18))
        self.speed_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # create a button to reset
        self.reset_button = tkinter.Button(self.frame, width=10, text="Clear", fg="green",
                                           command=self.clear)
        self.reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.window.mainloop()

    # start function and evaluating if it is ok or wrong
    def start(self, event):
        # start if not running
        if not self.running:
            if not event.keycode in [13, 16, 17]:  # keycode for  enter shift ctrl,
                self.running = True
                t = threading.Thread(target=self.time_threading)
                t.start()
                # typing wrong turns the test red
        if not self.label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            # all good , text is black
            self.input_entry.config(fg='black')
        if self.input_entry.get() == self.label.cget('text'):
            self.running = False
            self.input_entry.config(fg='green')

    # start timer
    def time_threading(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            # calculate words per minute and omit the space
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Typing Speed: {wpm:.2f} words per minute")

    # reset the interface
    def clear(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Typing Speed: 0.00 words per minute")
        self.label.config(text=random.choice(self.text))
        self.input_entry.delete(0, tkinter.END)


SpeedTyping()
