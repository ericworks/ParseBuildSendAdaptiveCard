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
    try:
        card, webhook = AdaptiveCardBuilder.make_card()
        AdaptiveCardSender.send_requests(webhook, card)
    except Exception as e:
        print(f"Error: {e}")
        print("Error: Please check your parameters and try again.")
        exit(1)
