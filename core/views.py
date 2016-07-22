from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.
@login_required
def usuario_detalhe(request):
	return render(request,'usuario.html')

# @login_required
# @permission_required('armazem.pode_administrar')
#def armazem_cria(request): 
#	form = ArmazemForm(request.POST or None)
#	if form.is_valid():
#		instance = form.save(commit=False)
#		instance.usuario = request.user
#		instance.save()
#		messages.success(request,' Armazém foi criado.')
#		return HttpResponseRedirect(instance.get_absolute_url())
#	context = {'form':form,}
#	return render(request,'armazem_form.html', context)	


#@login_required
#def fornecedor_edita(request,id=None):#
#	instance = get_object_or_404(Fornecedor,id=id)
#	form = FornecedorForm(request.POST or None, instance=instance)
#	if form.is_valid():
#		instance = form.save(commit=False)
#		instance.usuario = request.user
#		instance.save()
#		messages.success(request,' Fornecedor foi modificado.')
#		return HttpResponseRedirect(instance.get_absolute_url())
#	context = { 'instance':instance, 'form':form }
#	return render(request,'fornecedor_form.html', context)