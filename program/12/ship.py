# 创建ship类,包含方法__init__()、管理飞船位置的方法update()，
# 以及在屏幕上绘制飞船的方法blitme()。
import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		""" 初始化飞船并设置其初始位置 """
		self.screen = screen
		self.ai_settings =ai_settings
		
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# 在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)  # 因为ship_speed_factor存在小数，
		                                        # 故需要将self.center变成float
		# 移动标志
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		""" 根据移动标志调整飞船的位置 """
		# 更新飞船的center值，而不是rect（矩形左上角为原点，右下角为最大点）
		if self.moving_right and self.rect.right < self.screen_rect.right: 
		# self.rect.right返回飞船外接矩形的右边缘的x坐标，如果这个值小于self.screen_rect.right，
		# 就说明飞船未触及屏幕右边缘
			self.center +=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
		# 与右边类似，如果rect的左边缘的x坐标大于零，说明飞船未触及屏幕左边缘
			self.center -=self.ai_settings.ship_speed_factor
		
		# 根据self.center更新rect对象
		self.rect.centerx = self.center  ## self.rect.centerx只存储self.center的整数部分，但对显示
	                                     ## 飞船而言，这问题不大
	def blitme(self):
		""" 在指定位置绘制飞船 """
		self.screen.blit(self.image,self.rect)