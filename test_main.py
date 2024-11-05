import unittest
from unittest.mock import MagicMock
import tkinter as tk
from src.gui.sudoku_gui import GUI
from Sudoku import main

class TestSudokuApp(unittest.TestCase):

    def test_gui_initialization(self):
        # Mocking tkinter.Tk class
        mock_tk = MagicMock(spec=tk.Tk)
        tk.Tk = mock_tk
        
        # Mock the GUI methods
        mock_gui = MagicMock(spec=GUI)
        GUI.return_value = mock_gui

        # Call the main function (this will initialize the GUI)
        main()

        # Check if Tk() was called
        mock_tk.assert_called_once()
        
        # Check if methods were called
        mock_gui.generate_sudoku_board.assert_called_once()
        mock_gui.right_side_option_block.assert_called_once()

if __name__ == '__main__':
    unittest.main()
