from services import SocialNetworkScraper
import config
if __name__ == '__main__':
    service = SocialNetworkScraper(fake=True, delay=config.CHROME_DRIVER_DELAY)

    title = "Test automated post"
    content = "Test automated post content"
    service.social_network_add_post(title, content, fake=True)
    print('done')
