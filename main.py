from PIL import Image
from pystray import Icon, Menu, MenuItem
import subprocess
from resolution_manager import ResolutionManager


class ResolutionChanger:
    def __init__(self):
        self.res_manager = ResolutionManager()
        self.menu = (
            MenuItem(
                "Toggle Resolution",
                self.res_manager.toggle_resolution,
                default=True,
                visible=False,
            ),
            MenuItem("TV模式 1920x1080 120Hz 150DPI", self.set_custom_settings_1),
            MenuItem("2K模式 2560x1440 144Hz 200DPI", self.set_custom_settings_2),
            MenuItem(
                "3840x2560", lambda: self.res_manager.change_resolution(3840, 1080)
            ),
            MenuItem(
                "2560x1440", lambda: self.res_manager.change_resolution(2560, 1440)
            ),
            MenuItem(
                "1920x1080", lambda: self.res_manager.change_resolution(1920, 1080)
            ),
            MenuItem(
                "1600x1200", lambda: self.res_manager.change_resolution(1600, 1200)
            ),
            MenuItem("Custom Scaling",
                Menu(
                    MenuItem("100%", lambda: self.set_dpi(100)),
                    MenuItem("125%", lambda: self.set_dpi(125)),
                    MenuItem("150%", lambda: self.set_dpi(150)),
                    MenuItem("175%", lambda: self.set_dpi(175)),
                    MenuItem("200%", lambda: self.set_dpi(200)),
                ),
            ),
            MenuItem(
                "Refresh Rate",
                Menu(
                    MenuItem("144", lambda: self.res_manager.change_refresh_rate(144)),
                    MenuItem("120", lambda: self.res_manager.change_refresh_rate(120)),
                    MenuItem("100", lambda: self.res_manager.change_refresh_rate(100)),
                    MenuItem("60", lambda: self.res_manager.change_refresh_rate(60)),
                    MenuItem("50", lambda: self.res_manager.change_refresh_rate(50)),
                ),
            ),
            MenuItem("Quit", lambda: self.quit()),
        )


        self.icon_image = Image.open(r"img\icon_white.png")

        self.icon = Icon("Resolution Changer", self.icon_image, "ResChanger", self.menu)
        self.icon.run()

    def set_dpi(self, scaling_percentage: int):
        """
        Calls the SetDPI.exe tool with the specified scaling percentage.
        """
        try:
            subprocess.run(["SetDPI.exe", str(scaling_percentage)], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to set DPI to {scaling_percentage}%")
    def set_custom_settings_1(self):
        self.res_manager.change_resolution(1920, 1080)
        self.res_manager.change_refresh_rate(120)
        self.set_dpi(150)
    def set_custom_settings_2(self):
        self.res_manager.change_resolution(2560, 1440)
        self.res_manager.change_refresh_rate(144)
        self.set_dpi(200)
        
    def quit(self):
        """
        exits the application.
        """
        self.icon.stop()


if __name__ == "__main__":
    res_changer = ResolutionChanger
    res_changer()
