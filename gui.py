"""GUI module — the Tkinter application window and event handlers."""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

from localization import STRINGS
from icon_utils import extract_icon_from_exe, convert_image_to_ico
from compiler import compile_launcher


class ExeBuilderApp:
    """Main application window for the Exe Launcher Builder."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.lang = "en"
        self.root.geometry("520x420")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        self._build_ui()
        self._apply_title()

        # Show welcome dialog on startup
        self.root.after(100, self._show_welcome)

    # ── Localization helper ──────────────────────────────────────────

    def t(self, key: str) -> str:
        """Return the localized string for the given key."""
        return STRINGS[self.lang].get(key, key)

    # ── UI Construction ──────────────────────────────────────────────

    def _build_ui(self):
        """Build the entire UI layout."""
        self._build_lang_switcher()
        self._build_output_section()
        self._build_target_section()
        self._build_icon_section()
        self._build_pull_section()
        self._build_build_button()

    def _build_lang_switcher(self):
        lang_frame = tk.Frame(self.root)
        lang_frame.pack(fill=tk.X, padx=10, pady=(8, 0))

        # Info button on the left
        self.info_btn = tk.Button(
            lang_frame, text="ℹ️", font=("Arial", 12), bd=0,
            cursor="hand2", command=self._show_info,
        )
        self.info_btn.pack(side=tk.LEFT)

        lang_inner = tk.Frame(lang_frame)
        lang_inner.pack(side=tk.RIGHT)

        self.lang_label_widget = tk.Label(lang_inner, text=self.t("lang_label"), font=("Arial", 9))
        self.lang_label_widget.pack(side=tk.LEFT, padx=(0, 4))

        self.lang_var = tk.StringVar(value="English")
        self.lang_combo = ttk.Combobox(
            lang_inner, textvariable=self.lang_var,
            values=["English", "Türkçe"], state="readonly", width=10,
        )
        self.lang_combo.pack(side=tk.LEFT)
        self.lang_combo.bind("<<ComboboxSelected>>", self._on_lang_change)

    def _build_output_section(self):
        self.output_label = tk.Label(
            self.root, text=self.t("output_label"), font=("Arial", 10, "bold"),
        )
        self.output_label.pack(pady=(10, 5))

        self.output_exe_var = tk.StringVar(value=self.t("output_default"))
        self.output_entry = ttk.Entry(self.root, textvariable=self.output_exe_var, width=45)
        self.output_entry.pack()

    def _build_target_section(self):
        self.target_label = tk.Label(
            self.root, text=self.t("target_label"), font=("Arial", 10),
        )
        self.target_label.pack(pady=(15, 5))

        self.target_exe_var = tk.StringVar()
        self.target_entry = ttk.Entry(self.root, textvariable=self.target_exe_var, width=45)
        self.target_entry.pack()

    def _build_icon_section(self):
        self.icon_path_var = tk.StringVar(value="")

        icon_frame = tk.Frame(self.root)
        icon_frame.pack(pady=(15, 10))

        self.icon_btn = ttk.Button(
            icon_frame, text=self.t("select_icon_btn"), command=self._on_select_icon,
        )
        self.icon_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.icon_label = tk.Label(
            icon_frame, text=self.t("icon_default_text"),
            font=("Arial", 9, "italic"), fg="gray",
        )
        self.icon_label.pack(side=tk.LEFT)

        self.status_lbl = tk.Label(self.root, text="", font=("Arial", 8, "italic"), fg="blue")
        self.status_lbl.pack(pady=(2, 5))

    def _build_pull_section(self):
        self.pull_header_label = tk.Label(
            self.root, text=self.t("pull_header"),
            font=("Arial", 9, "italic", "bold"), fg="#e05a00",
        )
        self.pull_header_label.pack(pady=(10, 0))

        self.pull_btn = ttk.Button(
            self.root, text=self.t("pull_btn"), command=self._on_pull_from_exe,
        )
        self.pull_btn.pack(pady=(5, 5))

    def _build_build_button(self):
        self.build_btn = ttk.Button(
            self.root, text=self.t("build_btn"), command=self._on_build,
            style="Accent.TButton",
        )
        self.build_btn.pack(pady=15)

    # ── Language Switching ───────────────────────────────────────────

    def _on_lang_change(self, _event=None):
        selected = self.lang_var.get()
        self.lang = "tr" if selected == "Türkçe" else "en"
        self._refresh_ui()

    def _apply_title(self):
        self.root.title(self.t("window_title"))

    def _refresh_ui(self):
        """Update all widget texts to the current language."""
        self._apply_title()
        self.lang_label_widget.config(text=self.t("lang_label"))
        self.output_label.config(text=self.t("output_label"))
        self.target_label.config(text=self.t("target_label"))
        self.icon_btn.config(text=self.t("select_icon_btn"))
        self.pull_header_label.config(text=self.t("pull_header"))
        self.pull_btn.config(text=self.t("pull_btn"))
        self.build_btn.config(text=self.t("build_btn"))

        if not self.icon_path_var.get():
            self.icon_label.config(text=self.t("icon_default_text"))

    # ── Info / Welcome Dialogs ───────────────────────────────────────

    def _show_info(self):
        """Show an info dialog explaining what the app does."""
        messagebox.showinfo(self.t("info_title"), self.t("info_text"))

    def _show_welcome(self):
        """Show a welcome dialog on first startup."""
        messagebox.showinfo(self.t("welcome_title"), self.t("welcome_text"))

    # ── Event Handlers ───────────────────────────────────────────────

    def _on_pull_from_exe(self):
        """Pull icon and name from an existing .exe file."""
        filepath = filedialog.askopenfilename(
            title=self.t("pull_dialog_title"),
            filetypes=(
                (self.t("pull_filter_exe"), "*.exe"),
                (self.t("pull_filter_all"), "*.*"),
            ),
        )
        if not filepath:
            return

        base_name = os.path.basename(filepath)
        self.target_exe_var.set(base_name)
        self.output_exe_var.set(
            base_name.replace(".exe", "").replace(".EXE", "") + self.t("output_suffix")
        )

        self.status_lbl.config(text=self.t("pull_status_pulling"), fg="blue")
        self.root.update()

        output_dir = os.path.dirname(os.path.abspath(__file__))

        try:
            save_path = extract_icon_from_exe(filepath, output_dir)
            if save_path:
                self.icon_path_var.set(save_path)
                self.icon_label.config(
                    text=self.t("pulled_label").format(name=base_name[:15]), fg="green",
                )
                self.status_lbl.config(text=self.t("pull_status_success"), fg="green")
            else:
                self.status_lbl.config(text=self.t("pull_status_icon_fail"), fg="orange")
        except Exception as e:
            self.status_lbl.config(
                text=self.t("pull_status_error").format(error=str(e)), fg="red",
            )

    def _on_select_icon(self):
        """Open a file dialog to select an image and convert it to .ico."""
        filepath = filedialog.askopenfilename(
            title=self.t("select_icon_title"),
            filetypes=(
                (self.t("select_icon_filter"), "*.png;*.jpg;*.jpeg;*.bmp;*.webp;*.ico"),
                (self.t("pull_filter_all"), "*.*"),
            ),
        )
        if filepath:
            output_dir = os.path.dirname(os.path.abspath(__file__))
            try:
                save_path = convert_image_to_ico(filepath, output_dir)
                self.icon_path_var.set(save_path)
                self.icon_label.config(
                    text=self.t("icon_converted").format(name=os.path.basename(filepath)[:15]),
                    fg="green",
                )
                self.status_lbl.config(text=self.t("icon_converted_status"), fg="green")
            except Exception:
                self.icon_path_var.set(filepath)
                self.icon_label.config(text=os.path.basename(filepath), fg="green")
                self.status_lbl.config(text=self.t("icon_convert_warn"), fg="orange")
        else:
            self.icon_path_var.set("")
            self.icon_label.config(text=self.t("icon_default_text"), fg="gray")
            self.status_lbl.config(text="")

    def _on_build(self):
        """Compile the launcher EXE."""
        target_exe = self.target_exe_var.get().strip()
        output_exe = self.output_exe_var.get().strip()
        icon_path = self.icon_path_var.get().strip()

        if not target_exe:
            messagebox.showwarning(self.t("window_title"), self.t("warn_target_empty"))
            return

        if not output_exe:
            messagebox.showwarning(self.t("window_title"), self.t("warn_output_empty"))
            return

        if not output_exe.endswith(".exe"):
            output_exe += ".exe"

        # Remove existing output file if present
        if os.path.exists(output_exe):
            try:
                os.remove(output_exe)
            except Exception:
                messagebox.showerror(
                    self.t("window_title"),
                    self.t("error_file_locked").format(name=output_exe),
                )
                return

        success, message = compile_launcher(target_exe, output_exe, icon_path)

        if message == "CSC_NOT_FOUND":
            messagebox.showerror(self.t("window_title"), self.t("error_csc_missing"))
        elif success:
            messagebox.showinfo(
                self.t("window_title"), self.t("success_msg").format(path=message),
            )
        else:
            error_text = message if message else self.t("error_compile_unknown")
            messagebox.showerror(
                self.t("window_title"), self.t("error_compile").format(error=error_text),
            )
