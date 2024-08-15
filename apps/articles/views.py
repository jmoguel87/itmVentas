from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import frmCreateArticle
from .models import articles
	
class viewCreateArticle(TemplateView):
	template_name = 'createArticle.html'
	
	def get_context_data(self, **kwargs):
		context = super(viewCreateArticle, self).get_context_data(**kwargs)
		context["form"] = frmCreateArticle()
		return context

	def post(self,request,*args, **kwargs):
		errors = "", ""
		form = frmCreateArticle(request.POST)
		if form.is_valid():
			art:articles = articles()
			art.codigoArt = request.POST['codigoArt']
			art.nombreArt = request.POST['nombreArt']
			art.descripcionArt = request.POST['descripcionArt']
			art.unidadBaseArt = request.POST['unidadBaseArt']
			art.unidadSatArt = request.POST['unidadSatArt']
			art.claveSatArt = request.POST['claveSatArt']
			art.precioArt = request.POST['precioArt']
			art.save()
			errors = 'Articulo {aN}, almacenado exitosamente.'.format(aN=art.nombreArt) 
		else:
			errors = form.errors

		return render(
			request,
			'createArticle.html',
			{"errors": errors,"form":form}
		)
	
class ListArticleView(TemplateView):
	template_name = 'listArticles.html'

	def get(self, request):
		context = {}
		context['articles'] = articles.objects.all()
		return render(request,self.template_name,context)


