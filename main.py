from fastapi import Request ,FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import datetime
import pandas as pd

from typing import Optional

app = FastAPI()

# Add static files such as css and js
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


# To get unique file name which is uploaded
def get_unique_filename(filename):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    basename, extension = os.path.splitext(filename)
    return f"{basename}_{timestamp}{extension}"

# Home Endpoint
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# To upload file endpoint 
@app.post("/uploadfile", response_class=HTMLResponse)
async def UploadFile(request: Request, file: UploadFile = File(...)):
    
    
    media_folder = os.path.join(os.getcwd(), 'media')
    
    # Creates media folder in root directory if not exists 
    if not os.path.exists(media_folder):
        os.makedirs(media_folder)
    
    # Generates unique file name 
    unique_filename = get_unique_filename(file.filename)
    file_path = os.path.join(media_folder, unique_filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
        
    # redirect success page 
    return RedirectResponse(url="/upload_success/" + unique_filename)
    

# Upload success page 
@app.post("/upload_success/{filename}")
async def create_upload_file(request: Request , filename :str):
  
    return templates.TemplateResponse("upload_success.html", {"request": request,"file_name" : filename})


# To show the file data
@app.get("/showdataframe/{file_name}")
async def show_dataframe(request: Request , file_name : str , page: Optional[int] = 1,search_term: Optional[str] = None, column_select: Optional[str] = None):
    
    # Check and read file type and data into pandas dataframe
    file_extension = file_name.split(".")[-1]
    
    if file_extension == 'csv':
        data = pd.read_csv("media/" + file_name)
    elif file_extension in ['xls', 'xlsx']:
        data = pd.read_excel("media/" + file_name)
    else:
        return "Invalid file format"
    
    data_columns = data.columns.tolist()

    selected_column_name = column_select
    
    # Null values are isplayed as nan in frontend . if the user search using nan this converts into null values
    if search_term == "nan":
        search_term = None
    
    # Check the filtered search values and filter the dataframe 
    if selected_column_name is not None and selected_column_name != 'Select column to search':
        data = data[data[selected_column_name].astype(str) == search_term]
        
    # Calculates the Pagination values 
    # page = int(request.query_params.get("page", default=1))
    per_page = 50
    num_pages = int(data.shape[0] / per_page) + 1
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    
    # Final dataframe 
    rows = data.iloc[start_idx:end_idx].to_dict(orient="records")
    
    if num_pages <= 7:
        page_nums = list(range(1, num_pages+1))
    elif page < 4:
        page_nums = list(range(1, 5)) + ['...', num_pages]
    elif page > num_pages - 3:
        page_nums = [1, '...'] + list(range(num_pages-3, num_pages+1))
    else:
        page_nums = [1, '...', page-1, page, page+1, '...', num_pages]
        
    return templates.TemplateResponse(
        "dataframe.html",
        {
            "request": request,
            "rows": rows,
            "data_columns" :data_columns,
            "num_pages": num_pages,
            "current_page": page,
            "page_nums": page_nums,
            "next_page": page + 1 if page < num_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "file_name": file_name,
            "column_select" : selected_column_name,
            "search_term":search_term
            
        },
        
    )
    
    
    
    
