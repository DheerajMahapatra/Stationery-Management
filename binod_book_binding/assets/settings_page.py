
"""
Settings page — theme, profile credential overrides, database backup.
Integrated with visibility toggle controls and structural username parameters.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
import os
import sqlite3
from datetime import datetime
from assets import theme as theme_module
from assets.theme import get as T, FONTS, set_theme
from assets.widgets import FlatButton, LabeledEntry, section_header, Toast
from database.db_setup import get_connection, hash_password, DB_PATH


class SettingsPage(tk.Frame):
    def __init__(self, master, root_ref=None, on_theme_change=None, **kwargs):
        t = T()
        super().__init__(master, bg=t["bg"], **kwargs)
        self.root_ref = root_ref
        self.on_theme_change = on_theme_change
        
        # State tracking trackers for visibility states
        self.old_pw_visible = False
        self.new_pw_visible = False
        self.confirm_pw_visible = False
        
        self._build()

    def _build(self):
        t = T()
        section_header(self, "⚙️ Settings")

        content = tk.Frame(self, bg=t["bg"])
        content.pack(fill="both", expand=True, padx=24)

        # ── Change Username & Password ──────────────────────────────────────────
        card2 = tk.Frame(content, bg=t["card"], padx=24, pady=20)
        card2.pack(fill="x", pady=8)
        tk.Label(card2, text="🔐 Update Profile Credentials", bg=t["card"], fg=t["accent"],
                 font=FONTS["subhead"]).pack(anchor="w", pady=(0,10))

        # 1. Current Password Entry Row
        old_pw_frame = tk.Frame(card2, bg=t["card"])
        old_pw_frame.pack(anchor="w", pady=4)
        self.old_pw = LabeledEntry(old_pw_frame, label="Current Password", show="●", width=30)
        self.old_pw.pack(side="left", anchor="w")
        
        self.old_toggle_btn = tk.Button(
            old_pw_frame, text="👁", font=("Segoe UI", 10), bg=t["card"], fg=t["text2"],
            relief="flat", activebackground=t["card"], cursor="hand2", bd=0,
            command=self._toggle_old_password
        )
        # Fixed: changed align="bottom" to anchor="s"
        self.old_toggle_btn.pack(side="left", padx=6, anchor="s", pady=(20, 0))

        # Divider line
        tk.Frame(card2, height=1, bg=t["bg"], width=300).pack(anchor="w", pady=10)

        # 2. Target New Username Row
        self.new_username = LabeledEntry(card2, label="New Username", width=30)
        self.new_username.pack(anchor="w", pady=4)

        # 3. Target New Password Row
        new_pw_frame = tk.Frame(card2, bg=t["card"])
        new_pw_frame.pack(anchor="w", pady=4)
        self.new_pw = LabeledEntry(new_pw_frame, label="New Password", show="●", width=30)
        self.new_pw.pack(side="left", anchor="w")
        
        self.new_toggle_btn = tk.Button(
            new_pw_frame, text="👁", font=("Segoe UI", 10), bg=t["card"], fg=t["text2"],
            relief="flat", activebackground=t["card"], cursor="hand2", bd=0,
            command=self._toggle_new_password
        )
        # Fixed: changed align="bottom" to anchor="s"
        self.new_toggle_btn.pack(side="left", padx=6, anchor="s", pady=(20, 0))

        # 4. Confirm Target New Password Row
        confirm_frame = tk.Frame(card2, bg=t["card"])
        confirm_frame.pack(anchor="w", pady=4)
        self.new_pw2 = LabeledEntry(confirm_frame, label="Confirm New Password", show="●", width=30)
        self.new_pw2.pack(side="left", anchor="w")
        
        self.confirm_toggle_btn = tk.Button(
            confirm_frame, text="👁", font=("Segoe UI", 10), bg=t["card"], fg=t["text2"],
            relief="flat", activebackground=t["card"], cursor="hand2", bd=0,
            command=self._toggle_confirm_password
        )
        # Fixed: changed align="bottom" to anchor="s"
        self.confirm_toggle_btn.pack(side="left", padx=6, anchor="s", pady=(20, 0))

        self.pw_err = tk.Label(card2, text="", bg=t["card"], fg=t["danger"], font=FONTS["small"])
        self.pw_err.pack(anchor="w", pady=2)
        
        FlatButton(card2, text="Update Account Settings", icon="🔑",
                    command=self._change_credentials).pack(anchor="w", pady=8)

        # ── Database Backup ────────────────────────────────────────────────────
        card3 = tk.Frame(content, bg=t["card"], padx=24, pady=20)
        card3.pack(fill="x", pady=8)
        tk.Label(card3, text="💾 Database Backup", bg=t["card"], fg=t["accent"],
                 font=FONTS["subhead"]).pack(anchor="w", pady=(0,10))
        tk.Label(card3, text=f"Current DB: {DB_PATH}", bg=t["card"], fg=t["text2"],
                 font=FONTS["small"], wraplength=500, anchor="w").pack(anchor="w")
        FlatButton(card3, text="Backup Database", icon="💾",
                    command=self._backup).pack(anchor="w", pady=8)

        # ── About ──────────────────────────────────────────────────────────────
        card4 = tk.Frame(content, bg=t["card"], padx=24, pady=20)
        card4.pack(fill="x", pady=8)
        tk.Label(card4, text="ℹ️ About", bg=t["card"], fg=t["accent"],
                 font=FONTS["subhead"]).pack(anchor="w", pady=(0,6))
        about = (
            "Binod Book Binding — Stock Management & Billing Software\n"
            "Version 1.0  |  Built with Python + Tkinter + SQLite\n"
            "Offline, fully local. No internet required."
        )
        tk.Label(card4, text=about, bg=t["card"], fg=t["text2"],
                 font=FONTS["body"], justify="left").pack(anchor="w")

    # =========================================================
    # VISIBILITY PASSWORDS TOGGLE UTILITIES
    # =========================================================
    def _toggle_old_password(self):
        self.old_pw_visible = not self.old_pw_visible
        char = "" if self.old_pw_visible else "●"
        icon = "🙈" if self.old_pw_visible else "👁"
        self.old_pw.entry.config(show=char)
        self.old_toggle_btn.config(text=icon)

    def _toggle_new_password(self):
        self.new_pw_visible = not self.new_pw_visible
        char = "" if self.new_pw_visible else "●"
        icon = "🙈" if self.new_pw_visible else "👁"
        self.new_pw.entry.config(show=char)
        self.new_toggle_btn.config(text=icon)

    def _toggle_confirm_password(self):
        self.confirm_pw_visible = not self.confirm_pw_visible
        char = "" if self.confirm_pw_visible else "●"
        icon = "🙈" if self.confirm_pw_visible else "👁"
        self.new_pw2.entry.config(show=char)
        self.confirm_toggle_btn.config(text=icon)

    # =========================================================
    # TRANSACTION SECURE EXECUTION CONTROLLERS
    # =========================================================
    def _change_credentials(self):
        old_password_input = self.old_pw.get()
        new_username_input = self.new_username.get().strip()
        new_password_input = self.new_pw.get()
        confirm_password_input = self.new_pw2.get()

        # Validation Checkpoints
        if not old_password_input or not new_username_input or not new_password_input or not confirm_password_input:
            self.pw_err.config(text="⚠  All fields are explicitly required.")
            return
        if new_password_input != confirm_password_input:
            self.pw_err.config(text="⚠  New passwords do not match.")
            return
        if len(new_password_input) < 6:
            self.pw_err.config(text="⚠  New password parameters must be at least 6 characters.")
            return

        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            # Lookup validating match on stored parameters matching active user role mappings
            cursor.execute(
                "SELECT user_id, username FROM users WHERE role='admin' AND password=? LIMIT 1",
                (hash_password(old_password_input),)
            )
            admin_record = cursor.fetchone()
            
            if not admin_record:
                self.pw_err.config(text="❌  Current password parameter validation failed.")
                return

            admin_user_id = admin_record["user_id"]

            # Prevent collisions if new username exists under another account profile instance
            cursor.execute(
                "SELECT user_id FROM users WHERE username=? AND user_id != ?", 
                (new_username_input, admin_user_id)
            )
            if cursor.fetchone():
                self.pw_err.config(text="❌  Target username parameter is already taken.")
                return

            # Atomically update profile database records
            cursor.execute(
                "UPDATE users SET username=?, password=? WHERE user_id=?",
                (new_username_input, hash_password(new_password_input), admin_user_id)
            )
            conn.commit()

            # UI Cleanup reflection reset fields
            self.pw_err.config(text="")
            for widget in (self.old_pw, self.new_username, self.new_pw, self.new_pw2):
                widget.clear()

            # Revert UI mask visuals back to standard secure defaults
            self.old_pw_visible = False
            self.new_pw_visible = False
            self.confirm_pw_visible = False
            self.old_pw.entry.config(show="●")
            self.new_pw.entry.config(show="●")
            self.new_pw2.entry.config(show="●")
            self.old_toggle_btn.config(text="👁")
            self.new_toggle_btn.config(text="👁")
            self.confirm_toggle_btn.config(text="👁")

            Toast(self.root_ref or self, "Credentials changed successfully!", "success")

        except Exception as database_err:
            messagebox.showerror("System Database Error", f"Unable to modify fields: {database_err}")
        finally:
            if conn:
                conn.close()

    def _backup(self):
        dest = filedialog.askdirectory(title="Select Backup Folder")
        if not dest:
            return
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = f"binod_backup_{ts}.db"
        dst  = os.path.join(dest, name)
        try:
            shutil.copy2(DB_PATH, dst)
            messagebox.showinfo("Backup", f"Database backed up to:\n{dst}")
        except Exception as e:
            messagebox.showerror("Backup Failed", str(e))

    def refresh(self):
        pass