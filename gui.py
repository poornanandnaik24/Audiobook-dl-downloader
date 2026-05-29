import os
import subprocess
import threading
import multiprocessing
import tkinter as tk
from tkinter import filedialog, messagebox
import http.cookiejar
import webbrowser
import webview

import customtkinter as ctk

# Set appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def run_webview_process():
    import webview
    import time
    import http.cookiejar
    import threading
    import sys
    
    extracted_cookies = []
    window_closed = threading.Event()
    
    def tracker(window):
        window.events.closed += lambda: window_closed.set()
        while not window_closed.is_set():
            try:
                cookies = window.get_cookies()
                if cookies:
                    extracted_cookies.clear()
                    extracted_cookies.extend(cookies)
            except Exception:
                pass
            time.sleep(1)
    
    try:
        window = webview.create_window('Log in, then CLOSE this window', 'https://www.google.com', width=800, height=600)
        webview.start(tracker, window, private_mode=False)
        
        if extracted_cookies:
            temp_cookie_path = os.path.abspath("temp_webview_cookies.txt")
            mcj = http.cookiejar.MozillaCookieJar(temp_cookie_path)
            
            for c in extracted_cookies:
                for key, morsel in c.items():
                    cookie = http.cookiejar.Cookie(
                        version=0,
                        name=morsel.key,
                        value=morsel.value,
                        port=None, port_specified=False,
                        domain=morsel['domain'] if morsel['domain'] else '',
                        domain_specified=bool(morsel['domain']),
                        domain_initial_dot=morsel['domain'].startswith('.') if morsel['domain'] else False,
                        path=morsel['path'] if morsel['path'] else '/',
                        path_specified=bool(morsel['path']),
                        secure=bool(morsel['secure']),
                        expires=None,
                        discard=False,
                        comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False
                    )
                    mcj.set_cookie(cookie)
            
            mcj.save(ignore_discard=True, ignore_expires=True)
    except Exception as e:
        print(f"Webview error: {e}")
    finally:
        sys.exit(0)

def get_resource_path(relative_path):
    import sys, os
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Naik's Audiobook Downloader v1.0")
        self.geometry("700x600")

        icon_path = get_resource_path("icon.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(6, weight=1)

        # Title Frame
        self.title_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.title_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="ew")
        self.title_frame.grid_columnconfigure(0, weight=1)
        
        self.title_label = ctk.CTkLabel(self.title_frame, text="Naik's Audiobook Downloader v1.0", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, sticky="w")
        
        self.sites_button = ctk.CTkButton(self.title_frame, text="Supported Sites", width=120, command=self.show_supported_sites)
        self.sites_button.grid(row=0, column=1, sticky="e")

        self.about_button = ctk.CTkButton(self.title_frame, text="About", width=60, command=self.show_about)
        self.about_button.grid(row=0, column=2, padx=(10, 0), sticky="e")

        # URL Input
        self.url_label = ctk.CTkLabel(self, text="URL:")
        self.url_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.url_entry = ctk.CTkEntry(self, placeholder_text="Enter audiobook URL")
        self.url_entry.grid(row=1, column=1, columnspan=2, padx=(0, 20), pady=10, sticky="ew")

        # Authentication Frame
        self.auth_frame = ctk.CTkFrame(self)
        self.auth_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
        self.auth_frame.grid_columnconfigure(1, weight=1)
        self.auth_frame.grid_columnconfigure(3, weight=1)

        self.auth_label = ctk.CTkLabel(self.auth_frame, text="Authentication (Optional, depending on source)", font=ctk.CTkFont(weight="bold"))
        self.auth_label.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5), sticky="w")

        self.username_label = ctk.CTkLabel(self.auth_frame, text="Username:")
        self.username_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.username_entry = ctk.CTkEntry(self.auth_frame, placeholder_text="Username")
        self.username_entry.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="ew")

        self.password_label = ctk.CTkLabel(self.auth_frame, text="Password:")
        self.password_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.password_entry = ctk.CTkEntry(self.auth_frame, placeholder_text="Password", show="*")
        self.password_entry.grid(row=1, column=3, padx=(0, 10), pady=5, sticky="ew")

        # Embedded Browser Login
        self.webview_button = ctk.CTkButton(self.auth_frame, text="Login via Embedded Browser (Gets Cookies)", command=self.open_embedded_browser)
        self.webview_button.grid(row=2, column=0, columnspan=4, padx=10, pady=(15, 10), sticky="ew")

        # Output Directory
        self.output_label = ctk.CTkLabel(self, text="Save To:")
        self.output_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.output_entry = ctk.CTkEntry(self, placeholder_text="Select Output Directory")
        self.output_entry.grid(row=3, column=1, padx=(0, 10), pady=10, sticky="ew")
        self.output_button = ctk.CTkButton(self, text="Browse", command=self.browse_output)
        self.output_button.grid(row=3, column=2, padx=(0, 20), pady=10)

        # Download Button
        self.download_button = ctk.CTkButton(self, text="Download", command=self.start_download)
        self.download_button.grid(row=4, column=0, columnspan=3, padx=20, pady=20)

        # Output Log Text Box
        self.log_label = ctk.CTkLabel(self, text="Log Output:")
        self.log_label.grid(row=5, column=0, padx=20, pady=(10, 0), sticky="w")
        self.log_textbox = ctk.CTkTextbox(self, state="disabled")
        self.log_textbox.grid(row=6, column=0, columnspan=3, padx=20, pady=(0, 20), sticky="nsew")

        # Process handle
        self.process = None

        self.process = None

    def open_embedded_browser(self):
        # We must use multiprocessing because webview requires a main thread to run its GUI loop.
        self.webview_button.configure(state="disabled", text="Browser Open...")
        p = multiprocessing.Process(target=run_webview_process)
        p.start()
        threading.Thread(target=self._monitor_webview, args=(p,), daemon=True).start()

    def _monitor_webview(self, process):
        process.join()
        self.after(0, lambda: self.webview_button.configure(state="normal", text="Login via Embedded Browser (Gets Cookies)"))
        
        temp_cookie_path = os.path.abspath("temp_webview_cookies.txt")
        if os.path.exists(temp_cookie_path) and os.path.getmtime(temp_cookie_path) > getattr(self, '_last_cookie_time', 0):
            self.after(0, lambda: self.append_log(f"Successfully extracted cookies to {temp_cookie_path}"))
            self.after(0, lambda: messagebox.showinfo("Cookies Captured", "Successfully captured login cookies!"))
            self._last_cookie_time = os.path.getmtime(temp_cookie_path)
        else:
            self.after(0, lambda: self.append_log("Browser closed, but no new cookies were found."))

    def browse_output(self):
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, directory)

    def append_log(self, text):
        self.log_textbox.configure(state="normal")
        self.log_textbox.insert(tk.END, text + "\n")
        self.log_textbox.see(tk.END)
        self.log_textbox.configure(state="disabled")

    def start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Missing URL", "Please enter an audiobook URL.")
            return

        # Prepare arguments
        args = ["audiobook-dl"]
        
        username = self.username_entry.get().strip()
        if username:
            args.extend(["--username", username])
            
        password = self.password_entry.get()
        if password:
            args.extend(["--password", password])

        cookie_file = os.path.abspath("temp_webview_cookies.txt")
        if os.path.exists(cookie_file):
            args.extend(["--cookie", cookie_file])

        output_dir = self.output_entry.get().strip()
        if output_dir:
            args.extend(["--output", os.path.join(output_dir, "{title}")])

        args.append(url)

        self.append_log(f"Starting download: {' '.join(args)}")
        self.download_button.configure(state="disabled", text="Downloading...")
        
        # Run in thread
        threading.Thread(target=self.run_subprocess, args=(args,), daemon=True).start()

    def run_subprocess(self, args):
        try:
            # We use creationflags=subprocess.CREATE_NO_WINDOW on Windows to hide the console window
            creationflags = 0
            if os.name == 'nt':
                creationflags = subprocess.CREATE_NO_WINDOW
                
            self.process = subprocess.Popen(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                creationflags=creationflags,
                encoding='utf-8',
                errors='replace'
            )

            for line in iter(self.process.stdout.readline, ''):
                if line:
                    self.after(0, self.append_log, line.strip())

            self.process.stdout.close()
            return_code = self.process.wait()
            
            if return_code == 0:
                self.after(0, self.append_log, "Download completed successfully.")
                self.after(0, lambda: messagebox.showinfo("Success", "Download completed successfully."))
            else:
                self.after(0, self.append_log, f"Process finished with exit code {return_code}.")
                self.after(0, lambda: messagebox.showerror("Error", f"Download failed with code {return_code}."))
                
        except Exception as e:
            self.after(0, self.append_log, f"Error: {str(e)}")
            self.after(0, lambda: messagebox.showerror("Error", f"An error occurred: {str(e)}"))
        finally:
            self.after(0, self.reset_button)

    def reset_button(self):
        self.download_button.configure(state="normal", text="Download")

    def show_about(self):
        messagebox.showinfo("About", "Naik's Audiobook Downloader v1.0\n\nContact: poornanandnaik24@gmail.com")

    def show_supported_sites(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Supported Sites")
        popup.geometry("400x350")
        # Ensure the popup is on top
        popup.attributes("-topmost", True)
        popup.focus()
        
        label = ctk.CTkLabel(popup, text="Supported Services:", font=ctk.CTkFont(size=16, weight="bold"))
        label.pack(pady=(10, 5))
        
        scroll_frame = ctk.CTkScrollableFrame(popup)
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        sites = [
            "audiobooks.com (Cookies)",
            "Blinkist (Cookies)",
            "Chirp (Cookies)",
            "eReolen (Cookies & Login)",
            "Everand / Scribd (Cookies)",
            "Librivox (No auth required)",
            "Nextory (Login)",
            "Overdrive (Cookies)",
            "Podimo (Login)",
            "Saxo (Login)",
            "Storytel / Mofibo (Login)",
            "YourCloudLibrary (Cookies & Login)"
        ]
        
        for site in sites:
            site_label = ctk.CTkLabel(scroll_frame, text=f"• {site}", font=ctk.CTkFont(size=13))
            site_label.pack(anchor="w", pady=2, padx=10)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = App()
    app.mainloop()
