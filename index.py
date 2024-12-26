import pygame 

pygame.init()

screen=pygame.display.set_mode((640,400))
clock=pygame.time.Clock()
count=0

#player characteristics
player_surface=pygame.image.load("C:\Projects\Python\AsteroidEscape\Graphics\png\character\walk\walk0001.png").convert_alpha()
player_rect=player_surface.get_rect(midbottom=(100,310))

player_gravity=0

#Enemy Chaarcteristics
slime_surface=pygame.image.load("C:\Projects\Python\AsteroidEscape\Graphics\png\enemies\slime_walk.png").convert_alpha()
slime_pos_x=450
slime_pos_y=310
slime_rect=slime_surface.get_rect(midbottom=(slime_pos_x,slime_pos_y))


#Surface Characteristics
background_surface=pygame.image.load("C:\Projects\Python\AsteroidEscape\Graphics\Background.jpg").convert_alpha()
background_surface=pygame.transform.scale(background_surface,(640,400))

text_font=pygame.font.Font("C:\Projects\Python\AsteroidEscape\Fonts\joystix.otf", 60)
score_font=pygame.font.Font("C:\Projects\Python\AsteroidEscape\Fonts\joystix.otf", 20)


ground_surface=pygame.image.load("C:\Projects\Python\AsteroidEscape\Graphics\ground.jpg").convert_alpha()
ground_surface=pygame.transform.scale(ground_surface,(640,132))
ground_surface_rect=ground_surface.get_rect(midbottom=(320,440))


#Game Restart Surfaces
player_end_surface=pygame.image.load("C:\Projects\Python\AsteroidEscape\Graphics\png\character\Front.png").convert_alpha()
player_end_surface=pygame.transform.rotozoom(player_end_surface,0,1.2)
player_end_rect=player_end_surface.get_rect(center=(320,200))

name_font=pygame.font.Font("C:\Projects\Python\AsteroidEscape\Fonts\joystix.otf", 20)
name_surface=name_font.render("Asteroid Escape",False, "#9ED8DB")
name_surface_rect=name_surface.get_rect(center=(320,115))

restart_surface=name_font.render("Press SPACE to restart", False, (255,255,255))
restart_surface_rect=restart_surface.get_rect(center=(320,330))



running=True
game_active=True

def display_score():
    text_surface=text_font.render(f'{count}', False, (255,255,255))
    text_rect=text_surface.get_rect(center=(320,200))
    screen.blit(text_surface, text_rect)



while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
      
        if event.type==pygame.KEYDOWN:
            if game_active:
                if event.key==pygame.K_SPACE and player_rect.y==215:
                    player_gravity=-20
            else:
                 if event.key==pygame.K_SPACE:
                    count=0
                    slime_pos_x=450
                    game_active=True

    
                
    if game_active:
        slime_pos_x-=4
        slime_rect.midbottom=(slime_pos_x,slime_pos_y)

        if slime_rect.left < -10:
            slime_pos_x=screen.get_width()

        player_gravity+=1
        player_rect.y+=player_gravity

        if player_rect.y>=215:
            player_rect.y=215

        if player_rect.y<215:
            player_surface=pygame.image.load("C:\Projects\Python\AsteroidEscape\Graphics\png\character\jump.png").convert_alpha()
        else:
            player_surface=pygame.image.load("C:\Projects\Python\AsteroidEscape\Graphics\png\character\walk\walk0001.png").convert_alpha()


        screen.blit(background_surface, (0,0))
        screen.blit(ground_surface, ground_surface_rect)
        screen.blit(player_surface, player_rect)
        screen.blit(slime_surface, slime_rect)

        if player_rect.left>=slime_rect.right :
            count+=1
            print(count)

        display_score()

        if player_rect.colliderect(slime_rect):
            game_active=False
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