import csv , logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")


#READ (Extract)
def extract(path) :
    with open(path) as f :
        return list(csv.DictReader(f))
    
#CLEAN (Transform)
def transform(rows):
    clean,bad=[],0
    for  r in rows :
        try:
            r["amount"] =int(r["amount"])
            clean.append(r)
        except (ValueError,KeyError):
            bad+=1
    logging.info(f" clean={len(clean)} bad={bad}")
    return clean

# Write (Load)
def load (rows,path) :
    with open (path,"w",newline="") as f :
        w= csv.DictWriter(f,fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

# main
if __name__=="__main__":
    data=extract("data/raw_sales.csv")
    data=transform(data)
    load(data,"output/clean_sales.csv")
    # total Revenue 
    total=sum(r["amount"] for r in data)
    logging.info(f" Total revenue = {total}")
    logging.info(" pipeline done")
