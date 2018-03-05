phgeograpy (PH Geography)
===

phgeograpy is a python package that lists regions, provinces, and cities/municipalities in the Philippines.

Take a break from machine learning and chatbots. I created this project to explore and experience building a python package. This is my first python package. Yey! I'll also use this project to expore unit testing.

I'm working on a web app that needs location input broken down into regions, provinces, and cities/municipalities so I created this package to make it reusable and open source. Technically it's just a list, you can use it to create dropdown inputs or model choices in Django.

# Regions

Regions are represented by `phgeograpy.Region` class.

Sample usage:

```python
import phgeograpy

# Get all regions in the philippines
regions = phgeograpy.regions()

# Get the details of the first region
print(regions[0].slug)  # A unique id of the region
print(regions[0].name)  # Name of the region
print(regions[0].description)  # A longer/alternative name of the region

# Get a specific region.
# If no region is found, an Exception will be raised.
region = phgeograpy.regions('ncr')  # `ncr` is the slug of NCR.
```

# Provinces

Provinces are represented by `phgeograpy.Province` class.

Sample usage:

```python
import phgeograpy

# Get all provinces in the philippines
provinces = phgeograpy.provinces()

# Get the details of the first province
print(provinces[0].slug)  # A unique id of the province
print(provinces[0].name)

# Get the region where the province is located
region = provinces[0].region

# Get provinces of a specific region
region1_provinces = phgeograpy.provinces(region_slug='region1')

# You can also get the provinces from the `phgeograpy.Region` class instance
region1 = phgeograpy.regions('region1')
region1_provinces = region1.provinces()
```

# Municipalities

Municipalities are represented by `phgeograpy.Municipality` class. Cities are also included.

Sample Usage:

```python
import phgeograpy

# Get all municipalities in the philippines
municipalities = phgeograpy.municipalities()

# Get the details of the first municipality
print(municipalities[0].slug)  # A unique id of the municipality
print(municipalities[0].name)
print(municipalities[0].is_city)  # `True` if the instance is a city
print(municipalities[0].is_capital)  # `True` if the instance is the capital of the province it is located
print(municipalities[0].is_huc)  # `True` if the instance is a highly-urbanized/independent city

# Get the province where the municipality is located
province = municipalities[0].province

# Get municipalities from the `phgeograpy.Province` class instance
municipalities = province.municipalities()
```

# Raw data

To get raw data, just set `raw` parameter to `True`.

Sample usage:

```python
# Get raw regions data
raw_regions = phgeograpy.regions(raw=True)
```

Note that all data below the area of your query will be included in the raw output (e.g. raw regions will include data for provinces and municipalities, raw provinces will include data for municipalities).
