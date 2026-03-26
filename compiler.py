"""C# compiler utilities: template, CSC discovery, and compilation."""

import os
import subprocess

CS_TEMPLATE = r"""using System;
using System.IO;
using System.Diagnostics;
using System.Windows.Forms;
using System.Reflection;

[assembly: AssemblyCompany("Created By Legendnoobe")]
[assembly: AssemblyCopyright("Created By Legendnoobe")]
[assembly: AssemblyDescription("Legendnoobe \"{TARGET_EXE}\" Launcher")]
[assembly: AssemblyProduct("Legendnoobe \"{TARGET_EXE}\" Launcher")]
[assembly: AssemblyTitle("Legendnoobe \"{TARGET_EXE}\" Launcher")]
[assembly: AssemblyFileVersion("1.0.0.0")]

namespace ExeLauncher
{
    class Program
    {
        [STAThread]
        static void Main()
        {
            string targetExe = "{TARGET_EXE}";
            string baseDir = AppDomain.CurrentDomain.BaseDirectory;

            try
            {
                string foundPath = SearchFile(baseDir, targetExe);
                if (foundPath != null)
                {
                    ProcessStartInfo psi = new ProcessStartInfo();
                    psi.FileName = foundPath;
                    psi.WorkingDirectory = Path.GetDirectoryName(foundPath);
                    psi.UseShellExecute = true;
                    Process.Start(psi);
                }
                else
                {
                    MessageBox.Show("'" + targetExe + "' was not found in this folder or subfolders.\nPlease make sure you are in the correct folder.", "Launcher Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occurred in the launcher:\n" + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        static string SearchFile(string directory, string fileName)
        {
            try
            {
                string filePath = Path.Combine(directory, fileName);
                if (File.Exists(filePath))
                    return filePath;

                foreach (string dir in Directory.GetDirectories(directory))
                {
                    string result = SearchFile(dir, fileName);
                    if (result != null)
                        return result;
                }
            }
            catch (UnauthorizedAccessException) { }
            catch (Exception) { }
            return null;
        }
    }
}
"""

# Possible paths where csc.exe may be found on Windows
_CSC_SEARCH_PATHS = [
    r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe",
    r"C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe",
]


def find_csc() -> str | None:
    """Find the C# compiler (csc.exe) on the system.

    Returns the path to csc.exe if found, otherwise None.
    """
    for path in _CSC_SEARCH_PATHS:
        if os.path.exists(path):
            return path
    return None


def compile_launcher(target_exe: str, output_exe: str, icon_path: str = None) -> tuple[bool, str]:
    """Compile a C# launcher EXE targeting the given executable.

    Args:
        target_exe: Name of the target EXE to launch.
        output_exe: Path for the output launcher EXE.
        icon_path: Optional path to a .ico file to embed.

    Returns:
        A tuple of (success: bool, message: str).
    """
    csc_path = find_csc()
    if not csc_path:
        return False, "CSC_NOT_FOUND"

    cs_code = CS_TEMPLATE.replace("{TARGET_EXE}", target_exe)
    cs_file = "launcher_temp.cs"

    try:
        with open(cs_file, "w", encoding="utf-8-sig") as f:
            f.write(cs_code)

        cmd = [csc_path, "/nologo", "/target:winexe", f"/out:{output_exe}"]

        if icon_path and os.path.exists(icon_path):
            cmd.append(f"/win32icon:{icon_path}")

        cmd.append("-reference:System.Windows.Forms.dll")
        cmd.append(cs_file)

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            errors="replace",
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        if result.returncode == 0:
            return True, os.path.abspath(output_exe)
        else:
            error_msg = result.stdout.strip() if result.stdout else ""
            return False, error_msg
    finally:
        if os.path.exists(cs_file):
            try:
                os.remove(cs_file)
            except OSError:
                pass
