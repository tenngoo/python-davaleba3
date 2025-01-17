import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QLabel, QLineEdit, QPushButton
from PyQt5.uic import loadUi


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        loadUi("form.ui", self)
        # Path from my machine: loadUi("/Users/harry_apreev/app_quiz3/form.ui", self)

        # Find widgets
        self.expense_list = self.findChild(QListWidget, 'expence_list')
        self.total_label = self.findChild(QLabel, 'total_label')
        self.name_input = self.findChild(QLineEdit, 'name_input')
        self.amount_input = self.findChild(QLineEdit, 'amount_input')
        self.save_button = self.findChild(QPushButton, 'save_button')

        # Initialize total amount
        self.total_amount = 0.0

        # Connect signals
        self.save_button.clicked.connect(self.add_expense)

    def add_expense(self):
        # Get input values
        name = self.name_input.text().strip()
        amount_text = self.amount_input.text().strip()

        # Validate input
        if not name or not amount_text:
            print("Incomplete input!")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            print("Invalid amount entered!")
            return

        # Add expense to the list
        self.expense_list.addItem(f"{name} - {amount}")

        # Update total
        self.total_amount += amount
        self.total_label.setText(f"{self.total_amount}")

        # Clear input fields
        self.name_input.clear()
        self.amount_input.clear()


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
