import tkinter as tk
from Model.facilityModel import FacilityModel
from View.FacilityView import FacilityView
from Controller.FacilityController import FacilityController

if __name__ == "__main__":
    root = tk.Tk()
    model = FacilityModel()
    controller = FacilityController(model, None)  # Pass model
    view = FacilityView(root, controller)  # Pass controller
    controller.view = view  # Set view in controller
    root.mainloop()
