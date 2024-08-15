from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import frmCreateClient
from .models import clients

class viewIndex(TemplateView):
	template_name = 'base.html'
	
class viewCreateClient(TemplateView):
	template_name = 'createClient.html'
	
	def get_context_data(self, **kwargs):
		context = super(viewCreateClient, self).get_context_data(**kwargs)
		context["form"] = frmCreateClient()
		return context

	def post(self,request,*args, **kwargs):
		errors = "", ""
		form = frmCreateClient(request.POST)
		if form.is_valid():
			clt:clients = clients()
			clt.codigoClt = request.POST['codigoClt']
			clt.razonSocialClt = request.POST['razonSocialClt']
			clt.rfcClt = request.POST['rfcClt']
			clt.regimenFiscalClt = request.POST['regimenFiscalClt']
			clt.mainTelClt = request.POST['mainTelClt']
			clt.mainEmailClt = request.POST['mainEmailClt']
			clt.mainCalleyCruzamientosClt = request.POST['mainCalleyCruzamientosClt']
			clt.mainNumExtClt = request.POST['mainNumExtClt']
			clt.mainNumIntClt = request.POST['mainNumIntClt']
			clt.mainCpClt = request.POST['mainCpClt']
			clt.mainAsentamientoClt = request.POST['mainAsentamientoClt']
			clt.mainLocalidadClt = request.POST['mainLocalidadClt']
			clt.mainMunicipioClt = request.POST['mainMunicipioClt']
			clt.mainEstadoClt = request.POST['mainEstadoClt']
			clt.mainPaisClt = request.POST['mainPaisClt']
			clt.save()
			errors = 'Cliente {cRS}, almacenado exitosamente.'.format(cRS=clt.razonSocialClt) 
		else:
			errors = form.errors

		return render(
			request,
			'createClient.html',
			{"errors": errors,"form":form}
		)

class ListClientView(TemplateView):
	template_name = 'listClients.html'

	def get(self, request):
		context = {}
		context['clients'] = clients.objects.all()
		return render(request,self.template_name,context)

