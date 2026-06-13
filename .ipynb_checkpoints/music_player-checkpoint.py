import tkinter as tk
from tkinter import filedialog
import os
import shutil  
import pygame

LIBRARY_FOLDER = "app_music_library"

class PermanentMusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Media Player Library")
        self.root.geometry("450x550")
        self.root.configure(bg="#1e1e2e") 

        pygame.mixer.init()

        self.playlist = []
        self.is_paused = False
        self.current_song_idx = None

        if not os.path.exists(LIBRARY_FOLDER):
            os.makedirs(LIBRARY_FOLDER)

        tk.Label(root, text="🎵 Vijay's Music Library", font=("Arial", 14, "bold"), bg="#1e1e2e", fg="#cdd6f4").pack(pady=15)

        self.track_status_lbl = tk.Label(
            root, text="Welcome back!", font=("Arial", 11, "italic"), 
            bg="#313244", fg="#a6e3a1", width=42, height=2, relief="flat", wraplength=320
        )
        self.track_status_lbl.pack(pady=10)

        list_frame = tk.Frame(root, bg="#1e1e2e")
        list_frame.pack(fill="both", expand=True, padx=30, pady=10)

        self.playlist_box = tk.Listbox(
            list_frame, font=("Arial", 10), bg="#11111b", fg="#cdd6f4", 
            bd=0, highlightthickness=1, highlightbackground="#313244", 
            selectbackground="#a6e3a1", selectforeground="#11111b"
        )
        self.playlist_box.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.playlist_box.yview)
        scrollbar.pack(side="right", fill="y")
        self.playlist_box.config(yscrollcommand=scrollbar.set)
        
        self.playlist_box.bind("<Double-Button-1>", lambda event: self.play_song())

        controls_frame = tk.Frame(root, bg="#1e1e2e")
        controls_frame.pack(pady=15)

        btn_style = {"font": ("Arial", 10, "bold"), "bg": "#313244", "fg": "#cdd6f4", "bd": 0, "padx": 15, "pady": 6, "cursor": "hand2"}
        tk.Button(controls_frame, text="▶ Play", command=self.play_song, **btn_style).grid(row=0, column=0, padx=8)
        tk.Button(controls_frame, text="⏸ Pause", command=self.pause_song, **btn_style).grid(row=0, column=1, padx=8)
        tk.Button(controls_frame, text="⏹ Stop", command=self.stop_song, **btn_style).grid(row=0, column=2, padx=8)

        import_btn = tk.Button(
            root, text="➕ Import Single Song File to Library", command=self.import_song_file, 
            font=("Arial", 11, "bold"), bg="#a6e3a1", fg="#11111b", bd=0, pady=10, cursor="hand2"
        )
        import_btn.pack(fill="x", padx=30, pady=(10, 25))

        self.refresh_library_view()


    def refresh_library_view(self):
        """Scans the local app directory and completely populates the user screen interface"""
        self.playlist.clear()
        self.playlist_box.delete(0, tk.END)
        
        for file in os.listdir(LIBRARY_FOLDER):
            full_path = os.path.join(LIBRARY_FOLDER, file)
            if os.path.isfile(full_path):
                self.playlist.append(full_path)
                self.playlist_box.insert(tk.END, file)
        
        if self.playlist:
            self.playlist_box.selection_set(0)
            self.track_status_lbl.config(text=f"Library Active: {len(self.playlist)} tracks loaded.")
        else:
            self.track_status_lbl.config(text="Library is empty. Import a track to start!")

    def import_song_file(self):
        """Opens up an individual file selection dialog box and saves a copy inside the app folder"""
        chosen_file_path = filedialog.askopenfilename(
            title="Select Audio Track to Import",
            filetypes=[("All Files", "*.*"), ("Audio Tracks", "*.mp3 *.wav *.ogg")]
        )
        
        if chosen_file_path:
            filename = os.path.basename(chosen_file_path)
            destination_path = os.path.join(LIBRARY_FOLDER, filename)
            
            try:
                shutil.copy(chosen_file_path, destination_path)
                
                self.refresh_library_view()
                
                new_idx = self.playlist.index(destination_path)
                self.playlist_box.selection_clear(0, tk.END)
                self.playlist_box.selection_set(new_idx)
                self.playlist_box.see(new_idx)
                
                self.track_status_lbl.config(text=f"Imported successfully: {filename}", fg="#a6e3a1")
            except Exception as e:
                self.track_status_lbl.config(text="Failed to copy file to library folder.", fg="#f38ba8")


    def play_song(self):
        try:
            selected_indices = self.playlist_box.curselection()
            if not selected_indices: return

            idx = selected_indices[0]
            song_path = self.playlist[idx]

            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            
            self.is_paused = False
            self.current_song_idx = idx
            self.track_status_lbl.config(text=f"Playing: {os.path.basename(song_path)}", fg="#a6e3a1")
        except Exception as e:
            print(f"Engine Fallback Triggered: {e}")
            self.track_status_lbl.config(text="Audio format mismatch or decoding failure.", fg="#f38ba8")

    def pause_song(self):
        if self.current_song_idx is not None:
            if not self.is_paused:
                pygame.mixer.music.pause()
                self.is_paused = True
                self.track_status_lbl.config(text="Playback Paused", fg="#f9e2af")
            else:
                pygame.mixer.music.unpause()
                self.is_paused = False
                self.track_status_lbl.config(text=f"Playing: {os.path.basename(self.playlist[self.current_song_idx])}", fg="#a6e3a1")

    def stop_song(self):
        pygame.mixer.music.stop()
        self.is_paused = False
        self.track_status_lbl.config(text="Playback Stopped", fg="#cdd6f4")

if __name__ == "__main__":
    root = tk.Tk()
    app = PermanentMusicPlayer(root)
    root.mainloop()