# Создайте класс Zebra, 
# внутри есть метод which_stripe
# который поочередно печатает фразы «Полоска белая», «Полоска черная» без кавычек
# начиная именно с фразы «Полоска белая»
# Также реализуйте метод run_away, который печатает фразу «Oh, Sugar Honey Ice Tea»

class Zebra:
    def __init__ (self, stripe_iter = 1):
        self.stripe_iter = stripe_iter
        self.stripe = 'Полоска белая'
    def run_away(self):
        print('Oh, Sugar Honey Ice Tea')
    def which_stripe(self):
        if self.stripe_iter % 2 == 0:
            self.stripe = 'Полоска черная'
        else:
            self.stripe = 'Полоска белая'
        self.stripe_iter += 1
        return print(self.stripe)



zebra = Zebra() 
zebra.run_away() # Oh, Sugar Honey Ice Tea
zebra.which_stripe() # Полоска белая
zebra.which_stripe() # Полоска черная
zebra.which_stripe() # Полоска белая
zebra.which_stripe() # Полоска черная
zebra.which_stripe() # Полоска белая
zebra.run_away() # Oh, Sugar Honey Ice Tea


zebra_1 = Zebra() 
zebra_2 = Zebra()
zebra_1.which_stripe() # Полоска белая
zebra_2.which_stripe() # Полоска белая
zebra_1.which_stripe() # Полоска черная
zebra_1.which_stripe() # Полоска белая
zebra_1.which_stripe() # Полоска черная
zebra_2.which_stripe() # Полоска черная
zebra_2.which_stripe() # Полоска белая