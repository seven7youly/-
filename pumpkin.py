while True:
	#回到原点
	while get_pos_x()>0 or get_pos_y()>0:
		if get_pos_y()>0:
			move(North)
		if get_pos_x()>0:
			move(East)
	#收集并种南瓜
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type()==Grounds.Grassland:
				till()
			else:
				pass
			harvest()
			plant(Entities.Pumpkin)
			move(North)
		move(East)
	#检查南瓜成熟情况并作记录
	not_ready=[] #创建序列储存烂南瓜的位置
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if not can_harvest():
				x,y=get_pos_x(),get_pos_y()
				not_ready.append((x,y))
				harvest()
				plant(Entities.Pumpkin)
			move(North)
		move(East)
	#检查位置最近的烂南瓜
		#not_ready第一个运算为起始数据
	while len(not_ready)>0:
		x,y=not_ready[0]
		step_x=min(get_world_size()-abs(get_pos_x()-x)+1,abs(get_pos_x()-x))
		step_y=min(get_world_size()-abs(get_pos_y()-y)+1,abs(get_pos_y()-y))
		step=step_x+step_y
		pumpkin_x=x
		pumpkin_y=y
		#烂南瓜的位置
		for item in not_ready:
			x,y=item
			step_x=min(get_world_size()-abs(get_pos_x()-x),abs(get_pos_x()-x))
			step_y=min(get_world_size()-abs(get_pos_y()-y),abs(get_pos_y()-y))
			step_move=step_x+step_y
			#获得最短的移动距离
			if step_move<=step:
				step=step_move
				step_move_x=step_x
				step_move_y=step_y
				pumpkin_x=x
				pumpkin_y=y
			else:
				pass
		#移向最近的烂南瓜
		#x方向移动
		if step_move_x==abs(get_pos_x()-pumpkin_x):#直接移动
			if get_pos_x()>pumpkin_x:
				for i in range(get_pos_x()-pumpkin_x):
					move(West)
			else:
				for i in range(pumpkin_x-get_pos_x()):
					move(East)
		else:#(循环移动)
			if get_pos_x()>pumpkin_x:
				for i in range(pumpkin_x+get_world_size()-get_pos_x()+1):
					move(East)
			else:
				for i in range(get_pos_x()+get_world_size()-pumpkin_x+1):
					move(West)
		#y方向移动
		if step_move_y==abs(get_pos_y()-pumpkin_y):#直接移动
			if get_pos_y()>pumpkin_y:
				for i in range(get_pos_y()-pumpkin_y):
					move(South)
			else:
				for i in range(pumpkin_y-get_pos_y()):
					move(North)
		else:#(循环移动)
			if get_pos_y()>pumpkin_y:
				for i in range(pumpkin_y+get_world_size()-get_pos_y()+1):
					move(North)
			else:
				for i in range(get_pos_y()+get_world_size()-pumpkin_y):
					move(South)
		#检查位置是否正确
		if  (get_pos_x()==pumpkin_x and get_pos_y()==pumpkin_y):
			#检查再次播种的情况，可以收割的化从烂南瓜列表删除，不能收割重新播种
			if not can_harvest():
				harvest()
				plant(Entities.Pumpkin)
				use_item(Items.Water)
				use_item(Items.Fertilizer)
			else:#删除
				not_ready.remove((pumpkin_x,pumpkin_y))
			pass
