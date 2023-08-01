import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request,'../templates/index.html')

@csrf_exempt
def download(request):
    if request.method == 'POST':
        video_url = request.POST.get('videoUrl')

        # Ganti "YOUR_API_ENDPOINT" dengan URL endpoint dari API TikTok video downloader Anda
        api_endpoint = "https://api.tik.fail/api/grab"

        # Kirim permintaan ke API TikTok video downloader menggunakan requests
        response = requests.get(api_endpoint, params={'url': video_url})

        if response.ok:
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Error while downloading video.'}, status=response.status_code)

    return JsonResponse({'error': 'Invalid request.'}, status=400)