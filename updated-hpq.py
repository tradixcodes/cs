import tkinter as tk
from tkinter import messagebox, simpledialog
import heapq
from enum import Enum

class Severity(Enum):
    CRITICAL = 1
    SEVERE = 2
    MODERATE = 3
    MILD = 4
    ROUTINE = 5

class Patient:
    def __init__(self, name, age, severity: Severity):
        self.name = name
        self.age = age
        self.severity = severity
        # Priority is primarily based on severity (lower enum value = higher priority)
        # Age is used as a secondary factor for ties
        self.priority = (severity.value, -age)
        self.id = id(self)
        self.entry_time = id(self)  # Use as timestamp for arrival order

    def __lt__(self, other):
        # First compare by severity
        # If severity is equal, compare by age (higher age = higher priority)
        # If age is equal, compare by arrival time (earlier = higher priority)
        return (self.priority, self.entry_time) < (other.priority, other.entry_time)

    def __repr__(self):
        return f"{self.name} (Age: {self.age}, Severity: {self.severity.name})"

class HospitalPriorityQueue:
    def __init__(self):
        self.queue = []
        self.patient_dict = {}

    def add(self, patient):
        """Add a patient to the queue"""
        heapq.heappush(self.queue, patient)
        self.patient_dict[patient.name] = patient
        return f"{patient.name} added to queue with {patient.severity.name} priority"

    def remove_min(self):
        """Remove and return the highest priority patient"""
        if not self.queue:
            return "Queue is empty"
        patient = heapq.heappop(self.queue)
        del self.patient_dict[patient.name]
        return f"Serving {patient.name} ({patient.severity.name})"

    def peek(self):
        """Return the highest priority patient without removing"""
        if not self.queue:
            return "Queue is empty"
        return f"Next to be served: {self.queue[0]}"

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.queue) == 0

    def size(self):
        """Return number of patients in queue"""
        return len(self.queue)

    def update_severity(self, name, new_severity):
        """Update a patient's severity and reposition in queue"""
        if name not in self.patient_dict:
            return f"{name} not found in queue"

        # Remove existing patient
        patient = self.patient_dict[name]
        self.queue.remove(patient)
        heapq.heapify(self.queue)

        # Create new patient with updated severity but maintain other attributes
        new_patient = Patient(name, patient.age, new_severity)
        self.add(new_patient)
        return f"Patient {name}'s priority updated to {new_severity.name}"

    def display_queue(self):
        """Return a string representation of the entire queue"""
        if not self.queue:
            return "Queue is empty"
        # Sort to show in priority order
        sorted_queue = sorted(self.queue)
        return "\n".join([str(patient) for patient in sorted_queue])

    def last_in_queue(self):
        """Return the last patient in the queue"""
        if not self.queue:
            return "Queue is empty"
        # Find the patient with the lowest priority
        last_patient = max(self.queue, key=lambda x: (x.priority, x.entry_time))
        return f"Last in queue: {last_patient}"

class HospitalQueueApp:
    def __init__(self, master):
        self.master = master
        master.title("Hospital Triage Priority Queue")
        master.geometry("800x800")
        self.pq = HospitalPriorityQueue()
        self.create_widgets()

    def create_widgets(self):
        # Queue Display
        self.queue_display = tk.Text(self.master, height=20, width=60)
        self.queue_display.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        buttons = [
            ("Add Patient", self.add_patient),
            ("Remove Next Patient", self.remove_next_patient),
            ("Peek Next Patient", self.peek_next_patient),
            ("Update Patient Priority", self.update_patient_priority),
            ("Check if Empty", self.check_empty),
            ("Queue Size", self.show_queue_size),
            ("Display Full Queue", self.show_full_queue),
            ("Show Last in Queue", self.show_last_in_queue)
        ]

        for i, (text, command) in enumerate(buttons):
            row = i // 2
            col = i % 2
            btn = tk.Button(button_frame, text=text, command=command, width=25)
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
            if age is not None:
                severity_options = [s.name for s in Severity]
                severity = simpledialog.askstring(
                    "Input",
                    f"Enter severity level ({', '.join(severity_options)}):"
                )
                if severity and severity.upper() in severity_options:
                    patient = Patient(name, age, Severity[severity.upper()])
                    result = self.pq.add(patient)
                    messagebox.showinfo("Result", result)
                    self.update_display()

    def remove_next_patient(self):
        result = self.pq.remove_min()
        messagebox.showinfo("Result", result)
        self.update_display()

    def peek_next_patient(self):
        result = self.pq.peek()
        messagebox.showinfo("Next Patient", result)

    def check_empty(self):
        result = "Queue is empty" if self.pq.is_empty() else "Queue is not empty"
        messagebox.showinfo("Queue Status", result)

    def show_queue_size(self):
        size = self.pq.size()
        messagebox.showinfo("Queue Size", f"Current queue size: {size} patients")

    def update_patient_priority(self):
        name = simpledialog.askstring("Input", "Enter patient name:")
        if name:
            severity_options = [s.name for s in Severity]
            new_severity = simpledialog.askstring(
                "Input",
                f"Enter new severity level ({', '.join(severity_options)}):"
            )
            if new_severity and new_severity.upper() in severity_options:
                result = self.pq.update_severity(name, Severity[new_severity.upper()])
                messagebox.showinfo("Result", result)
                self.update_display()

    def show_full_queue(self):
        self.update_display()
        messagebox.showinfo("Full Queue", self.pq.display_queue())

    def show_last_in_queue(self):
        result = self.pq.last_in_queue()
        messagebox.showinfo("Last Patient", result)

def main():
    root = tk.Tk()
    app = HospitalQueueApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()