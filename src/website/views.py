from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from src.website.forms import ContactMeForm
from src.website.models import About, Brands, Reviews, Awards, WorkExperience, Expertise, FAQ, Services, Projects


# Create your views here.
class HomeView(TemplateView):
    template_name = "website/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['experience'] = WorkExperience.objects.all().order_by('start_year')
        context['expertise'] = Expertise.objects.all().order_by('skill_name')[:6]
        context['services'] = Services.objects.all()
        context['projects'] = Projects.objects.all()[:2]

        return context


class AboutView(TemplateView):
    template_name = "website/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['logos'] = Brands.objects.order_by('name')[:7]
        context['reviews'] = Reviews.objects.order_by('name')[:5]
        context['awards'] = Awards.objects.order_by('name')[:5]

        return context


class ServicesView(TemplateView):
    template_name = "website/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['logos'] = Brands.objects.order_by('name')[:7]
        context['reviews'] = Reviews.objects.order_by('name')[:5]
        context['awards'] = Awards.objects.order_by('name')[:5]
        context['faqs'] = FAQ.objects.order_by('question')
        context['services'] = Services.objects.all()

        return context


class WorksView(ListView):
    model = Projects
    template_name = "website/works.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Projects.objects.all().order_by('name')[:6]
        paginator = Paginator(qs, 3)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object']= page_object
        return context


class ContactView(TemplateView):
    template_name = "website/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactMeForm()
        context['faqs'] = FAQ.objects.order_by('question')
        return context

    def post(self, request, *args, **kwargs):
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:contact')

        return self.render_to_response({'form': form})


class ProjectDetailView(TemplateView):
    template_name = "website/project-detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        context['project'] = project
        return context