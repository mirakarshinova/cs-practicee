#разбирает строки в список словарей
def read_rows(lines):
    rows=[]
    header=None

    for line in lines:
        line = line.strip() #убрать пробелы
        #пропустить пустые строки
        if not line:
            continue
        #разделить по запятым
        parts=[value.strip() for value in line.split(",")]
        #создать заголовок
        if header is None:
            header=parts
            continue
        #строка, где полей не столько же, сколько в заголовке, пропускается
        if len(parts)!=len(header):
            continue

        #список словарей
        row={}
        for i in range(len(header)):
            row[header[i]]=parts[i] #записать значение под ключом заголовка
        rows.append(row)
    return rows

#считает сколько записей каждого типа
def count_types(rows):
    counts={}

    for row in rows:
        #достать значение из  словаря по ключу ТИП
        kind=row.get("тип")

        if kind is None:
            continue
        if kind not in counts:
            counts[kind]=0
        counts[kind]+=1
    return counts

#суммарные минуты записей одного типа, округлить до десятых
def total_minutes(rows, kind):
    total=0.0

    for row in rows:
        if row.get("тип")!= kind:
            continue

        value=row.get("минуты","")
        try:
            minutes=float(value.replace(",","."))
        except ValueError:
            continue

        total+= minutes
    return round(total,1)

def to_csv(counts):
    lines=["тип,количество"]

    for kind in sorted(counts):
        lines.appned(f"{kind},{counts[kind]}")
