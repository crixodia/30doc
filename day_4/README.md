# Día 4: Fechas

Supongamos que tenemos dos fechas Fecha 1: 04/04/2022 y Fecha 2: 23/04/2022, fechas de inicio y fin, respectivamente. Y quiero distribuir un numero n de horas en este rango de fechas.

Por ejemplo, quiero distribuir 120 horas, en las fechas indicadas anteriormente, sin considerar los fines de semana, el programa me debería de mostrar: 08:00:00.

¿Qué deberías presentar?

1. Programa una función que reciba fecha 1 y fecha 2 y el número n de horas total a distribuir, y nos retorne la cantidad de horas, minutos y segundos (de ser el caso) que tiene que dedicar diariamente una persona para lograr cumplir n horas en el rango de fechas comprendido entre Fecha 1 y Fecha 2, sin considerar los fines de semana.

**Nota:** Considera como primer día de la semana el lunes y como último día de la semana el domingo.

**Nota:** El formato de las fechas es dd/mm/yyyy y para el formato del tiempo HH:MM:SS.

## Solución

Para este problema utilizamos los módulos que provee Python para trabajar con fechas y horas, en este caso utilizamos el módulo datetime. Con datetime podemos dar formato a las fechas y horas. Por otro lado, con timedelta podemos realizar operaciones con fechas y horas.

La solucion consiste en contar los días que transcurren desde la fecha inicial hasta la final. Luego, se calcula el número de días hábiles, es decir, los días que no son fines de semana. Finalmente, se calcula la cantidad de horas que debe dedicar diariamente una persona para lograr cumplir n horas en el rango de fechas.

```python
def date_div(date1: str, date2: str, n: int) -> datetime:
    # Formato dd/mm/yyyy HH:MM:SS
    date1 = datetime.strptime(date1, "%d/%m/%Y %H:%M:%S")
    date2 = datetime.strptime(date2, "%d/%m/%Y %H:%M:%S")

    days = 0
    while date1 < date2:
        # Desde Lunes hasta Viernes
        if date1.weekday() < 5:
            days += 1
        date1 += timedelta(days=1)

    return timedelta(hours=n / days)
```

## Video Explicativo

<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@crixodia/video/7149021110917401861" data-video-id="7149021110917401861" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@crixodia" href="https://www.tiktok.com/@crixodia?refer=embed">@crixodia</a> Día 4 <a title="30daysofcode" target="_blank" href="https://www.tiktok.com/tag/30daysofcode?refer=embed">#30DaysOfCode</a> <a title="30daysofcodebyaeis" target="_blank" href="https://www.tiktok.com/tag/30daysofcodebyaeis?refer=embed">#30DaysOfCodeByAEIS</a> <a title="python" target="_blank" href="https://www.tiktok.com/tag/python?refer=embed">#Python</a> <a target="_blank" title="♬ original sound - Gabriel Bastidas" href="https://www.tiktok.com/music/original-sound-7149021184636947205?refer=embed">♬ original sound - Gabriel Bastidas</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
