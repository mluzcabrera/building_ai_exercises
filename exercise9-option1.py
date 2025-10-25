def bot8(pbot, p8_bot, p8_human):
    #calculate P(8-digits)
    #P(8-digits) = P(8-digits | bot) x P(bot) + P(8-digits | human) x P(human)
    p8d = p8_bot * pbot + p8_human * (1-pbot)
    #use it and the Bayes rule to calculate and print out the probability of the new follower being a bot, P(bot | 8-digits):
    #P(bot | 8-digits) =  P(8-digits | bot) x P(bot) / P(8-digits).
    pbot_8 = p8_bot * pbot / p8d
    print(pbot_8)

# you can change these values to test your program with different values
pbot = 0.1 #probability of a follower being a bot 
p8_bot = 0.8 #probability of a bot having a username with 8 digits
p8_human = 0.05 #probability of a human having a username with 8 digits

bot8(pbot, p8_bot, p8_human)
