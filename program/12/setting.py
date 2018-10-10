# 包含Settings类，这个类只包含方法__init__(),
# 它初始化控制游戏外观和飞船速度的属性
class Setting():
	""" 存储《外星人入侵》的所有设置的类 """
	
	def __init__(self):
		""" 初始化游戏的设置 """
		# 屏幕设置
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230,230,230)
		
		# 飞船的速度
		self.ship_speed_factor = 1.5
		
		# 子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60