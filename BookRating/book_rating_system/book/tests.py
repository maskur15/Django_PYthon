from book.models import Rating,User
def remove_all_ratings(request):
    # Remove all ratings from the database
    Rating.objects.all().delete()
    User.objects.all().delete()
    
    print('remove')
remove_all_ratings()