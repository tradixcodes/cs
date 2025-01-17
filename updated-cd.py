import tkinter as tk
from tkinter import messagebox
import random

class SpringCandyDispenser:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Spring Candy Dispenser")
        self.root.geometry("800x900")  # Increased window size

        # Initialize the candy stack with some items
        self.candy_colors = [
            "#FF6B6B",  # Red
            "#4ECDC4",  # Teal
            "#45B7D1",  # Blue
            "#FDCB6E",  # Golden
            "#6C5CE7",  # Purple
            "#A8E6CF",  # Mint Green
            "#FF8ED4",  # Pink
            "#FAD390"   # Light Orange
        ]
        self.candy_stack = self.candy_colors[:4]  # Start with 4 candies

        # Spring mechanism variables
        self.spring_tension = tk.DoubleVar(value=32.0)  # Initial tension for 4 candies
        self.max_spring_tension = 100.0
        self.max_candies = 12

        # Create main container
        self.main_container = tk.Frame(root, bg='#f0f0f0')
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title
        title_label = tk.Label(self.main_container,
                             text="Spring Candy Dispenser",
                             font=('Helvetica', 16, 'bold'),
                             bg='#f0f0f0')
        title_label.pack(pady=10)

        # Create canvas for visual representation
        self.canvas = tk.Canvas(self.main_container,
                              width=400,
                              height=600,
                              bg='white',
                              relief='ridge',
                              bd=2)
        self.canvas.pack(pady=10)

        # Spring base parameters
        self.spring_x = 200
        self.spring_y = 500
        self.spring_width = 100
        self.spring_height = 200
        self.spring_coils = 10

        # Spring tension label
        self.spring_label = tk.Label(self.main_container,
                                   text="Spring Tension: 32.0%",
                                   font=('Helvetica', 12),
                                   bg='#f0f0f0')
        self.spring_label.pack(pady=5)

        # Method result label
        self.method_label = tk.Label(self.main_container,
                                   text="",
                                   font=('Helvetica', 12),
                                   bg='#f0f0f0')
        self.method_label.pack(pady=5)

        # Buttons frame
        self.button_frame = tk.Frame(self.main_container, bg='#f0f0f0')
        self.button_frame.pack(pady=20)

        # Create buttons with improved styling
        button_style = {
            'font': ('Helvetica', 11),
            'width': 12,
            'height': 2,
            'relief': 'raised',
            'bd': 3
        }

        # Row 1 buttons
        tk.Button(self.button_frame,
                 text="Push Candy",
                 command=self.push_candy,
                 bg='#90EE90',
                 **button_style).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(self.button_frame,
                 text="Pop Candy",
                 command=self.pop_candy,
                 bg='#FFB6C1',
                 **button_style).grid(row=0, column=1, padx=5, pady=5)

        # Row 2 buttons
        tk.Button(self.button_frame,
                 text="Peek",
                 command=self.show_peek,
                 bg='#87CEEB',
                 **button_style).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(self.button_frame,
                 text="Is Empty",
                 command=self.show_is_empty,
                 bg='#DDA0DD',
                 **button_style).grid(row=1, column=1, padx=5, pady=5)

        # Row 3 button
        tk.Button(self.button_frame,
                 text="Length",
                 command=self.show_length,
                 bg='#F0E68C',
                 **button_style).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Draw initial spring and candies
        self.draw_spring()
        self.draw_candies()

    # [Rest of the methods remain the same as in your original code]
    def draw_spring(self):
        """Draw the spring with current tension"""
        # Clear previous spring
        self.canvas.delete("spring")

        # Calculate current spring compression
        tension = self.spring_tension.get()
        compressed_height = self.spring_height * (1 - tension / 100)

        # Spring base (grey rectangle)
        self.canvas.create_rectangle(
            self.spring_x - self.spring_width / 2,
            self.spring_y,
            self.spring_x + self.spring_width / 2,
            self.spring_y + 20,
            fill="gray",
            tags="spring"
        )

        # Spring coils
        for i in range(self.spring_coils):
            y_offset = i * (compressed_height / self.spring_coils)
            points = [
                self.spring_x, self.spring_y - y_offset,
                self.spring_x + self.spring_width / 2,
                self.spring_y - y_offset - compressed_height / (2 * self.spring_coils),
                self.spring_x - self.spring_width / 2,
                self.spring_y - y_offset - compressed_height / (self.spring_coils),
                self.spring_x, self.spring_y - y_offset - compressed_height / (self.spring_coils)
            ]
            self.canvas.create_line(points, fill="steel blue", width=3, tags="spring")

        # Update spring tension label
        self.spring_label.config(text=f"Spring Tension: {tension:.1f}%")

    def draw_candies(self):
        """Draw candies on top of the spring"""
        self.canvas.delete("candy")
        tension = self.spring_tension.get()
        compressed_height = self.spring_height * (1 - tension / 100)

        for i, color in enumerate(self.candy_stack):
            candy_size = 40
            candy_x = self.spring_x
            candy_y = self.spring_y - compressed_height - (i * candy_size) - candy_size / 2

            self.canvas.create_oval(
                candy_x - candy_size / 2,
                candy_y - candy_size / 2,
                candy_x + candy_size / 2,
                candy_y + candy_size / 2,
                fill=color,
                outline="black",
                tags="candy"
            )

    def push_candy(self):
        if len(self.candy_stack) < self.max_candies:
            new_color = random.choice(self.candy_colors)
            self.candy_stack.append(new_color)
            current_tension = self.spring_tension.get()
            new_tension = min(current_tension + 8, 100)
            self.spring_tension.set(new_tension)
            self.draw_spring()
            self.draw_candies()
        else:
            messagebox.showwarning("Full", "Candy dispenser is full!")

    def pop_candy(self):
        if self.candy_stack:
            self.candy_stack.pop()
            current_tension = self.spring_tension.get()
            new_tension = max(current_tension - 8, 0)
            self.spring_tension.set(new_tension)
            self.draw_spring()
            self.draw_candies()
        else:
            messagebox.showwarning("Empty", "No candies left!")

    def show_length(self):
        length = len(self.candy_stack)
        self.method_label.config(text=f"Stack Length: {length}")

    def show_is_empty(self):
        is_empty = len(self.candy_stack) == 0
        self.method_label.config(text=f"Is Empty: {is_empty}")

    def show_peek(self):
        if self.candy_stack:
            self.canvas.delete("peek_highlight")
            top_candy = self.candy_stack[-1]
            color_name = self.get_color_name(top_candy)
            tension = self.spring_tension.get()
            compressed_height = self.spring_height * (1 - tension / 100)
            candy_size = 40
            candy_x = self.spring_x
            candy_y = self.spring_y - compressed_height - ((len(self.candy_stack) - 1) * candy_size) - candy_size / 2

            self.canvas.create_oval(
                candy_x - candy_size / 2 - 5,
                candy_y - candy_size / 2 - 5,
                candy_x + candy_size / 2 + 5,
                candy_y + candy_size / 2 + 5,
                outline="gold",
                width=3,
                tags="peek_highlight"
            )
            self.method_label.config(text=f"Top Candy - Color: {color_name}")
        else:
            self.method_label.config(text="No candies in stack")

    def get_color_name(self, color_code):
        color_names = {
            "#FF6B6B": "Red",
            "#4ECDC4": "Teal",
            "#45B7D1": "Blue",
            "#FDCB6E": "Golden",
            "#6C5CE7": "Purple",
            "#A8E6CF": "Mint Green",
            "#FF8ED4": "Pink",
            "#FAD390": "Light Orange"
        }
        return color_names.get(color_code, "Unknown")

def main():
    root = tk.Tk()
    app = SpringCandyDispenser(root)
    root.mainloop()

if __name__ == "__main__":
    main()