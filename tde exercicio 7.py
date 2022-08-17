horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
# Um hora tem 60 minutos
transcorrido_min = 60 * horas + minutos
transcorrido_seg = segundos
print('Total transcorrido do dia em minutos e segundos {}m {}s'.format(transcorrido_min, transcorrido_seg))