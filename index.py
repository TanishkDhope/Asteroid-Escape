import pygame 
from random import randint

pygame.init()

def read_high_score():
    try:
        with open('highScore.txt', 'r') as file:
            score=file.read().strip()
            return int(score)
    except (FileNotFoundError, ValueError):
        return 0
    return 0

pygame.display.set_caption("Asteroid Escape")
screen=pygame.display.set_mode((640,400))
clock=pygame.time.Clock()
count=0
high_score=read_high_score()

#player characteristics
player_walk1=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0001.png").convert_alpha()
player_walk2=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0002.png").convert_alpha()
player_walk3=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0003.png").convert_alpha()
player_walk4=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0004.png").convert_alpha()
player_walk5=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0005.png").convert_alpha()
player_walk6=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0006.png").convert_alpha()
player_walk7=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0007.png").convert_alpha()
player_walk8=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0008.png").convert_alpha()
player_walk9=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0009.png").convert_alpha()
player_walk10=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0010.png").convert_alpha()
player_walk11=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\walk\walk0011.png").convert_alpha()
player_index=0
player_walk=[player_walk1,player_walk2,player_walk3,player_walk4,player_walk5,player_walk6,player_walk7,player_walk8,player_walk9,player_walk10]
player_surf=player_walk[player_index]
player_rect=player_surf.get_rect(midbottom=(100,310))
player_jump=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\jump.png").convert_alpha()
player_gravity=0

#Enemy Chaarcteristics
slime_index=0
fly_index=0
slime_frame1=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\enemies\slime_walk.png").convert_alpha()
slime_frame2=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\enemies\slime_normal.png").convert_alpha()
slime_frame=[slime_frame1,slime_frame2]
slime_surf=slime_frame[slime_index]
fly_frame1=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\enemies\Fly_normal.png").convert_alpha()
fly_frame2=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\enemies\Fly_fly.png").convert_alpha()
fly_frame=[fly_frame1,fly_frame2]
fly_surf=fly_frame[fly_index]

obstacle_list=[]

#Non-Enemy Objects
grass_surf_1=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\grass.png").convert_alpha()
grass_surf_1=pygame.transform.scale(grass_surf_1, (25,30))
grass_surf_2=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\Bush.png").convert_alpha()
# grass_surf_2=pygame.transform.scale(grass_surf_2, (50,13))

cloud_surf_1=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\cloud_1.png").convert_alpha()
cloud_surf_1=pygame.transform.scale(cloud_surf_1, (63,33))
cloud_surf_2=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\cloud_2.png").convert_alpha()
cloud_surf_2=pygame.transform.scale(cloud_surf_2, (63,33))
cloud_surf_3=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\cloud_3.png").convert_alpha()
cloud_surf_3=pygame.transform.scale(cloud_surf_3, (63,33))

cloud_list=[]
grass_list=[]

#Surface Characteristics
background_surface=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Background.jpg").convert_alpha()
background_surface=pygame.transform.scale(background_surface,(640,400))

text_font=pygame.font.Font("C:\Projects\Python\Asteroid-Escape\Fonts\joystix.otf", 60)
score_font=pygame.font.Font("C:\Projects\Python\Asteroid-Escape\Fonts\joystix.otf", 20)

ground_surface=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\ground.jpg").convert_alpha()
ground_surface=pygame.transform.scale(ground_surface,(640,132))
ground_surface_rect=ground_surface.get_rect(midbottom=(320,440))




#Menu Surfaces
menu_font=pygame.font.Font("C:\Projects\Python\Asteroid-Escape\Fonts\joystix.otf", 20)
title_font=pygame.font.Font("C:\Projects\Python\Asteroid-Escape\Fonts\debug.otf", 70)

title_surf=title_font.render("Asteroid Escape", False, (255,255,255))
title_surf_rect=title_surf.get_rect(center=(320,80))

start_surface=menu_font.render("Start Game", False, (255,255,255))
start_surf_rect=start_surface.get_rect(center=(320,150))

high_surf=menu_font.render("High Scores", False, (255,255,255))
high_surf_rect=high_surf.get_rect(center=(320,190))

settings_surf=menu_font.render("Settings", False, (255,255,255))
settings_surf_rect=settings_surf.get_rect(center=(320,230))

quit_surf=menu_font.render("Quit", False, (255,255,255))
quit_surf_rect=quit_surf.get_rect(center=(320,270))

coming_soon=title_font.render("Comming Soon", False, (255,255,255))
coming_soon_rect=coming_soon.get_rect(center=(320,200))

menu_player=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\jump.png").convert_alpha()
menu_player=pygame.transform.rotozoom(menu_player, 45, 1)
menu_player_rect=menu_player.get_rect(center=(100,250))

move_x=0
move_y=0

menu_sound=pygame.mixer.Sound("C:\Projects\Python\Asteroid-Escape\Audio\Menu.wav")
menu_sound.set_volume(1)

def menu_player_animation(move_x, move_y):
    x_pos=menu_player_rect.x
    y_pos=menu_player_rect.y

    if x_pos==0:
            move_x=1   #move to the right
    elif x_pos==560:
            move_x=0   #move to the left
    
    if y_pos==0:
            move_y=1    #move down
    elif y_pos==300:
            move_y=0    #move up

    if move_y:
        menu_player_rect.y+=1
    else:
        menu_player_rect.y-=1
    
    if move_x:
        menu_player_rect.x+=1
    else:
        menu_player_rect.x-=1
    return move_x,move_y

    
    
#Game Restart Surfaces
player_end_surface=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\Front.png").convert_alpha()
player_end_surface=pygame.transform.rotozoom(player_end_surface,0,1.2)
player_end_rect=player_end_surface.get_rect(center=(320,200))

name_font=pygame.font.Font("C:\Projects\Python\Asteroid-Escape\Fonts\debug.otf", 50)
name_surface=name_font.render("Asteroid Escape",False, "#9ED8DB")
name_surface_rect=name_surface.get_rect(center=(320,100))

restart_surface=menu_font.render("Press SPACE to restart", False, (255,255,255))
restart_surface_rect=restart_surface.get_rect(center=(320,310))



#Confetti
confetti_1=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti1.png").convert_alpha()
confetti_2=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti2.png").convert_alpha()
confetti_3=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti3.png").convert_alpha()
confetti_4=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti4.png").convert_alpha()
confetti_5=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti5.png").convert_alpha()
confetti_6=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti6.png").convert_alpha()
confetti_7=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti7.png").convert_alpha()
confetti_8=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti8.png").convert_alpha()
confetti_9=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti9.png").convert_alpha()
confetti_10=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti10.png").convert_alpha()
confetti_11=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Confetti11.png").convert_alpha()
confetti_frame=[confetti_1, confetti_2, confetti_3, confetti_4,confetti_5,confetti_6,confetti_7, confetti_8, confetti_9,confetti_10,confetti_11]
confetti_index=0
confetti_surface=confetti_frame[confetti_index]
confetti_surf_rect=confetti_surface.get_rect(center=(320,280))
high_score_sound=pygame.mixer.Sound("C:\Projects\Python\Asteroid-Escape\Audio\High_score.mp3")


def confetti_animation():
    global confetti_index, confetti_surface, confetti_frame
    if confetti_index>=len(confetti_frame)-1:
        confetti_index=0

    confetti_index+=0.1
    confetti_surface=confetti_frame[int(confetti_index)]


#Audio
jump_sound=pygame.mixer.Sound("C:\Projects\Python\Asteroid-Escape\Audio\Jump.wav")
jump_sound.set_volume(0.1)

death_sound=pygame.mixer.Sound("C:\Projects\Python\Asteroid-Escape\Audio\Retro_die_03.OGG")
death_sound.set_volume(0.1)

bg_sound=pygame.mixer.Sound("C:\Projects\Python\Asteroid-Escape\Audio\Bg_music_test1.mp3")
bg_sound.set_volume(0.1)
bg_sound.play(loops=-1)



#Timer
obstacle_timer=pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)          #two args (event_to_trigger, How often in miliseconds)

slime_animation_timer=pygame.USEREVENT+ 2
pygame.time.set_timer(slime_animation_timer, 500)

fly_animation_timer=pygame.USEREVENT+ 3
pygame.time.set_timer(fly_animation_timer, 200)

cloud_timer=pygame.USEREVENT + 4
pygame.time.set_timer(cloud_timer, 3000)

grass_timer=pygame.USEREVENT + 5
pygame.time.set_timer(grass_timer, 2500)

running=True
game_state="menu"
game_pause=False
alternate=True

#display score logic
def display_score():
    text_surface=text_font.render(f'{count}', False, (255,255,255))
    text_rect=text_surface.get_rect(center=(320,200))
    screen.blit(text_surface, text_rect)

#display High Score
def display_high():
    global high_score
    if count>=high_score:
        high_score=count
    high_score_surf=score_font.render(f'HI {high_score}', False, (255,255,255))
    high_score_rect=high_score_surf.get_rect(center=(60,30))
    screen.blit(high_score_surf, high_score_rect)
    

#obstacle logic
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if not game_pause:
                obstacle_rect.x-=4.2
            if obstacle_rect.bottom==310:
                screen.blit(slime_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
                

        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-10]

        return obstacle_list
    else:
        return []

#cloud movement
def cloud_movement(cloud_list):
    if cloud_list:
        for cloud in cloud_list:
            if not game_pause:
                cloud.x-=1.8
            if cloud.bottom==40:
                screen.blit(cloud_surf_1, cloud)
            elif cloud.bottom==50:
                screen.blit(cloud_surf_2, cloud)
            else:
                screen.blit(cloud_surf_2, cloud)
                

        cloud_list=[cloud for cloud in cloud_list if cloud.right>-10]
        return cloud_list
    else:
        return []


#grass movement
def grass_movement(grass_list):
    if grass_list:
        for grass in grass_list:
            if not game_pause:
                grass[1].x-=2
            if grass[0]==0:
                screen.blit(grass_surf_1, grass[1])
            else:
                screen.blit(grass_surf_2, grass[1])

        grass_list=[grass for grass in grass_list if grass[1].right>-10]
        return grass_list
    else:
        return []

#collision logic
def check_collision(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player_rect.colliderect(obstacle_rect):
                obstacle_list=[]
                death_sound.play()
                return "end",obstacle_list
    return "active",obstacle_list


def calc_score(obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            if player_rect.left>obstacle.x and game_state=="active" and not game_pause:
                return 1
    return 0 

def player_animation():
    #play walking if on floor
    #display jump when player not on floor
    global player_surf,player_index
    if player_rect.bottom<215:
        player_surf=player_jump
    else:
        player_index+=0.35
        if player_index>=len(player_walk):
            player_index=0
        player_surf=player_walk[int(player_index)]
        

def save_high_score():
    with open('highScore.txt','w') as file:
        file.write(str(high_score))



while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
      
        if event.type==pygame.KEYDOWN:
            if game_state=="active":
                if event.key==pygame.K_SPACE and player_rect.y==215:
                    player_gravity=-20
                    jump_sound.play()
                elif event.key==pygame.K_p:
                    game_pause=not game_pause
                    print(f"Pause: {game_pause}")
            else:
                if event.key==pygame.K_SPACE:
                    count=0
                    game_state="active"
                elif event.key==pygame.K_ESCAPE:
                    game_state="menu"

        if game_state=="active" and not game_pause:
            if event.type==obstacle_timer:
                if randint(0,2):
                    obstacle_list.append(slime_surf.get_rect(midbottom=(randint(900,1100),310)))    
                else:
                    obstacle_list.append(fly_surf.get_rect(center=(randint(900,1100),randint(150,200))))

            if event.type==cloud_timer:
                rand=randint(0,3)
                if rand==0:
                    cloud_list.append(cloud_surf_1.get_rect(midbottom=(randint(600,800),40)))   
                elif rand==1:
                    cloud_list.append(cloud_surf_2.get_rect(midbottom=(randint(600,800),50))) 
                else:
                    cloud_list.append(cloud_surf_3.get_rect(midbottom=(randint(600,800),80))) 

            if event.type==grass_timer:
                if randint(0,2):
                    grass_list.append([0,grass_surf_1.get_rect(midbottom=(randint(800,1000),310))])   
                else:
                    grass_list.append([1,grass_surf_2.get_rect(midbottom=(randint(800,1000),310))]) 
 
    

            if event.type==slime_animation_timer:
                if slime_index==0: slime_index=1
                else: slime_index=0
                slime_surf=slime_frame[slime_index]
            
            if event.type==fly_animation_timer:
                if fly_index==0: fly_index=1
                else: fly_index=0
                fly_surf=fly_frame[fly_index]
                
    
    #game_screen
    if game_state=="active":

        player_gravity+=1
        player_rect.y+=player_gravity

        if player_rect.y>=215:
            player_rect.y=215

        player_animation()



        screen.blit(background_surface, (0,0))
        cloud_list=cloud_movement(cloud_list)
        grass_list=grass_movement(grass_list)

        screen.blit(ground_surface, ground_surface_rect)
        screen.blit(player_surf, player_rect)
        obstacle_list=obstacle_movement(obstacle_list)
  
        count+=calc_score(obstacle_list)

        game_state,obstacle_list=check_collision(obstacle_list)
        display_score()
        display_high()
    
    #Start Menu
    elif game_state=="menu":

        fly_surf=pygame.transform.scale(fly_surf, (50,25))
        fly_surf_rect=fly_surf.get_rect(center=(380,130))
        slime_surf_rect=slime_surf.get_rect(center=(200,305))

        screen.blit(background_surface, (0,0))
        screen.blit(slime_surf, slime_surf_rect)
        screen.blit(fly_surf, fly_surf_rect)
        screen.blit(menu_player, menu_player_rect)
        screen.blit(title_surf,title_surf_rect)
        screen.blit(start_surface, start_surf_rect)
        screen.blit(high_surf, high_surf_rect)
        screen.blit(settings_surf, settings_surf_rect)
        screen.blit(quit_surf, quit_surf_rect)


        move_x,move_y=menu_player_animation(move_x, move_y)

        mouse_pos=pygame.mouse.get_pos()
        if start_surf_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            if pygame.mouse.get_pressed()[0]:   
                game_state="active"
                menu_sound.play()
        elif quit_surf_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            if pygame.mouse.get_pressed()[0]:  
                running=False
                
        elif high_surf_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            if pygame.mouse.get_pressed()[0]:  
                menu_sound.play() 
                game_state="high"
        elif settings_surf_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            if pygame.mouse.get_pressed()[0]:  
                menu_sound.play() 
                game_state="setting"
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)


    #High Score screen
    elif game_state=="high":
        screen.fill("grey")
        screen.blit(coming_soon, coming_soon_rect)


    elif game_state=="setting":
        screen.fill("grey")
        screen.blit(coming_soon, coming_soon_rect)

    #end/restart screen
    elif game_state=="end":
        screen.fill("#467599")
        screen.blit(name_surface, name_surface_rect)
        screen.blit(restart_surface, restart_surface_rect)
        screen.blit(player_end_surface, player_end_rect)
        if(count>=high_score):
            name_surface=name_font.render("New High Score",False, "#9ED8DB")
            name_surface_rect=name_surface.get_rect(center=(320,100))
            screen.blit(confetti_surface,confetti_surf_rect)
            confetti_animation()
        text_surface=score_font.render(f'Score {count}', False, (255,255,255))
        text_rect=text_surface.get_rect(center=(530,30))
        high_score_surf=score_font.render(f'HI {high_score}', False, (255,255,255))
        high_score_rect=high_score_surf.get_rect(center=(100,30))
        screen.blit(high_score_surf, high_score_rect)
        screen.blit(text_surface, text_rect)
        save_high_score()

   

        
    pygame.display.update()
    clock.tick(60)    

pygame.quit()