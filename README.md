### <img src="https://cdn-icons-png.flaticon.com/512/1042/1042820.png" height=24 width=24>  Super Resolution v3.0

<small>
Super Resolution 3.0 is a project focused on the fusion of Sentinel-2 optical and Sentinel-1 radar satellite data to generate high-resolution super-resolved images. The project utilizes advanced deep learning techniques to enhance the spatial resolution of satellite imagery, providing detailed and accurate insights for various applications such as environmental monitoring, agriculture, and urban planning.<br><br>
</small>
<center>
<img src="https://r2.easyimg.io/jpn8qnkjy/screenshot_2024-03-20_230205.png" height=400 width=950>
</center><br><br>

#### Run Model Inference of SR3:
```
Inference Notebook : src/notebooks/inference/inference.ipynb 
```
<br>

#### ⚡ Latest SOTA Features:
```
- Generates 1.25m imagery after every 5 day.
- Get cloud free imagery upto 4 cloudy timestaps.
- STAC APIs Integration for Data Download.
- S3 Bucket Integration for SR3
```

#### A Top Level Folder Structure for Pipelining

    
    ├── src                    
    │   ├── data            # contains downloading dataset & datacube scripts     
    │   ├── models          # contains model architectures
    │   ├── pipelines
    │   │     └── pipeline.py # end-to-end pipeline for SR3
    │   │
    │   ├── notebooks       # contains training & inference notebooks   
    │   └── utils           # contains utility & helper modules

<br>
