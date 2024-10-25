Simple test using Shapely to determine where a polygon intersects a partially overlapping line. 

Test is initial code that will be used recursively to query flight height restrictions database. 

Reason, max flight height is not 400ft for all areas in the greater Los Angeles area. Flying a route, we must be able to programmactically set the flight height above ground. 

GroundHeight.py, Testing API endpoint to get the WGS84 ground height at a location. The two values used to set a flight height at a drone enters restricted flight height polygons.