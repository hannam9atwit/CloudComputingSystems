from fastapi import FastAPI, Query, Path, Body
import uvicorn

app = FastAPI()

# Simple Hello World route
@app.get("/helloworld")
async def hello():
    return {"message": "Hello from FastAPI"}

# Route with a path parameter and query parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="Item ID"), q: str = Query(None)):
    return {"item_id": item_id, "query_param": q}

# PUT route that takes body input
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict = Body(...)):
    return {"item_id": item_id, "updated_item": item}

# GET user profile
@app.get("/users/{user_id}")
async def get_user(user_id: int, details: bool = Query(False)):
    return {"user_id": user_id, "details": details}

# PUT user profile update
@app.put("/users/{user_id}")
async def update_user(user_id: int, data: dict = Body(...)):
    return {"user_id": user_id, "updated_data": data}

# GET search items with keyword filter
@app.get("/search")
async def search_items(keyword: str = Query(...), limit: int = Query(10)):
    return {"keyword": keyword, "limit": limit}

# PUT modify a record
@app.put("/modify/{record_id}")
async def modify_record(record_id: int, content: dict = Body(...)):
    return {"record_id": record_id, "modified_content": content}

# System status check
@app.get("/status")
async def status_check():
    return {"status": "Running"}

# GET configuration setting
@app.get("/config/{setting}")
async def get_config(setting: str):
    return {"setting": setting, "value": "default"}

# PUT update configuration setting
@app.put("/config/{setting}")
async def update_config(setting: str, value: str = Body(...)):
    return {"setting": setting, "new_value": value}

# GET reports based on year
@app.get("/reports/{year}")
async def get_reports(year: int):
    return {"year": year, "reports": ["report1", "report2"]}

# PUT update reports for a given year
@app.put("/reports/{year}")
async def update_reports(year: int, report_data: dict = Body(...)):
    return {"year": year, "updated_reports": report_data}

# GET system settings based on option
@app.get("/settings/{option}")
async def get_setting(option: str):
    return {"option": option, "value": "enabled"}

# PUT update system settings
@app.put("/settings/{option}")
async def update_setting(option: str, new_value: str = Body(...)):
    return {"option": option, "new_value": new_value}

# Summary report
@app.get("/summary")
async def summary_report():
    return {"summary": "System operational"}

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
