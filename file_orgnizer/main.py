import os 
import shutil 
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

file_types = {'images' : ['.jpg', '.png', '.jpeg', '.gif','.bmp'],
              'documents' : [ '.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
              'videos' : [ '.mp4', '.mov', '.avi'],
              'music' : ['.mp3' , '.wav', '.flac'],
              'archives' : ['.zip', '.rar', '.7z'],
              'executables' : [ '.exe', '.msi']
              }

def orgnize_files(folder, status_text):
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder,filename)

            if os.path.isdir(file_path):
                continue

            _, ext = os.path.splitext(filename)

            moved = False
            for folder_name, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(file_path, os.path.join(target_folder,filename))
                    status_text.insert(tk.END, f"Moved {filename} to {folder_name}\n")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder, 'others')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                    shutil.move(file_path, os.path.join(other_folder, filename))
                    status_text.insert(tk.END, f"Moved {filename} to others\n")
        status_text.insert(tk.END, " File organization completed!\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)
        status_text.insert(tk.END, f"Selected folder: {folder_selected}\n")

def start_organizing():
    folder = folder_path.get()
    if folder:
        status_text.insert(tk.END, "Starting organization....\n")
        orgnize_files(folder, status_text)
    else:
        messagebox.showwarning("Warning", "Please select a folder first.")

app = tk.Tk()
app.title(" File Organizer")
app.geometry("500x500")
app.resizable(False, False)

folder_path = tk.StringVar()

browse_button = tk.Button(app, text="select folder", command=browse_folder,width=20)
browse_button.pack(pady=10)

start_button = tk.Button(app, text="Organize Files", command=start_organizing, width=20)
start_button.pack(pady=5)

status_text = scrolledtext.ScrolledText(app, width=60, height=15)
status_text.pack(pady=10)

app.mainloop()