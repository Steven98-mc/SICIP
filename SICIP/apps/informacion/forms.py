from django.forms import ModelForm
from django import forms
from betterforms.multiform import MultiModelForm
from .models import Tecnico, mdmqUrbana,Beneficiario, Conyuge,Canton, Parroquia, Ubicacion , Tramite,gadpp,stra,Archivo,mdmq,InformeDirectivo,InformeSociologica,InformeSectorial,drone,predio



class BeneficiarioModelForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['nombre','apellido','cedula','celular','correo','sexo','edad','dignidad','estado_civil','tramite','conyuge']

 
class TramiteModelForm(ModelForm):
    class Meta:
        model = Tramite
        fields = ['tipo_tramite', 'numero','fecha_reunion_ingreso','fecha_reunion_sector','viavilidad','escritura','plano','irm','copia_cedula','otro','tecnico','parroquia','ubicacion']
        widgets = {
            'escritura': forms.CheckboxInput(attrs={'class':'form-control'}),
            'plano': forms.CheckboxInput(attrs={'class':'form-control'}),
            'irm': forms.CheckboxInput(attrs={'class':'form-control'}),
            'copia_cedula': forms.CheckboxInput(attrs={'class':'form-control'})
        }


class IngresoTramiteModelForm(MultiModelForm):
    form_classes = {
        'tramite': TramiteModelForm,
        'beneficiario': BeneficiarioModelForm,
    }
    def save(self, commit=True):
        objects = super(IngresoTramiteModelForm, self).save(commit=False)

        if commit:
            beneficiario = objects['beneficiario']
            beneficiario.save()
            tramite = objects['tramite']
            tramite.save()

        return objects



#seguimiento rural

class gadppModelForm(ModelForm):
    class Meta:
        model = gadpp
        fields = '__all__'

class straModelForm(ModelForm):
    class Meta:
        model = stra
        fields = ['fecha_inspeccion','fecha_certificado_mae','fecha_ingreso_stra','fecha_entrega_providencia','numero_providencia','registro_stra','tramite']


class mdmqModelForm(ModelForm):
    class Meta:
        model = mdmq
        fields = '__all__'

class SeguimientoRuralModelForm(MultiModelForm):
    form_classes = {
        'gadpp': gadppModelForm,
        'stra': straModelForm,
        'mdmq': mdmqModelForm,
    }
    def save(self, commit=True):
        objects = super(SeguimientoRuralModelForm, self).save(commit=False)

        if commit:
            gadpp = objects['gadpp']
            gadpp.save()
            stra = objects['stra']
            stra.save()
            mdmq = objects['mdmq']
            mdmq.save()
        return objects

#Archivo

class archivoModelForm(ModelForm):
    class Meta:
        model = Archivo
        fields = '__all__'
        widgets = {
            'fecha': forms.SelectDateWidget(),
			'razones': forms.Textarea(attrs={'class':'form-control'}),
        }

class ArchivoModelForm(MultiModelForm):
    form_classes = {
        'archivo': archivoModelForm,
    }
    def save(self, commit=True):
        objects = super(ArchivoModelForm, self).save(commit=False)

        if commit:
            archivo = objects['archivo']
            archivo.save()
        return objects

#Informe directivo

class InformeDirectivoModelForm(ModelForm):
    class Meta:
        model = InformeDirectivo
        fields = '__all__'
class conyugeModelForm(ModelForm):
    class Meta:
        model = Conyuge
        fields = '__all__'

class BeneficiarioModelForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['nombre','apellido','cedula','celular','correo','sexo','edad','dignidad','estado_civil','tramite','conyuge']

class ReunionDirectivoModelForm(MultiModelForm):
    form_classes = {
        'informedirectivo': InformeDirectivoModelForm,
        'beneficiario': BeneficiarioModelForm,
    }
    def save(self, commit=True):
        objects = super(ReunionDirectivoModelForm, self).save(commit=False)

        if commit:
            informedirectivo = objects['informedirectivo']
            informedirectivo.save()
            beneficiario = objects['beneficiario']
            beneficiario.save()
        return objects


#seguimientoUrbana

class mdmqUrbanaModelForm(ModelForm):
    class Meta:
        model = mdmqUrbana
        fields = '__all__'

class SeguimientoUrbanaModelForm(MultiModelForm):
    form_classes = {
        'mdmqurbana': mdmqUrbanaModelForm,
    }
    def save(self, commit=True):
        objects = super(SeguimientoUrbanaModelForm, self).save(commit=False)

        if commit:
            mdmqUrbana = objects['mdmqurbana']
            mdmqUrbana.save()
        return objects
#reunion sectorial sociologica

class InformeSociologicaModelForm(ModelForm):
    class Meta:
        model = InformeSociologica
        fields = '__all__'

class InformeSociologicoModelForm(MultiModelForm):
    form_classes = {
        'informesociologica': InformeSociologicaModelForm,
        'beneficiario': BeneficiarioModelForm
    }
    def save(self, commit=True):
        objects = super(InformeSociologicoModelForm, self).save(commit=False)

        if commit:
            informesociologica = objects['informesociologica']
            informesociologica.save()
            beneficiario = objects['beneficiario']
            beneficiario.save()
        return objects


#reunion sectorial tecnica


class InformeSectorialModelForm(ModelForm):
    class Meta:
        model = InformeSectorial
        fields = '__all__'
#        widgets = {
#            'numero': forms.Textarea(attrs={'class':'form-control'}),
#            'CoordenadaX': forms.Textarea(attrs={'class':'form-control'}),
#            'CoordenadaY': forms.Textarea(attrs={'class':'form.control'})
#        }

class droneModelForm(ModelForm):
    class Meta:
        model = drone
        fields = '__all__'

class InformeSectorialTecnicaModelForm(MultiModelForm):
    form_classes = {
        'informesectorial': InformeSectorialModelForm,
        'drone': droneModelForm,
    }
    def save(self, commit=True):
        objects = super(InformeSectorialTecnicaModelForm, self).save(commit=False)

        if commit:
            informesectorial = objects['informesectorial']
            informesectorial.save()
            drone = objects['drone']
            drone.save()
        return objects


#informacion del predio


class predioModelForm(ModelForm):
    class Meta:
        model = predio
        fields = '__all__'

class InformePredioModelForm(MultiModelForm):
    form_classes = {
        'predio': predioModelForm,
        'beneficiario': BeneficiarioModelForm
    }
    def save(self, commit=True):
        objects = super(InformePredioModelForm, self).save(commit=False)

        if commit:
            predio = objects['predio']
            predio.save()
            beneficiario = objects['beneficiario']
            beneficiario.save()
        return objects

#conyuge

class conyugeModelForm(ModelForm):
    class Meta:
        model = Conyuge
        fields = '__all__'

class ConyugeModelForm(MultiModelForm):
    form_classes = {
        'conyuge': conyugeModelForm,
    }
    def save(self, commit=True):
        objects = super(ConyugeModelForm, self).save(commit=False)

        if commit:
            conyuge = objects['conyuge']
            conyuge.save()
        return objects


