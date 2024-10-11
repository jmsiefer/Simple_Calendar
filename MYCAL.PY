import tkinter as tk
import calendar
from datetime import datetime

class SimpleCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar")
        
        # Manually adjustable window height
        self.window_height = 210
        
        # Set consistent window size with adjustable height
        self.root.geometry(f"280x{self.window_height}")
        self.root.resizable(False, False)  # Prevent window resizing

        # Get current date, year, and month
        now = datetime.now()
        self.current_day = now.day
        self.current_year = now.year
        self.current_month = now.month
        
        self.year = self.current_year
        self.month = self.current_month
        
        # Create a fixed frame for navigation buttons and month label
        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack()

        # Fixed placement of navigation buttons and label
        self.prev_button = tk.Button(self.nav_frame, text="<", command=self.prev_month, width=2)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.month_label = tk.Label(self.nav_frame, text="", font=("Helvetica", 16), anchor="center", width=15)
        self.month_label.grid(row=0, column=1)

        self.next_button = tk.Button(self.nav_frame, text=">", command=self.next_month, width=2)
        self.next_button.grid(row=0, column=2, padx=10)

        # Calendar display area
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack(pady=5)  # Adjust as needed

        # Draw the initial calendar
        self.draw_calendar(self.year, self.month)
    
    def draw_calendar(self, year, month):
        # Clear the previous calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        # Update the month label
        self.month_label.config(text=f"{calendar.month_name[month]} {year}")
        
        # Get the calendar for the current month
        cal = calendar.monthcalendar(year, month)
        
        # Display the weekday headers
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Helvetica", 10, "bold")).grid(row=1, column=i, padx=5, pady=1)
        
        # Display the days of the month and highlight today if in the current month
        for row, week in enumerate(cal, start=2):
            for col, day in enumerate(week):
                if day != 0:
                    # Highlight today's date with a red background
                    if day == self.current_day and year == self.current_year and month == self.current_month:
                        tk.Label(self.calendar_frame, text=str(day), font=("Helvetica", 10), bg="red", fg="white").grid(row=row, column=col, padx=5, pady=1)
                    else:
                        tk.Label(self.calendar_frame, text=str(day), font=("Helvetica", 10)).grid(row=row, column=col, padx=5, pady=1)
    
    def prev_month(self):
        # Go to the previous month
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.draw_calendar(self.year, self.month)
    
    def next_month(self):
        # Go to the next month
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.draw_calendar(self.year, self.month)

# Create the application
root = tk.Tk()
app = SimpleCalendarApp(root)
root.mainloop()
