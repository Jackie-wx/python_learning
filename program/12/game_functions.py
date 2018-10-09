import sys
import pygame

def check_keydown_events(event,ship):
	""" 响应按键 """
	if event.key == pygame.K_RIGHT:  ## 右键按下，飞船一直向右移动
		ship.moving_right =True
	if event.key == pygame.K_LEFT:  ## 左键按下，飞船一直向左移动
		ship.moving_left =True

def check_keyup_events(event,ship):
	""" 响应松开 """
	if event.key == pygame.K_RIGHT:  ## 右键松掉，飞船停止右移
		ship.moving_right = False
	if event.key == pygame.K_LEFT:  ## 左键松掉，飞船停止左移
		ship.moving_left = False	

def check_events(ship):
	""" 响应按键和鼠标事件 """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship):
	""" 更新屏幕上的图像，并切换到新屏幕 """
	# 每次循环都重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	
	# 让最近绘制的屏幕可见
	pygame.display.flip()