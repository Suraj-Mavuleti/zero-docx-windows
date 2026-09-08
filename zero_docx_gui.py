import customtkinter as ctk
import threading
import time
import math
import socket
import urllib.request
import json
import sqlite3
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Zero Docx - Word Processor")
        self.geometry("800x600")
        self.configure(fg_color="#1a1a24")
        
        # Header
        self.header = ctk.CTkLabel(self, text="Zero Docx - Word Processor", font=("Helvetica", 24, "bold"), text_color="#00C7FF")
        self.header.pack(pady=20)
        
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=10)
        
        self.setup_ui()
        
    
    def setup_ui(self):
        toolbar = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        toolbar.pack(fill=ctk.X, pady=5)
        
        ctk.CTkButton(toolbar, text="Save Document", command=self.save).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(toolbar, text="Clear", command=self.clear).pack(side=ctk.LEFT, padx=5)
        
        self.text_area = ctk.CTkTextbox(self.main_frame, font=("Times New Roman", 16))
        self.text_area.pack(fill=ctk.BOTH, expand=True, pady=10)
        self.text_area.insert("0.0", "Start writing your document here...")
        
    def save(self):
        with open("document.txt", "w") as f:
            f.write(self.text_area.get("0.0", "end"))
        self.header.configure(text="Document Saved!")
        
    def clear(self):
        self.text_area.delete("0.0", "end")


if __name__ == "__main__":
    app = App()
    app.mainloop()
