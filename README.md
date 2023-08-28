# ScreenResolutionSwitcher
### 关于
一个Windows任务栏工具，可以一键切换要设置的分辨率、刷新率（hz）、屏幕自定义缩放（DPI），

适合一台电脑要频繁切换多种显示设备的场景

比如我的Nuc11平时是连65寸电视（支持120hz刷新）当HTPC用，大屏影音

> 1080P 150DPI 120Hz搭配飞鼠遥控是我比较满意的体验

等到剪视频码代码的时候就要换到27寸的显示器（只支持60hz），

> 这时候会切到：2K 100DPI 60Hz


![screenshots](https://github.com/SelfEnough/ScreenResolutionSwitcher/assets/36906472/7d1922be-a73c-4b7a-ae5a-5ad68ee47865)


可以增加自己常用的配置选项，在main.py中对应位置，增加
```
MenuItem("Set 1600x1200 50Hz 150DPI", self.set_custom_settings),
```
并增加对应的函数：
```
def set_custom_settings(self):
```

结合以下两个项目修改而来：

https://github.com/aarontbarratt/resolution-changer

https://github.com/imniko/SetDPI

# 使用方法

```
# 先安装依赖
pip install -r requirements.txt
然后运行
pythonw main.py
```
