# Basic MDF processing.


```python
from mdf_models import Channel, MDF, db

from pony.orm import *
```

TODO: Make this more descriptive for notebooks.


```python
# Select the first MDF file
q = MDF.select()
# Get the first MDF indexed.
mdf_sql = q.first()
mdf_sql
```




    MDF[1]



# List the channels in the file.

TODO: Make *this* more descriptive.


```python
list(mdf_sql.channels)
```




    [Channel[10],
     Channel[5],
     Channel[7],
     Channel[3],
     Channel[6],
     Channel[2],
     Channel[12],
     Channel[4],
     Channel[1],
     Channel[11],
     Channel[9],
     Channel[8]]




```python
# For each of the channels in the MDF file:
for channel in mdf_sql.channels:
    # Print the channel name
    print(channel.name)
```

    efficiency
    transmission_gear
    longitude
    engine_speed_desired
    coolant_temp
    engine_speed
    Y
    vehicle_speed
    time
    X
    power
    latitude



```python
channel.name
```




    'latitude'




```python
channel
```




    Channel[8]




```python
# Set of MDFs that have the channel above.
channel.mdfs
```




    <MDFSet Channel[8].mdfs>



Get the channel for engine speed. 


```python
engine_speed = Channel.select().filter(lambda channel: channel.name == "engine_speed").first()
```


```python
engine_speed
```




    Channel[2]



# Find MDFs missing channel 

MDFs missing engine speed:


```python
bad_mdfs = list()
for mdf in MDF.select():
    if channel not in mdf.channels:
        bad_mdfs.append(mdf)
```


```python
for bad_mdf in bad_mdfs:
    break
```


```python
bad_mdf.path
```




    '/projects/MDF_Data_Pipeline/Data/CarCompanyLLC/Boat/7218f46b-2da1-4722-a659-96b4bb197313.mdf'




```python
bad_mdf.size_mb
```




    20.00023365020752




```python
bad_mdf.path
```




    '/projects/MDF_Data_Pipeline/Data/CarCompanyLLC/Boat/7218f46b-2da1-4722-a659-96b4bb197313.mdf'



# Find MDF Files By Size

Big MDFs.


```python
query = select(mdf for mdf in MDF
               if mdf.size_mb>1024)
query.count()
```




    3



Medium MDFs.


```python
query = select(mdf for mdf in MDF
               if mdf.size_mb<100 and mdf.size_mb>50)
query.count()
```




    295



Small MDFs.


```python
query = select(mdf for mdf in MDF
               if mdf.size_mb<1)
query.count()
```




    1000




```python
mdf_obj = query.first()
mdf_obj
```




    MDF[1]




```python
mdf_obj.path
```




    '/projects/MDF_Data_Pipeline/Data/HeavyEquipmentInc/Airplane/5ab19863-6324-41b4-a7c0-387a38d00d3c.mf4'




```python
mdf_obj.size
```




    171256.0




```python
mdf_obj.size_mb
```




    0.16332244873046875




```python
MDF
```




    mdf_models.MDF



\#namespaces.


```python
import asammdf
```


```python
mdf = asammdf.MDF(mdf_obj.path)
```


```python
asammdf.__version__
```




    '5.20.0.dev2'




```python
mdf.channels_db
```




    {'time': ((0, 0),),
     'engine_speed': ((0, 1),),
     'engine_speed_desired': ((0, 2),),
     'vehicle_speed': ((0, 3),),
     'transmission_gear': ((0, 4),),
     'coolant_temp': ((0, 5),),
     'longitude': ((0, 6),),
     'latitude': ((0, 7),),
     'power': ((0, 8),),
     'efficiency': ((0, 9),),
     'X': ((0, 10),),
     'Y': ((0, 11),)}




```python
for channel in mdf.iter_channels():
    channel.plot()
```

    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_1.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_3.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_5.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_7.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_9.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_11.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_13.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_15.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_17.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_19.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/03_Analyze_Indexed_Files_files/docs/markdown/03_Analyze_Indexed_Files_36_21.png)



```python
import numpy as np
```


```python
np.mean(np.diff(channel.timestamps))
```




    0.0009992006145014896


