# FastAPI_FileUpload_Display-and-filter-dataframe
In this project we are going to upload Excel/CSV file and filter the data using fast api and jinja2 


## Manual setup 
1. Create virtual environment with `python3 -m venv venv`
2. Add Virtual environment path to source in `~/.bashrc` file at the end `source venv/bin/activate` and open new bash session.You will see `(venv)` which means you are in virtual environment 
3. `pip install -r requirements.txt`
4. `uvicorn main:app --host 0.0.0.0 --port 8081`
5. Open http://localhost:8081/ 

## Docker version
1. Pull latest image `docker pull kasiyashram96/excel-upload-fastapi:latest`
2. Run docker `docker run -dit -p 8081:8081 kasiyashram96/excel-upload-fastapi:latest`
3. Open http://localhost:8081/ 


## Usage 
 Upload file in below page 

 Click on `See data` 

 You can see data now and free to use filters 


-- Kasi Yeswanth