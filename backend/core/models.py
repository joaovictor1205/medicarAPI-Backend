# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class Especialidade(models.Model):
#     nome = models.CharField(max_length=250, unique=True)

#     criado_em = models.DateTimeField(auto_now_add=True)
#     atualizado_em = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name="Especialidade"
#         verbose_name_plural="Especialidades"
#         ordering=['id']

#     def __str__(self):
#         return self.nome


# class Medico(models.Model):
#     nome = models.CharField(max_length=250)
#     crm = models.CharField(max_length=50)
#     email = models.EmailField(max_length=250)
#     telefone = models.CharField(max_length=15)
#     especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='medico')

#     criado_em = models.DateTimeField(auto_now_add=True)
#     atualizado_em = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name="Médico"
#         verbose_name_plural="Médicos"
#         ordering=['id']
#         unique_together=['nome', 'crm']

#     def __str__(self):
#         return self.nome


# class Horario(models.Model):
#     horario = models.CharField(max_length=20)

#     class Meta:
#         verbose_name="Horário"
#         verbose_name_plural="Horários"
#         ordering=['id']

#     def __str__(self):
#         return self.horario


# class Agenda(models.Model):
#     medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='agenda')
#     dia = models.DateField()
#     horarios = models.ManyToManyField(Horario, on_delete=models.CASCADE, related_name='agenda')

#     class Meta:
#         verbose_name="Agenda"
#         verbose_name_plural="Agendas"
#         ordering=['id']

#     def __str__(self):
#         return f'Médico: {self.medico} - Dia: {self.dia}'


# class Consulta(models.Model):
#     data = models.DateField()
#     horario = models.TimeField()
#     data_agendamento = models.DateTimeField(auto_now_add=True)
#     medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='consulta')

#     class Meta:
#         verbose_name="Consulta"
#         verbose_name_plural="Consultas"
#         ordering=['id']
#         unique_together=['data', 'horario', 'medico']

#     def __str__(self):
#         return f'Dia: {self.data} - Horário: {self.horario} / Médico: {self.medico}'
