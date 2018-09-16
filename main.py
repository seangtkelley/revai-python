import requests
import revai

def main():
    revai_api = revai.API('definitely not a real api key')
    
    result = revai_api.get_account()
    print(result)

if __name__ == '__main__':
  main()