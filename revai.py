import requests
import json
import time

    
class API:

    HEADERS = {'Authorization': ''}

    def __init__(self, api_key=''):

        if len(api_key) == 0:
            raise ValueError("API Key cannot be empty")
        
        self.HEADERS['Authorization'] = "Bearer " + api_key


    def submit_job_url(self, media_url):
        url = "https://api.rev.ai/revspeech/v1beta/jobs"
        payload = {'media_url': media_url,
                'metadata': "Test"}
        request = requests.post(url, headers=self.HEADERS, json=payload)

        response_body = request.json()
        return response_body

    def submit_job_file(self, file):
        url = "https://api.rev.ai/revspeech/v1beta/jobs"
        files = { 'media': (file, open(file, 'rb'), 'audio/mp3') }
        request = requests.post(url, headers=self.HEADERS, files=files)

        response_body = request.json()
        return response_body

    def view_job(self, id=59594172):
        url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}'
        request = requests.get(url, headers=self.HEADERS)

        response_body = request.json()
        return response_body

    def get_transcript(self, id='59594172'):
        url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}/transcript'
        headers = self.HEADERS.copy()
        headers['Accept'] = 'application/vnd.rev.transcript.v1.0+json'
        request = requests.get(url, headers=headers)

        response_body = request.json()
        return response_body
    
    def get_account(self):
        url = 'https://api.rev.ai/revspeech/v1beta/account'
        request = requests.get(url, headers=self.HEADERS)

        response_body = request.json()
        return response_body