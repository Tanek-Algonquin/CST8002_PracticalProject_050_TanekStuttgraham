import tkinter as tk
from tkinter import messagebox
from Controller.FacilityController import FacilityController # Import Controller


class FacilityView:
    def __init__(self, root, controller):
        """Initialize the view with the main window and connect it to the controller."""
        self.root = root
        self.controller = controller
        self.root.title("Facility Management System")
        
        # Create a listbox to display facilities
        self.facility_listbox = tk.Listbox(self.root, width=50, height=10)
        self.facility_listbox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons for various actions
        self.create_buttons()

    def create_buttons(self):
        """Create buttons to interact with the controller."""
        self.load_button = tk.Button(self.root, text="Load Facilities", command=self.load_facilities)
        self.load_button.grid(row=1, column=0, padx=5, pady=5)

        self.save_button = tk.Button(self.root, text="Save Facilities", command=self.save_facilities)
        self.save_button.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Add Facility", command=self.open_add_facility_window)
        self.add_button.grid(row=1, column=2, padx=5, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Facility", command=self.delete_facility)
        self.delete_button.grid(row=1, column=3, padx=5, pady=5)

    def load_facilities(self):
        """Call the controller's method to load facilities."""
        self.controller.load_facilities()
        self.update_facility_list()

    def save_facilities(self):
        """Call the controller's method to save facilities."""
        self.controller.save_facilities()

    def open_add_facility_window(self):
        """Open a separate window to input facility details."""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Facility")

        # Dictionary to store entry fields
        self.entry_fields = {}

        # Labels and Entry fields for each facility attribute
        attributes = [
            "Region", "District", "License Number", "Facility Name", "Facility Type",
            "Facility Address 1", "Facility Address 2", "Facility Address 3",
            "Max Number of Children", "Max Number of Infants", "Max Number of Preschool-Aged Children",
            "Max Number of School Age Children", "Language of Service", "Operator Id", "Designated Facility"
        ]

        for i, attribute in enumerate(attributes):
            label = tk.Label(add_window, text=attribute)
            label.grid(row=i, column=0, padx=5, pady=2, sticky="w")
            
            entry = tk.Entry(add_window, width=40)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entry_fields[attribute] = entry  

        # Submit button
        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_facility(add_window))
        submit_button.grid(row=len(attributes), column=0, columnspan=2, pady=10)

    def add_facility(self, window):
        """Retrieve input values, create a facility object, and add it to the model."""
        facility_data = {}

        try:
            facility_data["Region"] = self.entry_fields["Region"].get()
            facility_data["District"] = self.entry_fields["District"].get()
            facility_data["License Number"] = self.entry_fields["License Number"].get()
            facility_data["Facility Name"] = self.entry_fields["Facility Name"].get()
            facility_data["Facility Type"] = self.entry_fields["Facility Type"].get()
            facility_data["Facility Address 1"] = self.entry_fields["Facility Address 1"].get()
            facility_data["Facility Address 2"] = self.entry_fields["Facility Address 2"].get()
            facility_data["Facility Address 3"] = self.entry_fields["Facility Address 3"].get()
            facility_data["Max Number of Children"] = int(self.entry_fields["Max Number of Children"].get())
            facility_data["Max Number of Infants"] = int(self.entry_fields["Max Number of Infants"].get())
            facility_data["Max Number of Preschool-Aged Children"] = int(self.entry_fields["Max Number of Preschool-Aged Children"].get())
            facility_data["Max Number of School Age Children"] = int(self.entry_fields["Max Number of School Age Children"].get())
            facility_data["Language of Service"] = self.entry_fields["Language of Service"].get()
            facility_data["Operator Id"] = self.entry_fields["Operator Id"].get()
            facility_data["Designated Facility"] = self.entry_fields["Designated Facility"].get()

            # Send facility data to controller
            self.controller.add_facility(facility_data)

            # Close the window and refresh list
            window.destroy()
            self.update_facility_list()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for child capacities.")

    def delete_facility(self):
        """Delete the selected facility."""
        try:
            selected_index = self.facility_listbox.curselection()[0]
            self.controller.delete_facility(selected_index)
            self.update_facility_list()
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a facility to delete.")

    def update_facility_list(self):
        """Update the listbox with the latest facilities."""
        self.facility_listbox.delete(0, tk.END)
        for facility in self.controller.model.record_list:
            self.facility_listbox.insert(tk.END, f"{facility.facilityName} - {facility.district}")

