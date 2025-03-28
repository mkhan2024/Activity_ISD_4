"""The module defines the ContactList class."""

__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Md Apurba Khan"

from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot

class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts.

    This class allows users to add and remove contacts via a graphical interface,
    utilizing event-driven programming with PySide6 signals and slots.
    """

    def __init__(self):
        """Initializes a new instance of the ContactList class.

        Sets up the window by calling the widget initialization method and
        connects button click signals to their respective event handler slots.
        """
        super().__init__()
        self.__initialize_widgets()
        # Connect the add_button clicked signal to the on_add_contact slot
        self.add_button.clicked.connect(self.__on_add_contact)
        # Connect the remove_button clicked signal to the on_remove_contact slot
        self.remove_button.clicked.connect(self.__on_remove_contact)

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def __on_add_contact(self):
        """Handle the Add Contact button click event.

        Extracts the contact name and phone number from input fields, validates
        them, and adds them to the table if both are provided. Updates the status
        label with feedback on the action's success or failure.
        """
        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if len(name) > 0 and len(phone) > 0:
            # Determine the current row count and insert a new row
            row_position = self.contact_table.rowCount()
            self.contact_table.insertRow(row_position)

            # Create table items for name and phone
            name_item = QTableWidgetItem(name)
            phone_item = QTableWidgetItem(phone)

            # Add items to the table
            self.contact_table.setItem(row_position, 0, name_item)
            self.contact_table.setItem(row_position, 1, phone_item)

            # Update status label with success message
            self.status_label.setText(f"Added contact: {name}")
        else:
            # Update status label with error message
            self.status_label.setText("Please enter a contact name and phone number.")

    @Slot()
    def __on_remove_contact(self):
        """Handle the Remove Contact button click event.

        Removes the selected contact from the table after user confirmation via
        a dialog box. Updates the status label based on the user's selection and
        response to the confirmation prompt.
        """
        selected_row = self.contact_table.currentRow()

        if selected_row >= 0:
            # Prompt user to confirm removal
            reply = QMessageBox.question(
                self,
                "Remove Contact",
                "Are you sure you want to remove this contact?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                # Remove the selected row and update status
                self.contact_table.removeRow(selected_row)
                self.status_label.setText("Contact removed.")
        else:
            # Update status if no row is selected
            self.status_label.setText("Please select a row to be removed.")