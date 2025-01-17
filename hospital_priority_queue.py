import tkinter as tk
from tkinter import messagebox, simpledialog
import heapq


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Use negative age for max-heap behavior (oldest first)
        self.priority = -age
        # Unique identifier to handle ties and updates
        self.id = id(self)

    def __lt__(self, other):
        # If ages are the same, use id to ensure stable sorting
        if self.priority == other.priority:
            return self.id < other.id
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.name} (Age: {self.age})"


class HospitalPriorityQueue:
    def __init__(self):
        self.queue = []
        self.patient_dict = {}

    def add(self, patient):
        """Add a patient to the queue"""
        heapq.heappush(self.queue, patient)
        self.patient_dict[patient.name] = patient
        return f"{patient.name} added to queue"

    def remove_min(self):
        """Remove and return the highest priority patient"""
        if not self.queue:
            return "Queue is empty"
        patient = heapq.heappop(self.queue)
        del self.patient_dict[patient.name]
        return f"Serving {patient.name}"

    def update_age(self, name, new_age):
        """Update a patient's age and reposition in queue"""
        if name not in self.patient_dict:
            return f"{name} not found in queue"

        # Remove existing patient
        patient = self.patient_dict[name]
        self.queue.remove(patient)
        heapq.heapify(self.queue)

        # Create new patient with updated age
        new_patient = Patient(name, new_age)
        self.add(new_patient)
        return f"Patient {name}'s age has been updated to {new_age}"

    def peek(self):
        """Return the highest priority patient without removing"""
        if not self.queue:
            return "Queue is empty"
        return f"Next to be served: {self.queue[0].name}"

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.queue) == 0

    def size(self):
        """Return number of patients in queue"""
        return len(self.queue)

    def display_queue(self):
        """Return a string representation of the entire queue"""
        if not self.queue:
            return "Queue is empty"
        # Sort to show in priority order
        sorted_queue = sorted(self.queue, key=lambda x: x.priority)
        return "\n".join([str(patient) for patient in sorted_queue])

    def last_in_queue(self):
        """Return the last patient in the queue"""
        if not self.queue:
            return "Queue is empty"
        # Find the patient with the highest (least negative) priority
        last_patient = max(self.queue, key=lambda x: x.priority)
        return f"Last in queue: {last_patient.name}"


class HospitalQueueApp:
    def __init__(self, master):
        self.master = master
        master.title("Tradix's Hospital Priority Queue")
        master.geometry("600x700")

        # Create priority queue
        self.pq = HospitalPriorityQueue()

        # Create and setup buttons and display
        self.create_widgets()

    def create_widgets(self):
        # Queue Display
        self.queue_display = tk.Text(self.master, height=15, width=50)
        self.queue_display.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        # Button configurations
        buttons = [
            ("Add Patient", self.add_patient),
            ("Remove Patient", self.remove_next_patient),
            ("Update Patient Age", self.update_patient_age),
            ("Peek Next Patient", self.peek_next_patient),
            ("Check if Empty", self.check_empty),
            ("Queue Size", self.show_queue_size),
            ("Display Full Queue", self.show_full_queue),
            ("Show Last in Queue", self.show_last_in_queue)
        ]

        # Create buttons
        for i, (text, command) in enumerate(buttons):
            row = i // 4
            col = i % 4
            btn = tk.Button(button_frame, text=text, command=command, width=15)
            btn.grid(row=row, column=col, padx=5, pady=5)

    def update_display(self):
        """Update the queue display"""
        self.queue_display.delete(1.0, tk.END)
        queue_contents = self.pq.display_queue()
        self.queue_display.insert(tk.END, queue_contents)

    def add_patient(self):
        name = simpledialog.askstring("Input", "Enter patient name:")
        if name:
            age = simpledialog.askinteger("Input", "Enter patient age:")
            if age:
                result = self.pq.add(Patient(name, age))
                messagebox.showinfo("Result", result)
                self.update_display()

    def remove_next_patient(self):
        result = self.pq.remove_min()
        messagebox.showinfo("Result", result)
        self.update_display()

    def update_patient_age(self):
        name = simpledialog.askstring("Input", "Enter patient name:")
        if name:
            new_age = simpledialog.askinteger("Input", "Enter new age:")
            if new_age:
                result = self.pq.update_age(name, new_age)
                messagebox.showinfo("Result", result)
                self.update_display()

    def peek_next_patient(self):
        result = self.pq.peek()
        messagebox.showinfo("Result", result)

    def check_empty(self):
        result = "Queue is empty" if self.pq.is_empty() else "Queue is not empty"
        messagebox.showinfo("Result", result)

    def show_queue_size(self):
        result = f"Queue size: {self.pq.size()}"
        messagebox.showinfo("Result", result)

    def show_full_queue(self):
        result = self.pq.display_queue()
        messagebox.showinfo("Full Queue", result)

    def show_last_in_queue(self):
        result = self.pq.last_in_queue()
        messagebox.showinfo("Result", result)


def main():
    root = tk.Tk()
    app = HospitalQueueApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
