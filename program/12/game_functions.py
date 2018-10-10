# 函数check_events()检测相关的事件，如按键和松开，
# 并使用辅助函数check_keydown_events()和check_keyup_events()来处理这些事件，
# 函数update_screen()用于在每次执行主循环时都重绘屏幕
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ship,ai_settings,screen,bullets):
	""" 响应按键 """
	if event.key == pygame.K_RIGHT:  ## 右键按下，飞船一直向右移动
		ship.moving_right =True
	if event.key == pygame.K_LEFT:  ## 左键按下，飞船一直向左移动
		ship.moving_left =True
	elif event.key == pygame.K_SPACE:
		# 创建一个子弹，并将其加入到编组bullets中
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def check_keyup_events(event,ship):
	""" 响应松开 """
	if event.key == pygame.K_RIGHT:  ## 右键松掉，飞船停止右移
		ship.moving_right = False
	if event.key == pygame.K_LEFT:  ## 左键松掉，飞船停止左移
		ship.moving_left = False	

def check_events(ship,ai_settings,screen,bullets):
	""" 响应按键和鼠标事件 """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship,screen,ai_settings,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
	""" 更新屏幕上的图像，并切换到新屏幕 """
	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# 每次循环都重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()
		
	# 让最近绘制的屏幕可见
	pygame.display.flip()