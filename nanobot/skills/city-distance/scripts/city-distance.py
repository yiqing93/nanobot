#!/usr/bin/env python3
"""
City Distance Calculator
Calculate straight-line and driving distances between two cities.
"""

import math
import urllib.request
import json
import urllib.parse
import sys

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate straight-line distance between two points using Haversine formula
    
    Args:
        lat1, lon1: Coordinates of first point (in degrees)
        lat2, lon2: Coordinates of second point (in degrees)
        
    Returns:
        Distance in kilometers
    """
    R = 6371  # Earth's radius in km
    
    # Convert to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c

def get_city_coords(city_name):
    """
    Get coordinates for a city using Nominatim API
    
    Args:
        city_name: Name of the city (e.g., "Chengdu, China")
        
    Returns:
        Tuple of (latitude, longitude, display_name) or (None, None, None) if not found
    """
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={urllib.parse.quote(city_name)}&limit=1"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'nanobot/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if data:
                return float(data[0]['lat']), float(data[0]['lon']), data[0]['display_name']
    except Exception as e:
        print(f"Error getting coordinates: {e}", file=sys.stderr)
    
    return None, None, None

def get_driving_distance(lat1, lon1, lat2, lon2):
    """
    Get driving distance using OSRM routing service
    
    Args:
        lat1, lon1: Coordinates of starting point
        lat2, lon2: Coordinates of destination
        
    Returns:
        Distance in kilometers, or None if route not available
    """
    url = f"https://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=false"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'nanobot/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if data.get('routes'):
                return data['routes'][0]['distance'] / 1000  # Convert meters to km
    except Exception as e:
        print(f"Error getting driving distance: {e}", file=sys.stderr)
    
    return None

def calculate_city_distance(city1_name, city2_name):
    """
    Calculate both straight-line and driving distances between two cities
    
    Args:
        city1_name: Name of the first city
        city2_name: Name of the second city
        
    Returns:
        Dictionary with distance information
    """
    # Get coordinates for both cities
    lat1, lon1, name1 = get_city_coords(city1_name)
    lat2, lon2, name2 = get_city_coords(city2_name)
    
    if not (lat1 and lat2):
        return {
            'success': False,
            'error': 'Could not find coordinates for one or both cities'
        }
    
    # Calculate straight-line distance
    straight_dist = haversine(lat1, lon1, lat2, lon2)
    
    # Get driving distance
    driving_dist = get_driving_distance(lat1, lon1, lat2, lon2)
    
    return {
        'success': True,
        'city1': {
            'name': name1,
            'lat': lat1,
            'lon': lon1
        },
        'city2': {
            'name': name2,
            'lat': lat2,
            'lon': lon2
        },
        'straight_line_km': straight_dist,
        'driving_km': driving_dist
    }

def print_result(result):
    """Print the distance calculation result in a formatted way"""
    if not result['success']:
        print(f"❌ {result['error']}")
        return
    
    print(f"📍 {result['city1']['name']}")
    print(f"   坐标：({result['city1']['lat']:.4f}, {result['city1']['lon']:.4f})")
    print()
    print(f"📍 {result['city2']['name']}")
    print(f"   坐标：({result['city2']['lat']:.4f}, {result['city2']['lon']:.4f})")
    print()
    print(f"📏 直线距离：{result['straight_line_km']:.1f} km")
    
    if result['driving_km']:
        print(f"🚗 开车距离：{result['driving_km']:.1f} km")
        # Estimate driving time (assuming 80 km/h average)
        hours = result['driving_km'] / 80
        print(f"   ⏱️ 预计耗时：约 {hours:.1f} 小时（不含休息）")
    else:
        print("🚗 开车距离：无法获取（可能因为跨海/边境限制）")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        city1 = sys.argv[1]
        city2 = sys.argv[2]
        
        print(f"🔍 查询：{city1} → {city2}")
        print()
        
        result = calculate_city_distance(city1, city2)
        print_result(result)
    else:
        print("Usage: python3 city-distance.py <city1> <city2>")
        print()
        print("Examples:")
        print("  python3 city-distance.py \"Chengdu, China\" \"Beijing, China\"")
        print("  python3 city-distance.py \"New York\" \"Los Angeles\"")
        print("  python3 city-distance.py \"London\" \"Paris\"")
