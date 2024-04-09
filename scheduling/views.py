from . with_celery import analyze_user_dna_and_email
def get_user():
    pass

# add .delay to the end of the function name using celery
# .delay dont call the function immediately, it will put it in the queue in queue task
def analyze_dna(request):
    user = get_user(request)
    analyze_user_dna_and_email.delay(dna_file, request.user.email)
    return "Check your email for your report."

# after creating view
# create celery worker : celery -A tasks worker --loglevel=info