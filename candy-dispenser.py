import tkinter as tk
from tkinter import messagebox
import random
import math


class SpringCandyDispenser:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Spring Candy Dispenser")
        self.root.geometry("500x800")

        # Initialize the candy stack with some items
        self.candy_colors = [
            "#FF6B6B",  # Red
            "#4ECDC4",  # Teal
            "#45B7D1",  # Blue
            "#FDCB6E",  # Golden
            "#6C5CE7",  # Purple
            "#A8E6CF",  # Mint Green
            "#FF8ED4",  # Pink
            "#FAD390"  # Light Orange
        ]
        self.candy_stack = self.candy_colors.copy()

        # Spring mechanism variables
        # Initial tension set to 56% (7 candies)
        self.spring_tension = tk.DoubleVar(value=56.0)
        self.max_spring_tension = 100.0
        self.max_candies = 12  # Updated max size

        # Create main frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Create canvas for visual representation
        self.canvas = tk.Canvas(self.frame, width=400, height=600, bg='white')
        self.canvas.pack(pady=10)

        # Spring base parameters
        self.spring_x = 200
        self.spring_y = 500  # Adjusted Y position
        self.spring_width = 100
        self.spring_height = 200
        self.spring_coils = 10

        # Spring tension label
        self.spring_label = tk.Label(self.frame, text="Spring Tension: 56.0%")
        self.spring_label.pack(pady=5)

        # Additional method result label
        self.method_label = tk.Label(self.frame, text="")
        self.method_label.pack(pady=5)

        # Draw initial spring
        self.draw_spring()

        # Draw initial candies
        self.draw_candies()

        # Buttons frame
        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=10)

        # Push button
        push_button = tk.Button(button_frame, text="Push Candy", command=self.push_candy)
        push_button.pack(side=tk.LEFT, padx=5)

        # Pop button
        pop_button = tk.Button(button_frame, text="Pop Candy", command=self.pop_candy)
        pop_button.pack(side=tk.LEFT, padx=5)

        # Peek button
        peek_button = tk.Button(button_frame, text="Peek", command=self.show_peek)
        peek_button.pack(side=tk.LEFT, padx=5)

        # Is Empty button
        is_empty_button = tk.Button(button_frame, text="Is Empty", command=self.show_is_empty)
        is_empty_button.pack(side=tk.LEFT, padx=5)

        # Length button
        length_button = tk.Button(button_frame, text="Length", command=self.show_length)
        length_button.pack(side=tk.LEFT, padx=5)

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

        # Spring coils (draw from the top of the grey rectangle, not below it)
        for i in range(self.spring_coils):
            # Calculate coil points
            y_offset = i * (compressed_height / self.spring_coils)
            points = [
                self.spring_x, self.spring_y - y_offset,  # Adjusted y_offset direction
                               self.spring_x + self.spring_width / 2,
                               self.spring_y - y_offset - compressed_height / (2 * self.spring_coils),
                               self.spring_x - self.spring_width / 2,
                               self.spring_y - y_offset - compressed_height / (self.spring_coils),
                self.spring_x, self.spring_y - y_offset - compressed_height / (self.spring_coils)
            ]

            # Draw coil segments
            self.canvas.create_line(points, fill="steel blue", width=3, tags="spring")

        # Update spring tension label
        self.spring_label.config(text=f"Spring Tension: {tension:.1f}%")

    def draw_candies(self):
        """Draw candies on top of the spring"""
        # Clear previous candies
        self.canvas.delete("candy")

        # Calculate spring compression
        tension = self.spring_tension.get()
        compressed_height = self.spring_height * (1 - tension / 100)

        # Draw candies
        for i, color in enumerate(self.candy_stack):
            # Candy parameters
            candy_size = 40
            candy_x = self.spring_x

            # Adjust candy_y to sit directly on top of the spring (top of the grey rectangle)
            candy_y = self.spring_y - compressed_height - (i * candy_size) - candy_size / 2

            # Draw candy as a circle
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
        """Add a new candy to the stack"""
        if len(self.candy_stack) < self.max_candies:
            # Add a new candy color
            new_color = random.choice(self.candy_colors)
            self.candy_stack.append(new_color)

            # Increase spring tension by 8%
            current_tension = self.spring_tension.get()
            new_tension = min(current_tension + 8, 100)
            self.spring_tension.set(new_tension)

            # Redraw spring and candies
            self.draw_spring()
            self.draw_candies()
        else:
            messagebox.showwarning("Full", "Candy dispenser is full!")

    def pop_candy(self):
        """Remove a candy from the stack"""
        if self.candy_stack:
            # Remove top candy
            self.candy_stack.pop()

            # Reduce spring tension by 8%
            current_tension = self.spring_tension.get()
            new_tension = max(current_tension - 8, 0)
            self.spring_tension.set(new_tension)

            # Redraw spring and candies
            self.draw_spring()
            self.draw_candies()
        else:
            messagebox.showwarning("Empty", "No candies left!")

    def show_length(self):
        """Display the current number of candies in the stack"""
        length = len(self.candy_stack)
        self.method_label.config(text=f"Stack Length: {length}")

    def show_is_empty(self):
        """Check if the candy stack is empty"""
        is_empty = len(self.candy_stack) == 0
        self.method_label.config(text=f"Is Empty: {is_empty}")

    def show_peek(self):
        """Show the color and details of the top candy without removing it"""
        if self.candy_stack:
            # Remove any previous highlight
            self.canvas.delete("peek_highlight")

            top_candy = self.candy_stack[-1]
            color_name = self.get_color_name(top_candy)

            # Calculate spring compression
            tension = self.spring_tension.get()
            compressed_height = self.spring_height * (1 - tension / 100)

            # Candy parameters
            candy_size = 40
            candy_x = self.spring_x

            # Adjust candy_y similarly to draw_candies method
            candy_y = self.spring_y - compressed_height - ((len(self.candy_stack) - 1) * candy_size) - candy_size / 2

            # Add a highlight around the top candy
            self.canvas.create_oval(
                candy_x - candy_size / 2 - 5,
                candy_y - candy_size / 2 - 5,
                candy_x + candy_size / 2 + 5,
                candy_y + candy_size / 2 + 5,
                outline="gold",
                width=3,
                tags="peek_highlight"
            )

            # Update method label
            self.method_label.config(text=f"Top Candy - Color: {color_name}")
        else:
            self.method_label.config(text="No candies in stack")

    def get_color_name(self, color_code):
        """Convert color code to a descriptive name"""
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


if __name__ == "__main__":
    root = tk.Tk()
    app = SpringCandyDispenser(root)
    root.mainloop()
