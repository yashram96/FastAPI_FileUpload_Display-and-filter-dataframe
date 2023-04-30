# FastAPI_FileUpload_Display-and-filter-dataframe
In this project we are going to upload Excel/CSV file and filter the data using fast api and jinja2 


## Manual setup 
### (Extract the project code into a folder and open terminal into project root directory) 
1. Create virtual environment with `python3 -m venv venv`
2. Add Virtual environment path to source in `~/.bashrc` file at the end `source venv/bin/activate` and open new bash session.You will see `(venv)` which means you are in virtual environment 
3. Install dependencies using `pip install -r requirements.txt`
4. Start server `uvicorn main:app --host 0.0.0.0 --port 8081`
5. Open http://localhost:8081/ 

## Docker version
1. Pull latest image `docker pull kasiyashram96/excel-upload-fastapi:latest`
2. Run docker `docker run -dit -p 8081:8081 kasiyashram96/excel-upload-fastapi:latest`
3. Open http://localhost:8081/ 


## Usage 
#### Step 1 : This is home page. Upload file in below page. All the file names will be appended with timestamp and uploaded into media folder in project root directory. 
Quick start with [sample file](api-scrip-master.csv)

 ![image](https://user-images.githubusercontent.com/52245316/235346562-f9e27429-630d-4456-b7b8-bad9de9f8685.png)


#### Step 2 : Click on `Show data` 
 ![image](https://user-images.githubusercontent.com/52245316/235346594-48a6bf5c-1a39-4fa9-86ca-3d92ccf3f141.png)


#### Step 3: You can see data now and free to use search filter and pagination
 ![image](https://user-images.githubusercontent.com/52245316/235346629-c85a2985-d4a9-4086-8c2d-9c0f5aa1bea8.png)



-- Kasi Yeswanth
