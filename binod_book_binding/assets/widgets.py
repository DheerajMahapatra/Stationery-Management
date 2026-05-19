"""
assets/widgets.py
Reusable styled Tkinter widgets for Binod Book Binding.
"""

import tkinter as tk
from tkinter import ttk
from assets.theme import get as T, FONTS


# ── Flat Button ────────────────────────────────────────────────────────────────
class FlatButton(tk.Button):
    def __init__(self, master, text="", color=None, hover=None,
                 fg=None, icon="", **kwargs):
        t = T()
        bg = color or t["accent"]
        hov = hover or t["hover"]
        fgc = fg or t["btn_fg"]
        super().__init__(
            master,
            text=f"{icon}  {text}" if icon else text,
            bg=bg, fg=fgc,
            activebackground=hov, activeforeground=fgc,
            relief="flat", bd=0, cursor="hand2",
            padx=14, pady=7,
            font=FONTS["btn"],
            **kwargs,
        )
        self._bg = bg
        self._hov = hov
        self.bind("<Enter>", lambda e: self.config(bg=hov))
        self.bind("<Leave>", lambda e: self.config(bg=bg))


class DangerButton(FlatButton):
    def __init__(self, master, text="", icon="🗑️", **kwargs):
        t = T()
        super().__init__(master, text=text, icon=icon,
                         color=t["danger"], hover="#b71c1c", **kwargs)


class SuccessButton(FlatButton):
    def __init__(self, master, text="", icon="✅", **kwargs):
        t = T()
        super().__init__(master, text=text, icon=icon,
                         color=t["accent3"], hover="#1b5e20", **kwargs)


# ── Labeled Entry ──────────────────────────────────────────────────────────────
class LabeledEntry(tk.Frame):
    def __init__(self, master, label="", width=25, show="", **kwargs):
        t = T()
        super().__init__(master, bg=t["card"], **kwargs)
        tk.Label(self, text=label, bg=t["card"], fg=t["text2"],
                 font=FONTS["small"]).pack(anchor="w")
        self.var = tk.StringVar()
        self.entry = tk.Entry(
            self, textvariable=self.var,
            width=width, show=show,
            bg=t["entry_bg"], fg=t["entry_fg"],
            insertbackground=t["entry_fg"],
            relief="flat", bd=0,
            font=FONTS["body"],
            highlightthickness=1,
            highlightbackground=t["border"],
            highlightcolor=t["accent"],
        )
        self.entry.pack(fill="x", pady=2)

    def get(self): return self.var.get().strip()
    def set(self, v): self.var.set(v)
    def clear(self): self.var.set("")


# ── Labeled ComboBox ───────────────────────────────────────────────────────────
class LabeledCombo(tk.Frame):
    def __init__(self, master, label="", values=None, width=23, **kwargs):
        t = T()
        super().__init__(master, bg=t["card"], **kwargs)
        tk.Label(self, text=label, bg=t["card"], fg=t["text2"],
                 font=FONTS["small"]).pack(anchor="w")
        self.var = tk.StringVar()
        self.combo = ttk.Combobox(self, textvariable=self.var,
                                  values=values or [], width=width,
                                  font=FONTS["body"])
        self.combo.pack(fill="x", pady=2)

    def get(self): return self.var.get().strip()
    def set(self, v): self.var.set(v)
    def clear(self): self.var.set("")


# ── Stat Card ─────────────────────────────────────────────────────────────────
class StatCard(tk.Frame):
    def __init__(self, master, icon="", label="", value="", color=None, **kwargs):
        t = T()
        c = color or t["accent"]
        super().__init__(master, bg=t["card"], pady=16, padx=20,
                         highlightthickness=2, highlightbackground=c, **kwargs)
        tk.Label(self, text=icon, bg=t["card"], fg=c,
                 font=("Segoe UI", 22)).pack(anchor="w")
        self.val_label = tk.Label(self, text=value, bg=t["card"], fg=c,
                                   font=FONTS["stat"])
        self.val_label.pack(anchor="w")
        tk.Label(self, text=label, bg=t["card"], fg=t["text2"],
                 font=FONTS["stat_lbl"]).pack(anchor="w")

    def update_value(self, v):
        self.val_label.config(text=str(v))


# ── Styled Treeview ────────────────────────────────────────────────────────────
def make_treeview(master, columns: list, height=15) -> ttk.Treeview:
    """
    Create a styled Treeview with scrollbars.
    columns: list of (col_id, heading, width) tuples
    Returns the Treeview widget (already packed inside master).
    """
    t = T()

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Custom.Treeview",
                    background=t["tree_bg"],
                    foreground=t["text"],
                    rowheight=28,
                    fieldbackground=t["tree_bg"],
                    bordercolor=t["border"],
                    lightcolor=t["border"],
                    darkcolor=t["border"],
                    font=FONTS["body"])
    style.configure("Custom.Treeview.Heading",
                    background=t["header_bg"],
                    foreground=t["accent"],
                    font=FONTS["subhead"],
                    relief="flat")
    style.map("Custom.Treeview",
              background=[("selected", t["select"])],
              foreground=[("selected", "#ffffff")])

    frame = tk.Frame(master, bg=t["bg"])
    frame.pack(fill="both", expand=True)

    col_ids = [c[0] for c in columns]
    tree = ttk.Treeview(frame, columns=col_ids, show="headings",
                        height=height, style="Custom.Treeview",
                        selectmode="browse")

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    tree.pack(side="left", fill="both", expand=True)

    for col_id, heading, width in columns:
        tree.heading(col_id, text=heading,
                     command=lambda c=col_id: _sort_tree(tree, c, False))
        tree.column(col_id, width=width, anchor="center", minwidth=40)

    tree.tag_configure("alt", background=t["tree_alt"])

    return tree


def populate_tree(tree: ttk.Treeview, rows: list, keys: list):
    """Clear and repopulate a treeview. keys maps to dict keys in rows."""
    tree.delete(*tree.get_children())
    for i, row in enumerate(rows):
        vals = [row.get(k, "") for k in keys]
        tag = "alt" if i % 2 == 1 else ""
        tree.insert("", "end", values=vals, tags=(tag,))


def _sort_tree(tree, col, reverse):
    data = [(tree.set(k, col), k) for k in tree.get_children("")]
    try:
        data.sort(key=lambda x: float(x[0]), reverse=reverse)
    except ValueError:
        data.sort(reverse=reverse)
    for i, (_, k) in enumerate(data):
        tree.move(k, "", i)
    tree.heading(col, command=lambda: _sort_tree(tree, col, not reverse))


# ── Section Header ─────────────────────────────────────────────────────────────
def section_header(master, title: str, subtitle: str = ""):
    t = T()
    f = tk.Frame(master, bg=t["bg"])
    f.pack(fill="x", padx=24, pady=(20, 4))
    tk.Label(f, text=title, bg=t["bg"], fg=t["text"],
             font=FONTS["heading"]).pack(side="left")
    if subtitle:
        tk.Label(f, text=f"  {subtitle}", bg=t["bg"], fg=t["text2"],
                 font=FONTS["small"]).pack(side="left", padx=4)
    tk.Frame(master, bg=t["border"], height=1).pack(fill="x", padx=24, pady=(0, 12))


# ── Toast notification ─────────────────────────────────────────────────────────
class Toast:
    def __init__(self, root, message: str, kind: str = "info", duration: int = 3000):
        t = T()
        color = {"info": t["accent"], "success": t["accent3"],
                 "error": t["danger"], "warn": t["warn"]}.get(kind, t["accent"])

        self.win = tk.Toplevel(root)
        self.win.overrideredirect(True)
        self.win.attributes("-topmost", True)
        self.win.configure(bg=color)

        tk.Label(self.win, text=message, bg=color, fg="#ffffff",
                 font=FONTS["body"], padx=20, pady=10).pack()

        # Position bottom-right of root
        root.update_idletasks()
        rw, rh = root.winfo_width(), root.winfo_height()
        rx, ry = root.winfo_x(), root.winfo_y()
        self.win.update_idletasks()
        w = self.win.winfo_width()
        x = rx + rw - w - 24
        y = ry + rh - 70
        self.win.geometry(f"+{x}+{y}")

        root.after(duration, self.win.destroy)
