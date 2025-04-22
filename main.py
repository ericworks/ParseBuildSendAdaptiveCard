from PyinstallerUtils import *
patch_exit()
import AdaptiveCardBuilder
import AdaptiveCardSender


if __name__ == "__main__":
    print("===========================================")
    print("ParseBuildSendAdaptiveCard v1.0.0")
    print("Author: Eric YOU")
    print("===========================================")
    print("")
    card, webhook = AdaptiveCardBuilder.make_card()
    
    AdaptiveCardSender.send_requests(webhook, card)

