# coding: utf-8

# In[34]:


from asammdf import MDF, Signal
import numpy as np
import scipy.signal
import random
import uuid
import os
import py


# $$ y(t) = A\sin(2 \pi f t + \varphi) = A\sin(\omega t + \varphi) $$

# In[35]:


channels = {
    "engine_speed": "rpm",
    "engine_speed_desired": "rpm",
    "vehicle_speed": "kph",
    "transmission_gear": "uint8",
    "coolant_temp": "C",
    "longitude": "",
    "latitude": "",
    "power": "W",
    "efficiency": "[unitless]",
    "X": "",
    "Y": "" ,
}

companies = [
    "HeavyEquipmentInc",
    "CarCompanyLLC",
    "HeavyDutyTruckCorp",
    "AerospaceStartup",
]
products = [
    "Bulldozer",
    "DumpTruck",
    "Excavator",
    "Transmission",
    "Airplane",
]
versions = [
    '2.00',
    '2.10',
    '2.14',
    '3.00',
    '3.10',
    '3.20',
    '3.30',
    '4.00',
    '4.10',
    '4.11',
]


# In[36]:


tf=10
t1=np.arange(0, tf, 1, dtype=np.float32)
t2=np.arange(0, tf, 2, dtype=np.float32)
t5En1=np.arange(0, tf, 5e-1, dtype=np.float32)
t1En3=np.arange(0, tf, 1e-3, dtype=np.float32)
timestamps = [t1, t2, t5En1, t1En3]

def sine(t, A=1, f=1):
    sine_ = A*np.sin(
        2 * np.pi * f * t
    )
    return sine_
    
def cos(t, A=1, f=1):
    cos_ = A*np.sin(
        2 * np.pi * f * t
    )
    return cos_

def square(t, A=1, f=1):
    square_ = A*scipy.signal.square(
        2 * np.pi * f * t
    )
    return square_

def sawtooth(t, A=1, f=1):
    sawtooth_ = A*scipy.signal.sawtooth(
        2 * np.pi * f * t,
        width=1,
    )
    return sawtooth_

def triangle(t, A=1, f=1):
    triangle_ = A*scipy.signal.sawtooth(
        2 * np.pi * f * t,
        width=0.5,
    )
    return triangle_

signal_generators = [sine, cos, square, sawtooth, triangle]


# In[37]:


signals = list()
for channel_name, channel_units in channels.items():
    if isinstance(channel_units, str):
        channel_unit = channel_units
    else:
        raise type(channel_units)
    
    signal_generator = random.choice(signal_generators)

    A = random.randint(1, 10)
    f = random.randint(1, 100)
    T = random.choice(timestamps)
    Y = signal_generator(T, A, f)
    
    signal_ = Signal(
        samples=Y,
        timestamps=T,
        name=channel_name,
        unit=channel_unit,
    )
    signals.append(signal_)

company = random.choice(companies)
product = random.choice(products)
version = random.choice(versions)

data_file_uuid = str(uuid.uuid4())

# In[38]:


channel_path_ = ["Data", company, product, data_file_uuid]

channel_path = py.path.local(
        os.path.join(*channel_path_)
)

channel_path.dirpath().ensure(dir=True)


# In[39]:

if __name__ == "__main__":
    mdf = MDF(
        version=version,
    )
    mdf.append(
        signals=signals,
        common_timebase=False,
    )
    o = mdf.save(
        dst=str(channel_path),
        overwrite=True,
        compression=2,
    )
    print(o)

