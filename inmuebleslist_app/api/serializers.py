from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa, Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comentario
        exclude = ["edificacion"]
        #fields = "__all__"

class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    class Meta:
        model = Edificacion
        fields = "__all__"

class EmpresaSerializer(serializers.ModelSerializer):
    edificacionlist = EdificacionSerializer(many=True, read_only=True)
    #edificacionlist = serializers.StringRelatedField(many=True)
    #edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #edificacionlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='edificacion-detalle')

    class Meta:
        model = Empresa
        fields = "__all__" 














    # def get_longitud_direccion(self, object):
    #     cantidad_caracteres = len(object.direccion)
    #     return cantidad_caracteres

    # def validate(self, data):
    #     if data["direccion"]==data["pais"]:
    #         raise serializers.ValidationError("La dirección y el país no pueden coincidir")
    #     else:
    #         return data
        
    # def validate_imagen(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError("La URL de la imagen es muy cortita")
    #     else:
    #         return data


# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("El valor es demasiado corto")

# class InmuebleSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators = [column_longitud])
#     pais = serializers.CharField(validators = [column_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance