import sopel.module
from sopel.tools import events

@sopel.module.event(events.RPL_WELCOME)
def welcome(bot, trigger):
    bot.say("Benvenuto %s"%(trigger.group(2)))

@sopel.module.commands('birra')
@sopel.module.example('.birra')
def birra(bot, trigger):
    """print a beer!"""
    bot.say(' .   *   ..  . *  *')
    bot.say(' *  * @()Ooc()*   o  .  ')
    bot.say('     (Q@*0CG*O()  ___ ')  
    bot.say('    |\_________/|/ _ \'') 
    bot.say('    |  |  |  |  | / | | ')
    bot.say('    |  |  |  |  | | | | ')
    bot.say('    |  |  |  |  | | | | ')
    bot.say('    |  |  |  |  | | | | ')
    bot.say('    |  |  |  |  | | | | ')
    bot.say('    |  |  |  |  | \_| | ')
    bot.say('    |  |  |  |  |\___/  ')
    bot.say('    |\_|__|__|_/|       ')
    bot.say('     \_________/        ')

@sopel.module.commands('aiuto')
@sopel.module.example('.aiuto')
def aiuto(bot, trigger):
    """print a info messagge"""
    bot.say('benvenuto nel canale #Pubo!')
    bot.say('digita .birra per una birra!')
    bot.say('digita .radio per avere info sulla radio')
    bot.say('oppure lascia un messaggio e verrai riconttato/a!')

@sopel.module.commands('radio')
@sopel.module.example('.radio')
def radio(bot, trigger):
    """print a radio message"""
    bot.say('Il fondatore di questo canale')
    bot.say('e anche un appassionato di musica HC, Oi! e punk')
    bot.say('e ha deciso quindi di fondare una piccola radio web:')
    bot.say('undergm.caster.fm ')
    bot.say('la radio trasmette solo musica della scena punk Oi! italia')
    bot.say('dagli anni 80 a oggi.')
    bot.say('Insieme alla radio per raccontare un po la storia di questo mondo')
    bot.say('ha creato anche un sito: undergroundmap.altervista.org ')
            


if __name__=="__main__":
    from sopel.test_tools import run_example_tests
    run_example_tests(__file__)
