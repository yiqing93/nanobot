---
name: city-distance
description: Calculate distance between two cities (straight-line and driving distance).
homepage: https://www.openstreetmap.org/
metadata: {"nanobot":{"emoji":"🗺️","requires":{"bins":["curl"]}}}
---

# City Distance

Calculate distances between two cities using two methods:
1. **Straight-line distance** (as the crow flies) - calculated using Haversine formula
2. **Driving distance** - queried from OpenStreetMap routing service

## Quick Usage

### Method 1: Python Script
```python
import math
import urllib.request
import json
import urllib.parse

def haversine(lat1, lon1, lat2, lon2):
    """Calculate straight-line distance between two points (in km)"""
    R = 6371  # Earth's radius in km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def get_city_coords(city_name):
    """Get coordinates for a city using Nominatim API"""
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={urllib.parse.quote(city_name)}&limit=1"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'nanobot/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if data:
                return float(data[0]['lat']), float(data[0]['lon']), data[0]['display_name']
    except:
        pass
    return None, None, None

def get_driving_distance(lat1, lon1, lat2, lon2):
    """Get driving distance using OSRM"""
    url = f"https://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=false"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'nanobot/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if data.get('routes'):
                return data['routes'][0]['distance'] / 1000  # Convert to km
    except:
        pass
    return None

# Example: Calculate distance between Chengdu and Beijing
city1 = "Chengdu, China"
city2 = "Beijing, China"

lat1, lon1, name1 = get_city_coords(city1)
lat2, lon2, name2 = get_city_coords(city2)

if lat1 and lat2:
    straight_dist = haversine(lat1, lon1, lat2, lon2)
    driving_dist = get_driving_distance(lat1, lon1, lat2, lon2)
    
    print(f"📍 {name1}")
    print(f"📍 {name2}")
    print(f"📏 直线距离：{straight_dist:.1f} km")
    if driving_dist:
        print(f"🚗 开车距离：{driving_dist:.1f} km")
    else:
        print("🚗 开车距离：无法获取")
else:
    print("❌ 无法找到城市坐标")
```

### Method 2: Using the Script
```bash
python3 scripts/city-distance.py "Chengdu" "Beijing"
```

## APIs Used

| API | Purpose | Endpoint |
|-----|---------|----------|
| **Nominatim** | Geocoding (city name → coordinates) | https://nominatim.openstreetmap.org/ |
| **OSRM** | Routing (driving distance) | https://router.project-osrm.org/ |

## Output Format

```
📍 成都市，四川省，中国
📍 北京市，中国
📏 直线距离：1516.8 km
🚗 开车距离：1785.2 km
```

## Notes

- **Straight-line distance**: Always available, calculated mathematically
- **Driving distance**: May not be available for:
  - Cross-border routes
  - Routes requiring ferries
  - Very long distances (API timeout)
- **Accuracy**: Coordinates are approximate (city center)

## Example Results

| From | To | Straight-line | Driving |
|------|-----|---------------|---------|
| Chengdu | Beijing | 1,516.8 km | 1,785.2 km |
| Chengdu | Hong Kong | 1,369.4 km | 1,716.4 km |
