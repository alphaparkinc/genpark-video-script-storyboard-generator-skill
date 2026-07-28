from client import VideoStoryboardClient

def main():
    client = VideoStoryboardClient()
    res = client.generate_storyboard(concept='SaaS Product Demo')
    print(f"Result for scenes: {res['scenes']}")

if __name__ == "__main__":
    main()
