import copy
import random
import pygame

class CardGame:
    def __init__(self):
        # Variaveis importantes para o funcionamento da tela e do jogo.
        pygame.init()
        self.screen = pygame.display.set_mode([600, 900])
        pygame.display.set_caption('Blackjack!')
        self.fps = 60
        self.timer = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', 44)
        self.smaller_font = pygame.font.Font('freesansbold.ttf', 36)
        self.active = False
        self.records = [0, 0, 0]
        self.player_score = 0
        self.dealer_score = 0
        self.initial_deal = False
        self.my_hand = []
        self.dealer_hand = []
        self.outcome = 0
        self.reveal_dealer =     False
        self.hand_active = False
        self.add_score = False
        self.results = ['','Player WINS!', 'DEALER WINS', 'TIE GAME!']
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.one_deck = 4 * self.cards
        self.decks = 4
        self.game_deck = copy.deepcopy(self.decks * self.one_deck)
    
    # Distribuicao de cartas aleatorias
    def deal_cards(self, current_hand):
        card = random.randint(0, len(self.game_deck))
        current_hand.append(self.game_deck[card - 1])
        self.game_deck.pop(card - 1)
        return current_hand
    
    # Pontos design
    def draw_scores(self, player, dealer):
        self.screen.blit(self.font.render(f'Score[{player}]', True, 'white'), (350, 400))
        if self.reveal_dealer:
            self.screen.blit(self.font.render(f'Score[{dealer}]', True, 'white'), (350, 100))
    # Cartas design
    def draw_cards(self, player, dealer, reveal):
        for i in range(len(player)):
            pygame.draw.rect(self.screen, 'white', [70 + (70 * i), 460 + (5 * i), 120, 220], 0, 5)
            self.screen.blit(self.font.render(player[i], True, 'black'), (75 + 70 * i, 465 + 5 * i))
            self.screen.blit(self.font.render(player[i], True, 'black'), (75 + 70 * i, 635 + 5 * i))
            pygame.draw.rect(self.screen, 'red', [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)

        for i in range(len(dealer)):
            pygame.draw.rect(self.screen, 'white', [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
            if i!= 0 or reveal:
                self.screen.blit(self.font.render(dealer[i], True, 'black'), (75 + 70 * i, 165 + 5 * i))
                self.screen.blit(self.font.render(dealer[i], True, 'black'), (75 + 70 * i, 335 + 5 * i))
            else:
                self.screen.blit(self.font.render('???', True, 'black'), (75 + 70 * i, 165 + 5 * i))
                self.screen.blit(self.font.render('???', True, 'black'), (75 + 70 * i, 335 + 5 * i))
            pygame.draw.rect(self.screen, 'blue', [70 + (70 * i), 160 + (5 * i), 120, 220], 5, 5)

    # Calculo de pontos
    def calculate_score(self, hand):
        hand_score = 0
        aces_count = hand.count('A')
        for i in range(len(hand)):
            for j in range(8):
                if hand[i] == self.cards[j]:
                    hand_score += int(hand[i])
            if hand[i] in ['10', 'J', 'Q', 'K']:
                hand_score += 10
            elif hand[i] == 'A':
                hand_score += 11
        if hand_score > 21 and aces_count > 0:
            for i in range(aces_count):
                if hand_score > 21:
                    hand_score -= 10
        return hand_score
    
    # Desenho do jogo
    def draw_game(self, active, record, result):
        button_list = []
        if not active:
            deal = pygame.draw.rect(self.screen, 'white', [150, 20, 300, 100], 0, 5)
            pygame.draw.rect(self.screen, 'green', [150, 20, 300, 100], 3, 5)
            deal_text = self.font.render('DEAL HAND', True, 'black')
            self.screen.blit(deal_text, (165, 50))
            button_list.append(deal)
        else:
            hit = pygame.draw.rect(self.screen, 'white', [0, 700, 300, 100], 0, 5)
            pygame.draw.rect(self.screen, 'green', [0, 700, 300, 100], 3, 5)
            hit_text = self.font.render('HIT ME', True, 'black')
            self.screen.blit(hit_text, (55, 735))
            button_list.append(hit)
            stand = pygame.draw.rect(self.screen, 'white', [300, 700, 300, 100], 0, 5)
            pygame.draw.rect(self.screen, 'green', [300, 700, 300, 100], 3, 5)
            stand_text = self.font.render('STAND', True, 'black')
            self.screen.blit(stand_text, (355, 735))
            button_list.append(stand)
            score_text = self.smaller_font.render(f'Wins: {record[0]}   Losses: {record[1]}   Draws: {record[2]}', True, 'white')
            self.screen.blit(score_text, (15, 840))
        if result!= 0:
            self.screen.blit(self.font.render(self.results[result], True, 'white'), (15, 25))
            deal = pygame.draw.rect(self.screen, 'white', [150, 220, 300, 100], 0, 5)
            pygame.draw.rect(self.screen, 'green', [150, 220, 300, 100], 3, 5)
            pygame.draw.rect(self.screen, 'black', [153, 223, 294, 94], 3, 5)
            deal_text = self.font.render('NEW HAND', True, 'black')
            self.screen.blit(deal_text, (165, 250))
            button_list.append(deal)
        return button_list

    # Checagem de pontos de cartas
    def check_endgame(self, hand_act, deal_score, play_score, result, totals, add):
        if not hand_act and deal_score >= 17:
            if play_score > 21:
                result = 2
            elif deal_score < play_score <= 21 or deal_score > 21:
                result = 1
            elif play_score < deal_score <= 21:
                result = 2
            else:
                result = 3
            if add:
                if result == 1 or result == 3:
                    totals[0] += 1
                elif result == 2:
                    totals[1] += 1
                else:
                    totals[2] += 1
                add = False
        return result, totals, add

    # Funcionamento de distribuição de cartas, botoes e pontos
    def run(self):
        run = True
        while run:
            self.timer.tick(self.fps)
            self.screen.fill('black')
            if self.initial_deal:
                for i in range(2):
                    self.my_hand = self.deal_cards(self.my_hand)
                    self.dealer_hand = self.deal_cards(self.dealer_hand)
                self.initial_deal = False
            if self.active:
                self.player_score = self.calculate_score(self.my_hand)
                self.draw_cards(self.my_hand, self.dealer_hand, self.reveal_dealer)
                if self.reveal_dealer:
                    self.dealer_score = self.calculate_score(self.dealer_hand)
                    if self.dealer_score < 17:
                        self.dealer_hand = self.deal_cards(self.dealer_hand)
                self.draw_scores(self.player_score, self.dealer_score)
            buttons = self.draw_game(self.active, self.records, self.outcome)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if not self.active:
                        if buttons[0].collidepoint(event.pos):
                            self.active = True
                            self.initial_deal = True
                            self.game_deck = copy.deepcopy(self.decks * self.one_deck)
                            self.my_hand = []
                            self.dealer_hand = []
                            self.outcome = 0
                            self.hand_active = True
                            self.reveal_dealer = False
                            self.outcome = 0
                            self.add_score = True
                    else:
                        if buttons[0].collidepoint(event.pos) and self.player_score < 21 and self.hand_active:
                            self.my_hand = self.deal_cards(self.my_hand)
                        elif buttons[1].collidepoint(event.pos) and not self.reveal_dealer:
                            self.reveal_dealer = True
                            self.hand_active = False
                        elif len(buttons) == 3:
                            if buttons[2].collidepoint(event.pos):
                                self.active = True
                                self.initial_deal = True
                                self.game_deck = copy.deepcopy(self.decks * self.one_deck)
                                self.my_hand = []
                                self.dealer_hand = []
                                self.outcome = 0
                                self.hand_active = True
                                self.reveal_dealer = False
                                self.outcome = 0
                                self.add_score = True
                                self.dealer_score = 0
                                self.player_score = 0

            if self.hand_active and self.player_score >= 21:
                self.hand_active = False
                self.reveal_dealer = True

            self.outcome, self.records, self.add_score = self.check_endgame(self.hand_active, self.dealer_score, self.player_score, self.outcome, self.records, self.add_score)

            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    game = CardGame()
    game.run()
                    