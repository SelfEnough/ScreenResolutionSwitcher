# ScreenResolutionSwitcher
一个Windows任务栏工具，可以一键切换要设置的分辨率、刷新率（hz）、屏幕自定义缩放（DPI）

![screenshots](https://github.com/SelfEnough/ScreenResolutionSwitcher/assets/36906472/7d1922be-a73c-4b7a-ae5a-5ad68ee47865)


可以增加自己常用的配置选项，在main.py中对应位置，增加
MenuItem("Set 1600x1200 50Hz 150DPI", self.set_custom_settings),
并增加对应的函数：def set_custom_settings(self):

结合以下两个项目修改而来：
https://github.com/aarontbarratt/resolution-changer
https://github.com/imniko/SetDPI
