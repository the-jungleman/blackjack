import  pygame
import  random
import  copy
    
class   Game():
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.font.init()
        screen=pygame.display.set_mode((1280,720))
        clock=pygame.time.Clock()
        running=True
        
        while running:
            screen.fill("purple")
            if  self.initial_deal:
                for i   in range(2):
                    self.my_hand,self.game_deck=self.deal_cards(self.my_hand,self.game_deck)
                    self.dealer_hand,self.game_deck=self.deal_cards(self.dealer_hand,self.game_deck)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
            self.smaller_font = pygame.font.SysFont('freesansbold.ttf', 36)


        #blackjack configurations
        self.cards=['2', '3', '4', '5', '6', '7', '8', '9','10','J','Q','K','A']
        self.deck=4*self.cards
        self.decks=4
        pygame.display.set_caption('Blackjack!')
        self.fps=60
        self.active = False

        # if pygame.get_init():
            # self.smaller_font = pygame.font.SysFont('freesansbold.ttf', 36)
        # else:
            # print("Pygame initialization failed")

        #win,loss,draw/push
        self.records = [0, 0, 0]
        self.player_score = 0
        self.dealer_score = 0
        self.initial_deal = False
        self.my_hand = []
        self.dealer_hand = []
        self.outcome = 0
        self.reveal_dealer = False
        self.hand_active = False
        self.outcome = 0
        self.add_score = False
        self.results = [
            '', 'PLAYER BUSTED!', 'Player WINS!',
            'DEALER WINS!', 'TIE GAME!'
            ]
    def deal_cards(current_hand, current_deck,self):
        self.card=random.randint(0,len(self.current_deck))
        self.current_hand.append(self.current_deck[self.card-1])
        self.current_deck.pop(self.card-1)
        return self.current_hand, self.current_deck
    
    def draw_scores(player,dealer,self):
        self.screen.blit(font.render(f'Score[{player}]',True,"white"),(350,400))
        if  self.reveal_dealer:
            self.screen.blit(font.render(f'Score[{dealer}]',True,"white"),(350,450))

    def draw_scores(player, dealer,self):
        screen.blit(font.render(f'Score[{player}]', True, 'white'), (350, 400))
        if self.reveal_dealer:
            screen.blit(font.render(f'Score[{dealer}]', True, 'white'), (350, 100))

    def calcule_score(hand,self):
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
    Game().run()