#!/usr/bin/env python
import requests

def main():
    print "Hello Rev.Ai"
    r = requests.get('https://api.rev.ai/revspeech/v1beta/account', headers={'Authorization': 'Bearer <api-key>'})
    print(r.text)

if __name__ == '__main__':
  main()