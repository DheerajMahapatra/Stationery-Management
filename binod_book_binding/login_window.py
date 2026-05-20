# """
# Ultra Professional Login UI
# Binod Book Binding Management System
# """

# import tkinter as tk
# from tkinter import messagebox
# from assets.theme import get as T, FONTS
# from assets.widgets import FlatButton, LabeledEntry
# from database.db_setup import get_connection, hash_password


# class LoginWindow(tk.Tk):

#     def __init__(self):
#         super().__init__()

#         self.title("Binod Book Binding — Professional Login")
#         self.resizable(False, False)

#         self._center(950, 580)

#         self.logged_in = False
#         self.show_password = False

#         self._build_ui()

#     # ================= CENTER WINDOW =================
#     def _center(self, w, h):
#         self.update_idletasks()

#         sw = self.winfo_screenwidth()
#         sh = self.winfo_screenheight()

#         x = (sw - w) // 2
#         y = (sh - h) // 2

#         self.geometry(f"{w}x{h}+{x}+{y}")

#     # ================= MAIN UI =================
#     def _build_ui(self):

#         t = T()

#         self.configure(bg=t["bg"])

#         # MAIN CONTAINER
#         container = tk.Frame(self, bg=t["bg"])
#         container.pack(fill="both", expand=True)

#         # ================= LEFT PANEL =================
#         left = tk.Frame(container, bg="#111827", width=450)
#         left.pack(side="left", fill="both")

#         left.pack_propagate(False)

#         # Logo
#         tk.Label(
#             left,
#             text="📚",
#             bg="#111827",
#             fg="white",
#             font=("Segoe UI Emoji", 60)
#         ).pack(pady=(70, 10))

#         tk.Label(
#             left,
#             text="Binod Book Binding",
#             bg="#111827",
#             fg="white",
#             font=("Segoe UI", 24, "bold")
#         ).pack()

#         tk.Label(
#             left,
#             text="Stationery Shop Management System",
#             bg="#111827",
#             fg="#9CA3AF",
#             font=("Segoe UI", 12)
#         ).pack(pady=(5, 30))

#         # Description
#         desc = """
# Manage Products, Billing, Customers,
# Sales Reports, Inventory & Stock
# with a beautiful modern interface.
#         """

#         tk.Label(
#             left,
#             text=desc,
#             justify="center",
#             bg="#111827",
#             fg="#D1D5DB",
#             font=("Segoe UI", 13),
#             wraplength=320
#         ).pack(pady=20)

#         # Bottom text
#         tk.Label(
#             left,
#             text="© 2026 Binod Book Binding",
#             bg="#111827",
#             fg="#6B7280",
#             font=("Segoe UI", 10)
#         ).pack(side="bottom", pady=20)

#         # ================= RIGHT PANEL =================
#         right = tk.Frame(container, bg="#F9FAFB")
#         right.pack(side="right", fill="both", expand=True)

#         # Login Card
#         card = tk.Frame(
#             right,
#             bg="white",
#             bd=0,
#             highlightthickness=1,
#             highlightbackground="#E5E7EB"
#         )

#         card.place(relx=0.5, rely=0.5, anchor="center",
#                    width=380, height=420)

#         # Welcome text
#         tk.Label(
#             card,
#             text="Welcome Back 👋",
#             bg="white",
#             fg="#111827",
#             font=("Segoe UI", 22, "bold")
#         ).pack(pady=(35, 5))

#         tk.Label(
#             card,
#             text="Login to continue",
#             bg="white",
#             fg="#6B7280",
#             font=("Segoe UI", 11)
#         ).pack(pady=(0, 25))

#         # Username
#         tk.Label(
#             card,
#             text="Username",
#             bg="white",
#             fg="#374151",
#             font=("Segoe UI", 10, "bold")
#         ).pack(anchor="w", padx=40)

#         self.user_entry = tk.Entry(
#             card,
#             font=("Segoe UI", 11),
#             bg="#F3F4F6",
#             relief="flat"
#         )

#         self.user_entry.pack(
#             fill="x",
#             padx=40,
#             pady=(5, 18),
#             ipady=10
#         )

#         self.user_entry.insert(0, "admin")

#         # Password
#         tk.Label(
#             card,
#             text="Password",
#             bg="white",
#             fg="#374151",
#             font=("Segoe UI", 10, "bold")
#         ).pack(anchor="w", padx=40)

#         password_frame = tk.Frame(card, bg="white")
#         password_frame.pack(fill="x", padx=40, pady=(5, 5))

#         self.pass_entry = tk.Entry(
#             password_frame,
#             font=("Segoe UI", 11),
#             bg="#F3F4F6",
#             relief="flat",
#             show="●"
#         )

#         self.pass_entry.pack(
#             side="left",
#             fill="x",
#             expand=True,
#             ipady=10
#         )

#         self.pass_entry.insert(0, "chandan@123")

#         # Show Button
#         self.show_btn = tk.Button(
#             password_frame,
#             text="👁",
#             bg="#2563EB",
#             fg="white",
#             relief="flat",
#             cursor="hand2",
#             command=self.toggle_password
#         )

#         self.show_btn.pack(side="right", padx=(5, 0))

#         # Error label
#         self.err_label = tk.Label(
#             card,
#             text="",
#             bg="white",
#             fg="#DC2626",
#             font=("Segoe UI", 10)
#         )

#         self.err_label.pack(anchor="w", padx=40, pady=5)

#         # Login button
#         login_btn = tk.Button(
#             card,
#             text="LOGIN",
#             bg="#2563EB",
#             fg="white",
#             activebackground="#1D4ED8",
#             activeforeground="white",
#             relief="flat",
#             cursor="hand2",
#             font=("Segoe UI", 12, "bold"),
#             command=self._login
#         )

#         login_btn.pack(
#             fill="x",
#             padx=40,
#             pady=(20, 15),
#             ipady=10
#         )

#         # Hover effect
#         login_btn.bind(
#             "<Enter>",
#             lambda e: login_btn.config(bg="#1D4ED8")
#         )

#         login_btn.bind(
#             "<Leave>",
#             lambda e: login_btn.config(bg="#2563EB")
#         )

#         # Default credentials
#         tk.Label(
#             card,
#             text="Default Login: admin / admin123",
#             bg="white",
#             fg="#6B7280",
#             font=("Segoe UI", 9)
#         ).pack()

#         # ENTER KEY
#         self.bind("<Return>", lambda e: self._login())

#     # ================= SHOW PASSWORD =================
#     def toggle_password(self):

#         self.show_password = not self.show_password

#         if self.show_password:
#             self.pass_entry.config(show="")
#         else:
#             self.pass_entry.config(show="●")

#     # ================= LOGIN =================
#     def _login(self):

#         username = self.user_entry.get().strip()
#         password = self.pass_entry.get().strip()

#         if not username or not password:
#             self.err_label.config(
#                 text="⚠ Please enter username and password"
#             )
#             return

#         try:
#             conn = get_connection()
#             cursor = conn.cursor()

#             cursor.execute(
#                 "SELECT * FROM users WHERE username=? AND password=?",
#                 (username, hash_password(password))
#             )

#             user = cursor.fetchone()

#             conn.close()

#             if user:

#                 self.logged_in = True

#                 messagebox.showinfo(
#                     "Success",
#                     f"Welcome {username}!"
#                 )

#                 self.destroy()

#             else:
#                 self.err_label.config(
#                     text="❌ Invalid username or password"
#                 )

#         except Exception as e:

#             messagebox.showerror(
#                 "Database Error",
#                 str(e)
#             )


# if __name__ == "__main__":
#     app = LoginWindow()
#     app.mainloop()














"""
Ultra Professional Login UI
Binod Book Binding Management System
"""

import tkinter as tk
from tkinter import messagebox
from assets.theme import get as T, FONTS
from assets.widgets import FlatButton, LabeledEntry
from database.db_setup import get_connection, hash_password


class LoginWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Binod Book Binding — Professional Login")
        self.resizable(False, False)

        self._center(950, 580)

        self.logged_in = False
        self.show_password = False

        self._build_ui()

    # ================= CENTER WINDOW =================
    def _center(self, w, h):
        self.update_idletasks()

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w) // 2
        y = (sh - h) // 2

        self.geometry(f"{w}x{h}+{x}+{y}")

    # ================= MAIN UI =================
    def _build_ui(self):

        t = T()

        self.configure(bg=t["bg"])

        # MAIN CONTAINER
        container = tk.Frame(self, bg=t["bg"])
        container.pack(fill="both", expand=True)

        # ================= LEFT PANEL =================
        left = tk.Frame(container, bg="#111827", width=450)
        left.pack(side="left", fill="both")

        left.pack_propagate(False)

        # Logo
        tk.Label(
            left,
            text="📚",
            bg="#111827",
            fg="white",
            font=("Segoe UI Emoji", 60)
        ).pack(pady=(70, 10))

        tk.Label(
            left,
            text="Binod Book Binding",
            bg="#111827",
            fg="white",
            font=("Segoe UI", 24, "bold")
        ).pack()

        tk.Label(
            left,
            text="Stationery Shop Management System",
            bg="#111827",
            fg="#9CA3AF",
            font=("Segoe UI", 12)
        ).pack(pady=(5, 30))

        # Description
        desc = """
Manage Products, Billing, Customers,
Sales Reports, Inventory & Stock
with a beautiful modern interface.
        """

        tk.Label(
            left,
            text=desc,
            justify="center",
            bg="#111827",
            fg="#D1D5DB",
            font=("Segoe UI", 13),
            wraplength=320
        ).pack(pady=20)

        # Bottom text
        tk.Label(
            left,
            text="© 2026 Binod Book Binding",
            bg="#111827",
            fg="#6B7280",
            font=("Segoe UI", 10)
        ).pack(side="bottom", pady=20)

        # ================= RIGHT PANEL =================
        right = tk.Frame(container, bg="#F9FAFB")
        right.pack(side="right", fill="both", expand=True)

        # Login Card
        card = tk.Frame(
            right,
            bg="white",
            bd=0,
            highlightthickness=1,
            highlightbackground="#E5E7EB"
        )

        card.place(relx=0.5, rely=0.5, anchor="center",
                   width=380, height=420)

        # Welcome text
        tk.Label(
            card,
            text="Welcome Back 👋",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=(35, 5))

        tk.Label(
            card,
            text="Login to continue",
            bg="white",
            fg="#6B7280",
            font=("Segoe UI", 11)
        ).pack(pady=(0, 25))

        # Username
        tk.Label(
            card,
            text="Username",
            bg="white",
            fg="#374151",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=40)

        self.user_entry = tk.Entry(
            card,
            font=("Segoe UI", 11),
            bg="#F3F4F6",
            relief="flat"
        )

        self.user_entry.pack(
            fill="x",
            padx=40,
            pady=(5, 18),
            ipady=10
        )

        # ❌ Removed auto‑fill: self.user_entry.insert(0, "admin")

        # Password
        tk.Label(
            card,
            text="Password",
            bg="white",
            fg="#374151",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=40)

        password_frame = tk.Frame(card, bg="white")
        password_frame.pack(fill="x", padx=40, pady=(5, 5))

        self.pass_entry = tk.Entry(
            password_frame,
            font=("Segoe UI", 11),
            bg="#F3F4F6",
            relief="flat",
            show="●"
        )

        self.pass_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=10
        )

        # ❌ Removed auto‑fill: self.pass_entry.insert(0, "chandan@123")

        # Show Button
        self.show_btn = tk.Button(
            password_frame,
            text="👁",
            bg="#2563EB",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.toggle_password
        )

        self.show_btn.pack(side="right", padx=(5, 0))

        # Error label
        self.err_label = tk.Label(
            card,
            text="",
            bg="white",
            fg="#DC2626",
            font=("Segoe UI", 10)
        )

        self.err_label.pack(anchor="w", padx=40, pady=5)

        # Login button
        login_btn = tk.Button(
            card,
            text="LOGIN",
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 12, "bold"),
            command=self._login
        )

        login_btn.pack(
            fill="x",
            padx=40,
            pady=(20, 15),
            ipady=10
        )

        # Hover effect
        login_btn.bind(
            "<Enter>",
            lambda e: login_btn.config(bg="#1D4ED8")
        )

        login_btn.bind(
            "<Leave>",
            lambda e: login_btn.config(bg="#2563EB")
        )

        # ✅ Updated default credentials hint
        tk.Label(
            card,
            text="Default Login: Chandan / Chandan@123",
            bg="white",
            fg="#6B7280",
            font=("Segoe UI", 9)
        ).pack()

        # ENTER KEY
        self.bind("<Return>", lambda e: self._login())

    # ================= SHOW PASSWORD =================
    def toggle_password(self):

        self.show_password = not self.show_password

        if self.show_password:
            self.pass_entry.config(show="")
        else:
            self.pass_entry.config(show="●")

    # ================= LOGIN =================
    def _login(self):

        username = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()

        if not username or not password:
            self.err_label.config(
                text="⚠ Please enter username and password"
            )
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, hash_password(password))
            )

            user = cursor.fetchone()

            conn.close()

            if user:

                self.logged_in = True

                messagebox.showinfo(
                    "Success",
                    f"Welcome {username}!"
                )

                self.destroy()

            else:
                self.err_label.config(
                    text="❌ Invalid username or password"
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()