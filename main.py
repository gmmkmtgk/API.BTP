import os, glob
from Controllers import gentable, genresult, genratecsvfiles
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every

app = FastAPI()

@app.get("/")
def refreshprices():
    return "Welcome to Momentum Investing Portal"


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

@app.on_event("startup")
@repeat_every(seconds=60*60*6)  # 6 hour
def refreshprices() -> None:
    try:
        for filename in glob.glob("Result*"):
            os.chmod(filename, 0o777)
            os.remove(filename)
        genratecsvfiles.genratezips()
    except Exception as e:
        pass

