from datetime import datetime, timedelta


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


if __name__ == "__main__":
    # 29 - 30, cubrir 2 horas -> 2 día
    print(date_div("29/09/2022 00:00:00", "01/10/2022 00:00:00", 2))

    # 26 - 30, cubrir 2 horas -> 5 días
    print(date_div("26/09/2022 00:00:00", "01/10/2022 00:00:00", 2))

    # Omitir fines de semana
    # 29 - 2, cubrir 2 horas -> 2 días
    print(date_div("29/09/2022 00:00:00", "03/10/2022 00:00:00", 2))
