import unittest
from unittest.mock import patch
import tkinter as tk
import server.client as client
import database.database_validations as database_validations
import image_things.picture_wia_laptop_camera as picture_wia_laptop_camera
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.window = tk.Tk()
        self.window.geometry("400x300")
        self.window.title("Item Manager")
        self.window.config(bg="#f0f0f0")
        self.add_item_button = tk.Button(self.window, text="Add Item", command=main.add_item_click, bg="lightgray", fg="black", font=("Arial", 14), borderwidth=2, relief="solid")
        self.take_item_button = tk.Button(self.window, text="Take Item", command=main.take_item_click, bg="lightgray", fg="black", font=("Arial", 14), borderwidth=2, relief="solid")
        self.input_field = tk.Entry(self.window, width=30, font=("Arial", 14), bg="lightgray", borderwidth=2, relief="solid")
        self.label = tk.Label(self.window, text="Choose an action", font=("Arial", 14), bg="#f0f0f0")

    def test_validate_input_valid(self):
        self.assertTrue(main.validate_input("123456"))

    def test_validate_input_invalid(self):
        self.assertFalse(main.validate_input("1234567"))
        self.assertFalse(main.validate_input("a23456"))
        self.assertFalse(main.validate_input("12345"))

    def test_add_item_click(self):
        self.add_item_button.invoke()
        self.assertEqual(self.label.cget("text"), "Enter Product ID")
        self.add_item_button.pack_forget()
        self.take_item_button.pack_forget()
        self.assertEqual(self.add_item_button.winfo_ismapped(), False)
        self.assertEqual(self.take_item_button.winfo_ismapped(), False)

    def test_take_item_click(self):
        self.take_item_button.invoke()
        self.assertEqual(self.label.cget("text"), "Enter your code")
        self.add_item_button.pack_forget()
        self.take_item_button.pack_forget()
        self.assertEqual(self.add_item_button.winfo_ismapped(), False)
        self.assertEqual(self.take_item_button.winfo_ismapped(), False)

    @patch('builtins.print')
    def test_submit_click_valid(self, mock_print):
        self.input_field.insert(0, "123456")
        self.input_field.pack()
        self.assertEqual(self.input_field.winfo_ismapped(), True)
        main.submit_click(self.input_field, self.submit_button)
        mock_print.assert_called_with(True)

    @patch('builtins.print')
    def test_submit_click_invalid(self, mock_print):
        self.input_field.insert(0, "654321")
        self.input_field.pack()
        self.assertEqual(self.input_field.winfo_ismapped(), True)
        with patch.object(tk.messagebox, 'showerror') as mock_error:
            main.submit_click(self.input_field, self.submit_button)
            mock_error.assert_called_once()
        mock_print.assert_not_called()

    def tearDown(self):
        self.window.destroy()

if __name__ == '__main__':
    unittest.main()
