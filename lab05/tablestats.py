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
        #заполняем массив строк (dict(zip) -- автоматически создает словарь с ключами из header и значениями из parts). 
        # Итог: rows список строк с словарями внутри
        rows.append(dict(zip(header, parts)))
    return rows



#считает сколько записей каждого типа
def count_types(rows):
    counts={}

    for row in rows:
        #достать значение из  словаря по ключу ТИП
        kind=row.get("тип")

        if kind not in counts:
            counts[kind]=0 #если тип встретился впервые добавляем в словарь со значением 0
        counts[kind]+=1
        #counts[kind] = counts.get(kind, 0) + 1  добавляем тип если он уже есть в словаре со зачением его +1, если нет - со значением 0 +1
    return counts

#суммарные минуты записей одного типа, округлить до десятых
def total_minutes(rows: list[dict], kind: str)-> float:
    total=0.0

    for row in rows:
        if row.get("тип")!= kind:
            continue

        value=row.get("минуты","") #вернуть пустое если ключа минуты нет
        try:
            minutes=float(value.replace(",","."))
            #minutes =  float(row['минуты'].replace(",", "."))
        except ValueError:
            continue

        total+= minutes
    return round(total,1)


#сводка текстом CSV: заголовок тип,количество, строки по алфавиту
def to_csv(counts: dict) -> str:
    lines=["тип,количество"]

    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}") #counts[kind] обращение к словарю по ключу kind
    return "\n".join(lines)+"\n"