import  pygame
import  random
import  copy

class RunGame():
    def __init__(self):
        pygame.init()
        screen=pygame.display.set_mode((1280,720))
        clock=pygame.time.Clock()
        running=True
        
        while running:
            screen.fill("purple")
            if  initial_deal:
                for i   in range(2):
                    my_hand,game_deck=deal_cards(my_hand,game_deck)
                    dealer_hand,game_deck=deal_cards(dealer_hand,game_deck)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
    
class   Game():
    def __init__(self):
        #blackjack configurations
        cards=['2', '3', '4', '5', '6', '7', '8', '9','10','J','Q','K','A']
        deck=4*cards
        decks=4
        pygame.display.set_caption('Blackjack!')
        fps=60
        smaller_font = pygame.font.Font('freesansbold.ttf', 36)
        active = False

        #win,loss,draw/push
        records = [0, 0, 0]
        player_score = 0
        dealer_score = 0
        initial_deal = False
        my_hand = []
        dealer_hand = []
        outcome = 0
        reveal_dealer = False
        hand_active = False
        outcome = 0
        add_score = False
        results = [
            '', 'PLAYER BUSTED!', 'Player WINS!',
            'DEALER WINS!', 'TIE GAME!'
            ]
    def deal_cards(current_hand, current_deck):
        card=random.randint(0,len(current_deck))
        current_hand.append(current_deck[card-1])
        current_deck.pop(card-1)
        return current_hand, current_deck
    
    def draw_scores(player,dealer):
        screen.blit(font.render(f'Score[{player}]',True,"white"),(350,400))
        if  reveal_dealer:
            screen.blit(font.render(f'Score[{dealer}]',True,"white"),(350,450))

    def draw_scores(player, dealer):
        screen.blit(font.render(f'Score[{player}]', True, 'white'), (350, 400))
        if reveal_dealer:
            screen.blit(font.render(f'Score[{dealer}]', True, 'white'), (350, 100))

    def calcule_score(hand):
        hand_score =0
        aces_count =hand.count("A")
        for i in range(len(hand)):
            for j   in range(8):
                if  hand[i]==cards[j]:
                    hand_score+=int(hand[j])
            if hand[i] in ['10', 'J', 'Q', 'K']:
                hand_score += 10
            elif hand[i] == 'A':
                hand_score += 11
        if hand_score > 21 and aces_count > 0:
            for i in range(aces_count):
                if hand_score > 21:
                    hand_score -= 10
        return hand_score

if __name__ == "__main__":
    game=RunGame()
    game.run()