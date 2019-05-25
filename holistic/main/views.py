from django.shortcuts import render


def index(request):
    context = {'latest_question_list': 1}
    return render(request, 'base.html', context)

#
# class ProfileView(ListCreateAPIView):
#     pass
#
#
# class DigestView(ListCreateAPIView):
#     pass
