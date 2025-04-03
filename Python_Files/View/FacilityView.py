import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, messagebox
from Controller.FacilityController import FacilityController  # Import Controller


class FacilityView:
    """The visual representation for this program. Creates a window with a datatable with buttons intended to manipulate the contents of the table."""
    def __init__(self, root, controller):
        """Initialize the view with the main window and connect it to the controller."""
        self.root = root
        self.controller = controller
        self.root.title("Tanek Stuttgraham's Facility Management System 041012512")
        self.current_index = None
        
        # Defining columns makes building view easier
        self.displayed_columns = ["Facility Name", "Facility Type", "Facility Id", "Region",
                                  "District", "Main Add", "Province", "Postal",
                                  "Children #", "Infant #", "P-A Child #", "S-A Child #",
                                  "Language", "Op. Id", "Facilities #", "Licence #"]
        
        # Create a TreeView Widget
        self.facility_tree = ttk.Treeview(self.root, columns=self.displayed_columns, show="headings", height=10)
        # Pass column headers to row building loop
        for col in self.displayed_columns:
            self.facility_tree.heading(col, text=col)
            self.facility_tree.column(col, width=75, anchor="center")
        
        # Grid the Treeview widget in the first row, first column and make it expand
        self.facility_tree.grid(row=0, column=0, columnspan=3, padx=9, pady=10, sticky="nsew")
        
        # Add scrollbar to the TreeView
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.facility_tree.yview)
        self.scrollbar.grid(row=0, column=5, sticky="ns")  # Place the scrollbar in the last column
        
        # Configure the Treeview to use the scrollbar
        self.facility_tree.configure(yscroll=self.scrollbar.set)
        
        # Create buttons for various actions
        self.create_buttons()

    def create_buttons(self):
        """Create buttons to interact with the controller."""
        #Uniform Button Size
        button_width = 22
        button_height = 2
        # Place buttons across different columns in row 1 to ensure proper spacing
        self.load_button = tk.Button(self.root, text="Load Updated Facilities", command=self.load_facilities, width= button_width, height= button_height )
        self.load_button.grid(row=1, column=1, padx=5, pady=5)

        self.load_og_facilities = tk.Button(self.root,  text="Load Original Facilities", command=self.load_original_facilities, width= button_width, height= button_height)
        self.load_og_facilities.grid(row=1, column=0, padx=5, pady=5)
        
        self.reset_changed_facilities = tk.Button(self.root,  text="Reset Changed Facilities List", command=self.load_original_to_changed, width= button_width, height= button_height)
        self.reset_changed_facilities.grid(row=1, column=2, padx=5, pady=5) 
       
        self.bar_graph_button = tk.Button(self.root, text="Bar Graph", command=self.show_bar_graph_window, width= button_width, height= button_height)
        self.bar_graph_button.grid(row=1, column=3, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Add Facility", command=self.open_add_facility_window, width= button_width, height= button_height)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.edit_button = tk.Button(self.root, text="Edit Facility", command=self.open_edit_facility_window, width= button_width, height= button_height)
        self.edit_button.grid(row=2, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Selected Facility", command=self.delete_facility, width= button_width, height= button_height)
        self.delete_button.grid(row=2, column=2, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Changed Facilities", command=self.delete_changed_facilities, width= button_width, height= button_height)
        self.delete_button.grid(row=2, column=3, padx=5, pady=5)


    def show_bar_graph_window(self):
        """Opens a new window and displays a bar graph for the selected row, or allows user to choose a category if no row is selected."""
        selected_item = self.facility_tree.selection()  # Get selected row
        
        if selected_item:
            # Get the record data
            record = self.facility_tree.item(selected_item[0], "values")
            
            # Print the selected record for debugging or inspection
            print("Selected Record Data:", record)
            
            # If you want to print each field with its column name for clarity
            for i, col_name in enumerate(self.displayed_columns):
                print(f"{col_name}: {record[i]}")
            
            self.generate_graph_from_record(record)  # Call method to generate graph for record
        else:
            # Create a window for manual column selection
            self.create_graph_window()
    
    def generate_graph_from_record(self, record):
        """Generate a bar graph using the data from a selected record, including only the max children and infant stats."""
        # Define graph window
        graph_window = tk.Toplevel(self.root)
        graph_window.title(f"Facility Record Bar Graph for {record[0]}")  # Using Facility Name for the title
        graph_window.geometry("800x500")

        # Define columns to include in the graph (max children and infant stats)
        stats_columns = ["Children #", "Infant #", "P-A Child #", "S-A Child #"]
        
        # Extract the data for these specific columns
        filtered_columns = [col for col in stats_columns]
        filtered_values = []
        for col in filtered_columns:
            # Get the index of the column in the displayed columns
            index = self.displayed_columns.index(col)
            
            # Get the value from the record for the current column
            value = record[index]
            
            # Convert to integer if it's a digit, otherwise set to 0
            filtered_values.append(int(value) if str(value).isdigit() else 0)


        # Create bar graph
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(filtered_columns, filtered_values, color='blue')
        ax.set_title("Children and Infant Statistics")
        ax.set_xlabel("Category")
        ax.set_ylabel("Number of Facilities")

        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        fig.tight_layout()

        # Embed Matplotlib chart in Tkinter window
        canvas_figure = FigureCanvasTkAgg(fig, master=graph_window)
        canvas_figure.draw()
        canvas_figure.get_tk_widget().pack(fill=tk.BOTH, expand=True)


    def create_graph_window(self):
        """Creates a window allowing the user to select a column for the bar graph."""
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Facility Bar Graph")
        graph_window.geometry("1000x600")

        frame = tk.Frame(graph_window)
        frame.pack(fill=tk.BOTH, expand=1)

        canvas = tk.Canvas(frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        column_options = ["facilityType", "region", "district", "LangOfService"]
        selected_column = tk.StringVar(graph_window)
        selected_column.set(column_options[0])  # Default selection

        dropdown_label = tk.Label(inner_frame, text="Select Column:")
        dropdown_label.pack()
        dropdown_menu = tk.OptionMenu(inner_frame, selected_column, *column_options)
        dropdown_menu.pack()

        def generate_graph():
            column = selected_column.get()
            categories, values = self.controller.get_facility_chart_data(column)

            fig, ax = plt.subplots(figsize=(9, 6))
            ax.bar(categories, values, color='blue')
            ax.set_title(f'Facility Distribution by {column}')
            ax.set_xlabel(column)
            ax.set_ylabel('Number of Facilities')

            plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
            fig.tight_layout()

            canvas_figure = FigureCanvasTkAgg(fig, master=inner_frame)
            canvas_figure.draw()
            canvas_figure.get_tk_widget().pack()

            inner_frame.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))

        generate_button = tk.Button(inner_frame, text="Generate Graph", command=generate_graph)
        generate_button.pack()

            
    def load_one_original_facility(self):
        """Load  the first one."""
       
        self.controller.get_first_available_facility()
        self.update_facility_list()
        
    def show_more_details(self):
        """Open a window with full facility data shown."""
        selected_row = self.facility_tree.selection()
        if not selected_row:
            messagebox.showwarning("Nothing Selected", "Select a facility and retry.")
            return
        selected_i = self.facility_tree.index(selected_row)
        self.current_index = selected_i  #Grabs Number
        facility = self.controller.model.record_list[selected_i]
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Tanek Stuttgraham's Details for {facility.facilityName} page 041012512")
        # Create a frame to contain the labels
        frame = tk.Frame(details_window)
        frame.pack(padx=50, pady=40)
        # Label Keys and Data
        details_list = [
            ("Facility Id", facility.facilityId),
            ("Region", facility.region),
            ("District", facility.district),
            ("License Number", facility.licenceNum),
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
        # Adds a next Buttom to the bottom
        next_button = tk.Button(details_window, text="Next Record", command=lambda: self.show_more_details_by_index(self.current_index+1))
        next_button.pack(pady=10)
        # Add a close button at the bottom
        close_button = tk.Button(details_window, text="Close", command=details_window.destroy)
        close_button.pack(pady=10)
        # Adds a previous Buttom to the bottom
        previous_button = tk.Button(details_window, text="Previous Record", command=lambda: self.show_more_details_by_index(self.current_index-1))
        previous_button.pack(pady=10)
            
    def load_original_to_changed(self):
        """Loads original list into changed list"""
        self.controller.load_original_to_changed()
        self.controller.load_facilities()
        self.update_facility_list()


    def load_facilities(self):
        """Call the controller's method to load facilities."""
        self.controller.load_facilities()
        self.update_facility_list()
        
    def load_original_facilities(self):
        """Call the controller's method to load facilities."""
        self.controller.load_original_facilities()
        self.update_facility_list()

    def save_facilities(self):
        """Call the controller's method to save facilities."""
        self.controller.save_facilities()

    def open_add_facility_window(self):
        """Open a separate window to input facility details."""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Facility Tanek Stuttgraham 041012512")

        # Dictionary to store entry fields
        self.entry_fields = {}
        
        headers = ["Region", "District", "Licence Number", "Facility Name", "Facility Type",
           "Facility Address 1", "Facility Address 2", "Facility Address 3",
           "Max Number of Children", "Max Number of Infants",
           "Max-Number-of-Preschool-Aged-Children", "Max-Number-of-School-Age-Children",
           "Language of Service", "Operator Id", "Designated Facility"]


        # Labels and Entry fields for each facility attribute
        for i, header in enumerate(headers):
            label = tk.Label(add_window, text=header)
            label.grid(row=i, column=0, padx=5, pady=2, sticky="w")

            entry = tk.Entry(add_window, width=40)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entry_fields[header] = entry

        # Submit button
        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_facility(add_window))
        submit_button.grid(row=len(headers), column=0, columnspan=2, pady=10)

    def add_facility(self, window):
        """Retrieve input values, create a facility object, and add it to the model."""
        facility_data = {}

        try:
            for key in self.entry_fields:
                facility_data[key] = self.entry_fields[key].get()

            # Convert numerical values for child capacities
            numerical_keys = [
                "Max Number of Children", "Max Number of Infants",
            "Max-Number-of-Preschool-Aged-Children", "Max-Number-of-School-Age-Children"
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

        # Get all column values for debugging
        facility_values = self.facility_tree.item(selected_item, "values")
        print(f"Selected row values: {facility_values}")  # Debugging

        # Identify the correct index for facilityId
        facilityId = facility_values[1]  # Change this if needed

        try:
            facilityId = int(facilityId)  # Ensure it's an integer
        except ValueError:
            print(f"Error: Facility ID is not a valid integer. Got: {facilityId}")
            return

        print(f"Attempting to delete Facility ID: {facilityId}")  # Debugging

        # Call the controller to delete the facility
        self.controller.delete_facility(facilityId)

        # Refresh the list
        self.update_facility_list()
        
        
    def delete_changed_facilities(self):
        """Resets the Changed facility list"""
        self.controller.delete_changed_facilities()
        self.controller.model.record_list = [] #refresh local memory
        self.update_facility_list()
        
    def open_edit_facility_window(self):
        """Opens a window that allows editing facilities"""
        selected_row = self.facility_tree.selection()
        if not selected_row:
            messagebox.showwarning("No Selection", "Please select facility to edit")
            return
        
        selected_i = self.facility_tree.index(selected_row)
        facility_data = self.controller.get_facility_data(selected_i)

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Facility Window Tanek Stuttgraham 041012512")
        
        self.edit_fields = {}
        
        headers = ["Region", "District", "Licence Number", "Facility Name", "Facility Type",
           "Facility Address 1", "Facility Address 2", "Facility Address 3",
           "Max Number of Children", "Max Number of Infants",
           "Max-Number-of-Preschool-Aged-Children", "Max-Number-of-School-Age-Children",
           "Language of Service", "Operator Id", "Designated Facility"]
        
        # Labels and Entry fields for each facility attribute
        for i, header in enumerate(headers):
            label = tk.Label(edit_window, text=header)
            label.grid(row=i, column=0, padx=5, pady=2, sticky="w")
            entry = tk.Entry(edit_window, width=40)
            entry.insert(0, str(facility_data[header]))
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.edit_fields[header] = entry     
        # Submit button
        submit_button = tk.Button(edit_window, text="Submit", command=lambda: self.save_edited_facility(edit_window, selected_i))
        submit_button.grid(row=len(headers), column=0, columnspan=2, pady=10)
   
    def save_edited_facility(self, window, index):
        """Retrieve edited facility data from the UI and send it to the controller."""
        facility_data = {key: self.edit_fields[key].get() for key in self.edit_fields}

        # Send the edited data to the controller
        self.controller.update_facility(index, facility_data)

        window.destroy()
        self.update_facility_list()

    def update_facility_list(self):
        """Update the Treeview with the latest facilities."""
        # Clear the existing entries in the Treeview
        for item in self.facility_tree.get_children():
            self.facility_tree.delete(item)

        # Insert new facility data
        for facility in self.controller.model.record_list:
            self.facility_tree.insert("", "end", values=[
                facility.facilityName, facility.facilityType, facility.facilityId,  facility.region,
                facility.district, facility.facilityAddress1, facility.facilityAddress2, facility.facilityAddress3,
                facility.maxNumofChildren, facility.maxNumInfants, facility.maxNumPreChildren, facility.maxNumSAgeChildren,
                facility.LangOfService, facility.operatorId, facility.designatedFacility, facility.licenceNum
            ])
