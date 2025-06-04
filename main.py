
import tkinter as tk
import random

WIDTH = 800
HEIGHT = 600

BUILDING_COUNT = 10
BUILDING_WIDTH = 60
BUILDING_MIN_HEIGHT = 150
BUILDING_MAX_HEIGHT = 400

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Zwei Gorillas auf Hochhäusern")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="skyblue")
        self.canvas.pack()

        self.buildings = self.generate_buildings()
        self.draw_buildings()

        # Bild rainer.png laden
        self.gorilla_img = tk.PhotoImage(file="rainer.png")

        self.place_gorillas()

    def generate_buildings(self):
        buildings = []
        gap = WIDTH // BUILDING_COUNT
        for i in range(BUILDING_COUNT):
            x = i * gap + (gap - BUILDING_WIDTH) // 2
            height = random.randint(BUILDING_MIN_HEIGHT, BUILDING_MAX_HEIGHT)
            y = HEIGHT - height
            buildings.append((x, y, BUILDING_WIDTH, height))
        return buildings

    def draw_buildings(self):
        for b in self.buildings:
            x, y, w, h = b
            self.canvas.create_rectangle(x, y, x + w, HEIGHT, fill="dimgray", outline="black")

    def place_gorillas(self):
        left_buildings = [b for b in self.buildings if b[0] + b[2]//2 < WIDTH//2]
        right_buildings = [b for b in self.buildings if b[0] + b[2]//2 >= WIDTH//2]

        left_b = random.choice(left_buildings)
        right_b = random.choice(right_buildings)

        # Positionen der Gorillas
        x_left = left_b[0] + left_b[2] // 2
        y_left = left_b[1]

        x_right = right_b[0] + right_b[2] // 2
        y_right = right_b[1]

        # Gorilla links
        self.canvas.create_image(x_left, y_left, image=self.gorilla_img, anchor="s")
        # Gorilla rechts
        self.canvas.create_image(x_right, y_right, image=self.gorilla_img, anchor="s")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

