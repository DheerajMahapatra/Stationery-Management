"""
Settings page — theme, password, database backup.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import shutil, os
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
        self._build()

    def _build(self):
        t = T()
        section_header(self, "⚙️ Settings")

        content = tk.Frame(self, bg=t["bg"])
        content.pack(fill="both", expand=True, padx=24)

        # # ── Appearance ─────────────────────────────────────────────────────────
        # card1 = tk.Frame(content, bg=t["card"], padx=24, pady=20)
        # card1.pack(fill="x", pady=8)
        # tk.Label(card1, text="🎨 Appearance", bg=t["card"], fg=t["accent"],
        #          font=FONTS["subhead"]).pack(anchor="w", pady=(0,10))

        # mode_row = tk.Frame(card1, bg=t["card"])
        # mode_row.pack(anchor="w")
        # tk.Label(mode_row, text="Theme Mode:", bg=t["card"], fg=t["text"],
        #          font=FONTS["body"]).pack(side="left", padx=(0,12))

        # self.mode_var = tk.StringVar(value=t["mode"])
        # for mode, label in [("dark", "🌙 Dark"), ("light", "☀️ Light")]:
        #     tk.Radiobutton(
        #         mode_row, text=label, variable=self.mode_var, value=mode,
        #         bg=t["card"], fg=t["text"], selectcolor=t["card2"],
        #         activebackground=t["card"], font=FONTS["body"],
        #         command=self._apply_theme
        #     ).pack(side="left", padx=8)

        # ── Change Password ────────────────────────────────────────────────────
        card2 = tk.Frame(content, bg=t["card"], padx=24, pady=20)
        card2.pack(fill="x", pady=8)
        tk.Label(card2, text="🔐 Change Password", bg=t["card"], fg=t["accent"],
                 font=FONTS["subhead"]).pack(anchor="w", pady=(0,10))

        self.old_pw  = LabeledEntry(card2, label="Current Password", show="●", width=30)
        self.old_pw.pack(anchor="w", pady=4)
        self.new_pw  = LabeledEntry(card2, label="New Password", show="●", width=30)
        self.new_pw.pack(anchor="w", pady=4)
        self.new_pw2 = LabeledEntry(card2, label="Confirm New Password", show="●", width=30)
        self.new_pw2.pack(anchor="w", pady=4)

        self.pw_err = tk.Label(card2, text="", bg=t["card"], fg=t["danger"],
                               font=FONTS["small"])
        self.pw_err.pack(anchor="w")
        FlatButton(card2, text="Update Password", icon="🔑",
                   command=self._change_password).pack(anchor="w", pady=8)

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

    def _apply_theme(self):
        set_theme(self.mode_var.get())
        if self.on_theme_change:
            self.on_theme_change()
        messagebox.showinfo("Theme", "Theme changed! Please restart the app for full effect.")

    def _change_password(self):
        old = self.old_pw.get()
        new = self.new_pw.get()
        c   = self.new_pw2.get()

        if not old or not new or not c:
            self.pw_err.config(text="⚠  All fields are required.")
            return
        if new != c:
            self.pw_err.config(text="⚠  New passwords do not match.")
            return
        if len(new) < 6:
            self.pw_err.config(text="⚠  Password must be at least 6 characters.")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE username='admin' AND password=?",
                       (hash_password(old),))
        if not cursor.fetchone():
            conn.close()
            self.pw_err.config(text="❌  Current password is incorrect.")
            return

        cursor.execute("UPDATE users SET password=? WHERE username='admin'",
                       (hash_password(new),))
        conn.commit()
        conn.close()

        self.pw_err.config(text="")
        for f in (self.old_pw, self.new_pw, self.new_pw2):
            f.clear()
        Toast(self.root_ref or self, "Password updated successfully!", "success")

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
