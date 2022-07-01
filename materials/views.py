from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView


from .models import Material


class MaterialListView(ListView):
    queryset = Material.objects.published()
    template_name = 'materials/list.html'
    paginate_by = 12


class MaterialDetailView(DetailView):
    queryset = Material.objects.published()
    template_name = 'materials/detail.html'


"""
class MaterialDownloadView(DetailView):
    queryset = Material.objects.published()

    def get(self, request, *args, **kwargs):
        mat = self.get_object()
        stat, created = Statistic.objects.get_or_create(
            material=mat, date=timezone.now()
        )
        if not created:
            stat.count += 1
            stat.save()
        return HttpResponse(
            mat.storage.read(), content_type='application/blender')


@login_required
def vote(request, pk, slug, score):
    mat = get_object_or_404(Material, pk=pk, slug=slug)
    voting, created = Vote.objects.get_or_create(
        user=request.user, material=mat, defaults={'score': score},
    )
    if not created:
        voting.score = score
        voting.save()
    return HttpResponseRedirect(reverse(
        'materials:detail', kwargs={'pk': pk, 'slug': slug}))
# Create your views here.
"""
