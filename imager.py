import tkinter

sensitivityRatio = 1.0


def display(data=[[6,9],[5,9]], title="STM Imaging Result", width=400, height=400, ratioDifference=1):
    def updateCanvas():
        global sensitivityRatio
        rows = len(data)
        cols = len(data[0])
        
        square_size = min(width/cols, height/rows)
        draw_width = square_size * cols
        draw_height = square_size * rows
        
        offset_x = (width - draw_width)/2
        offset_y = (height - draw_height)/2

        largest = float(0)
        for row in range(rows):
            for col in range(cols):
                if data[row][col] > largest: largest = data[row][col]
        extra = (largest * sensitivityRatio)
        if (extra>0):
            colourRatio = 255 / extra
        else:
            print("Error")
            sensitivityRatio+=ratioDifference
            colourRatio = 255

        canvas.delete("all")

        for row in range(rows):
            for col in range(cols):
                x1 = offset_x + col * square_size
                y1 = offset_y + row * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                value = int(data[row][col] * colourRatio)
                if value < 0: value = 0
                if value > 255: value = 255
                color = f'#FF{255-value:02x}{255-value:02x}'
                canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    root = tkinter.Tk()
    root.title(title)
    
    canvas = tkinter.Canvas(root, width=width, height=height, bg="black")
    canvas.pack(fill=tkinter.BOTH, expand=True)

    updateCanvas()

    def resizeEvent(event):
        nonlocal width, height
        if event.width != width or event.height != height:
            width, height = event.width, event.height
            updateCanvas()

    def keypressEvent(event):
        global sensitivityRatio
        if event.keysym == 'Up':
            sensitivityRatio += ratioDifference
            updateCanvas()
        elif event.keysym == 'Down':
            sensitivityRatio -= ratioDifference
            updateCanvas()

    root.bind("<Configure>", resizeEvent)
    root.bind("<KeyPress>", keypressEvent)
    
    root.mainloop()