from services import SocialNetworkScraper

if __name__ == '__main__':
    service = SocialNetworkScraper(fake=True, delay=1)

    title = "Test automated post"
    content = "Test automated post content"
    service.social_network_add_post(title, content, fake=True)
    print('done')
