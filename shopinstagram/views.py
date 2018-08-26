from django.shortcuts import render
from products.models import Product
import os
import requests 

# Create your views here.
def shopinstagram(request):
    # os.environ.get('SECRET_KEY') 
    access_token = os.environ.get('access_token') 
    user_id = os.environ.get('user_id') 
    r = requests.get("https://api.instagram.com/v1/users/"+ user_id +"/media/recent/?access_token=" + access_token + "&count=18")
    recent_media = r.json()
    image_ig_urls= []
    for media in recent_media['data']:
        try:
            ig_product = Product.objects.get(instagram=media['link']).pk
        except Product.DoesNotExist:
            ig_product = 0
        
        imageUrl = media['images']['low_resolution']['url']

        combined_data = {
           'image': imageUrl,
           'productUrl': ig_product
        }
        image_ig_urls.append(combined_data)

    return render(request, "shopinstagram/shopinstagram.html", {'image_ig_urls': image_ig_urls})



# ['url1', 'url2', 'url3']

# [{'image':'url1',  'productUrl': '2'}, 
# {'image':'url2', 'productUrl': ''}, 
# {'image':'url3', 'productUrl': '6'}]
