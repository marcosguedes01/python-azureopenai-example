def getResultFromResponse(response):
    return response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()