import pygame 
from random import randint

pygame.init()

pygame.display.set_caption("Asteroid Escape")
screen=pygame.display.set_mode((640,400))
clock=pygame.time.Clock()
count=0

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

#Surface Characteristics
background_surface=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\Background.jpg").convert_alpha()
background_surface=pygame.transform.scale(background_surface,(640,400))

text_font=pygame.font.Font("C:\Projects\Python\Asteroid-Escape\Fonts\joystix.otf", 60)
score_font=pygame.font.Font("C:\Projects\Python\Asteroid-Escape\Fonts\joystix.otf", 20)


ground_surface=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\ground.jpg").convert_alpha()
ground_surface=pygame.transform.scale(ground_surface,(640,132))
ground_surface_rect=ground_surface.get_rect(midbottom=(320,440))


#Game Restart Surfaces
player_end_surface=pygame.image.load("C:\Projects\Python\Asteroid-Escape\Graphics\png\character\Front.png").convert_alpha()
player_end_surface=pygame.transform.rotozoom(player_end_surface,0,1.2)
player_end_rect=player_end_surface.get_rect(center=(320,200))

name_font=pygame.font.Font("C:\Projects\Python\Asteroid-Escape\Fonts\joystix.otf", 20)
name_surface=name_font.render("Asteroid Escape",False, "#9ED8DB")
name_surface_rect=name_surface.get_rect(center=(320,115))

restart_surface=name_font.render("Press SPACE to restart", False, (255,255,255))
restart_surface_rect=restart_surface.get_rect(center=(320,330))

#Timer
obstacle_timer=pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)          #two args (event_to_trigger, How often in miliseconds)

slime_animation_timer=pygame.USEREVENT+ 2
pygame.time.set_timer(slime_animation_timer, 500)


fly_animation_timer=pygame.USEREVENT+ 3
pygame.time.set_timer(fly_animation_timer, 200)

running=True
game_active=True
game_pause=False
alternate=True

#display score logic
def display_score():
    text_surface=text_font.render(f'{count}', False, (255,255,255))
    text_rect=text_surface.get_rect(center=(320,200))
    screen.blit(text_surface, text_rect)

#obstacle logic
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if not game_pause:
                obstacle_rect.x-=4
            if obstacle_rect.bottom==310:
                screen.blit(slime_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
                

        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-10]

        return obstacle_list
    else:
        return []


#collision logic
def check_collision(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player_rect.colliderect(obstacle_rect):
                obstacle_list=[]
                return False,obstacle_list
    return True,obstacle_list


def calc_score(obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            if player_rect.left>obstacle.x and game_active and not game_pause:
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



while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
      
        if event.type==pygame.KEYDOWN:
            if game_active:
                if event.key==pygame.K_SPACE and player_rect.y==215:
                    player_gravity=-20
                elif event.key==pygame.K_p:
                    game_pause=not game_pause
                    print(f"Pause: {game_pause}")
            else:
                if event.key==pygame.K_SPACE:
                    count=0
                    game_active=True

        
        if game_active and not game_pause:
            if event.type==obstacle_timer:
                if randint(0,2):
                    obstacle_list.append(slime_surf.get_rect(midbottom=(randint(900,1100),310)))    
                else:
                    obstacle_list.append(fly_surf.get_rect(center=(randint(900,1100),150)))

            if event.type==slime_animation_timer:
                if slime_index==0: slime_index=1
                else: slime_index=0
                slime_surf=slime_frame[slime_index]
            
            if event.type==fly_animation_timer:
                if fly_index==0: fly_index=1
                else: fly_index=0
                fly_surf=fly_frame[fly_index]
            

        
                
            

    
                
    if game_active:

        player_gravity+=1
        player_rect.y+=player_gravity

        if player_rect.y>=215:
            player_rect.y=215

        player_animation()



        screen.blit(background_surface, (0,0))
        screen.blit(ground_surface, ground_surface_rect)
        screen.blit(player_surf, player_rect)
        obstacle_list=obstacle_movement(obstacle_list)

        # if player_rect.left>=slime_rect.right :
        #     count+=1
        count+=calc_score(obstacle_list)

        game_active,obstacle_list=check_collision(obstacle_list)
        display_score()


    else:
        screen.fill("#467599")
        screen.blit(name_surface, name_surface_rect)
        screen.blit(restart_surface, restart_surface_rect)
        screen.blit(player_end_surface, player_end_rect)
        text_surface=score_font.render(f'Score: {count}', False, (255,255,255))
        text_rect=text_surface.get_rect(center=(530,30))
        screen.blit(text_surface, text_rect)

        
    pygame.display.update()
    clock.tick(60)    

pygame.quit()