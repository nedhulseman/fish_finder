from instaloader import Instaloader


loader = Instaloader()
loader.interactive_login('sydneyrae.hulseman')
loader.download_hashtag('rainbowtrout', max_count=200)
