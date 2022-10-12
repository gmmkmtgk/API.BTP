import os, glob
from Controllers import gentable, genresult, genratecsvfiles
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/getstocks/{week}/{month}/{tmonth}/{smonth}/{year}")
def getstocks(week: int, month: int, tmonth: int, smonth: int, year: int):
    filename = 'Result' + str(week) + str(month) + str(tmonth) + str(smonth) + str(year) + '.csv'
    chk_file = Path(filename)
    if chk_file.is_file():
        return FileResponse(filename)
    else:
        df_inner = gentable.gen()
        resultStocks = genresult.getresult(df_inner,week,month,tmonth,smonth,year)  
        resultStocks.to_csv(filename)
    return FileResponse(filename)


@app.post("/refreshprices")
def refreshprices():
    try:
        for filename in glob.glob("Result*"):
            os.chmod(filename, 0o777)
            os.remove(filename)
        genratecsvfiles.genratezips()
        return {"message" : "Sucessfully done"}
    except Exception as e:
        return {"error":str(e)}