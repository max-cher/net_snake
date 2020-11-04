import tkinter as tk







def main():
    global root, canvas, gun, target, screen1, gravity, air, WIDTH, HEIGHT, SIZE
    WIDTH = 800
    HEIGHT = 800
    SIZE = 20
    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    canvas = tk.Canvas(root, bg='lightgreen')
    canvas.pack(fill=tk.BOTH, expand=1)
    
    for i in range(0, WIDTH, SIZE):
        canvas.create_line(0, i, HEIGHT, i)
    for i in range(0, HEIGHT, SIZE):
        canvas.create_line(i, 0, i, WIDTH)
    
def snake():
	global root, canvas, gun, target, screen1, gravity, air, WIDTH, HEIGHT, SIZE
	canvas.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#fb0")
    
    
    #target = Target()
    #screen1 = canvas.create_text(400, 300, text='', font='28')
    #gun = Gun()
    #bullet = 0
    #balls = []
    #gravity = 0.5
    #air = 0.005)




main()
snake()


root.mainloop()
