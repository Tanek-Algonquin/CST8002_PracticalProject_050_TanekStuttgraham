import tkinter as tk
from tkinter import ttk, messagebox
from Controller.FacilityController import FacilityController  # Import Controller


class FacilityView:
    def __init__(self, root, controller):
        """Initialize the view with the main window and connect it to the controller."""
        self.root = root
        self.controller = controller
        self.root.title("Tanek Stuttgraham's Facility Management System 041012512")

        # Defining columns makes building view easier
        self.displayed_columns = [
            "Facility Name", "Facility Type", "Region", "District", "Max Number of Children"
            ]

        # Create a TreeView Widget
        self.facility_tree = ttk.Treeview(self.root, columns=self.displayed_columns, show="headings", height=10)

        # Pass column headers to row building loop
        for col in self.displayed_columns:
            self.facility_tree.heading(col, text=col)
            self.facility_tree.column(col, width=150, anchor="center")

        # Sticky nsew lets grid expand in any direction
        self.facility_tree.grid(row=0, column=0, columnspan=4, padx=9, pady=10, sticky="nsew")

        # Add scrollbar to the TreeView
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.facility_tree.yview)
        self.facility_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=4, sticky="ns")

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
        
        self.show_more_button = tk.Button(self.root, text="Show More Details", command=self.show_more_details)
        self.show_more_button.grid(row=1, column=4, padx=5, pady=5)
        
        
    def show_more_details(self):
        """Open a window with full facility data shown."""
        selected_row = self.facility_tree.selection()
        if not selected_row:
            messagebox.showwarning("Nothing Selected", "Select a facility and retry.")
            return
        
        selected_i = self.facility_tree.index(selected_row)
        facility = self.controller.model.record_list[selected_i]
        
        details_window = tk.Toplevel(self.root)
        details_window.title("Tanek Stuttgrahams Details for {facility.facilityName} page 041012512")
        # Create a frame to contain the labels
        frame = tk.Frame(details_window)
        frame.pack(padx=50, pady=40)
        #Label Keys and Data
        details_list = [
            ("Region", facility.region),
        ("District", facility.district),
        ("License Number", facility.licenseNum),
        ("Facility Name", facility.facilityName),
        ("Facility Type", facility.facilityType),
        ("Primary Address", facility.facilityAddress1),
        ("Secondary Address", facility.facilityAddress2),
        ("Tertiary Address", facility.facilityAddress3),
        ("Max Number of Children", facility.maxNumofChildren),
        ("Max Number of Infants", facility.maxNumInfants),
        ("Max Number of Preschool-Aged Children", facility.maxNumPreChildren),
        ("Max Number of School-Aged Children", facility.maxNumSAgeChildren),
        ("Language of Service", facility.LangOfService),
        ("Operator ID", facility.operatorId),
        ("Designated Facility", facility.designatedFacility)
    ]
        # Create labels for each detail
        row = 0
        for label, value in details_list:
            tk.Label(frame, text=f"{label}: {value}", anchor="w", width=40, justify="left").grid(row=row, column=0, padx=5, pady=10, sticky="w")
            row += 1

        # Add a close button at the bottom
        close_button = tk.Button(details_window, text="Close", command=details_window.destroy)
        close_button.pack(pady=10)
        
            
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
        for i, attribute in enumerate(self.columns):
            label = tk.Label(add_window, text=attribute)
            label.grid(row=i, column=0, padx=5, pady=2, sticky="w")

            entry = tk.Entry(add_window, width=40)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entry_fields[attribute] = entry

        # Submit button
        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_facility(add_window))
        submit_button.grid(row=len(self.columns), column=0, columnspan=2, pady=10)

    def add_facility(self, window):
        """Retrieve input values, create a facility object, and add it to the model."""
        facility_data = {}

        try:
            for key in self.columns:
                facility_data[key] = self.entry_fields[key].get()

            # Convert numerical values for child capacities
            numerical_keys = [
                "Max Number of Children", "Max Number of Infants", "Max Number of Preschool-Aged Children",
                "Max Number of School Age Children"
            ]
            for key in numerical_keys:
                facility_data[key] = int(facility_data[key])

            # Send facility data to controller
            self.controller.add_facility(facility_data)

            # Close the window and refresh list
            window.destroy()
            self.update_facility_list()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for child capacities.")

    def delete_facility(self):
        """Delete the selected facility."""
        selected_item = self.facility_tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a facility to delete.")
            return

        # Get selected item details
        selected_index = self.facility_tree.index(selected_item)
        self.controller.delete_facility(selected_index)

        # Refresh list
        self.update_facility_list()

    def update_facility_list(self):
        """Update the Treeview with the latest facilities."""
        # Clear the existing entries in the Treeview
        for item in self.facility_tree.get_children():
            self.facility_tree.delete(item)

        # Insert new facility data
        for facility in self.controller.model.record_list:
            self.facility_tree.insert("", "end", values=[
                facility.facilityName, facility.facilityType, facility.region,  facility.district,  facility.maxNumofChildren
            ])
