import herepy
import ast

def getLocationDetails(latitude, longitude):
    latitude = float(latitude)
    longitude = float(longitude)

    gp = herepy.GeocoderReverseApi('jHffeGfyLsxEo6Jn0G77H70R8mO9BXL6xQQgrJlqe4o')
    response = gp.retrieve_addresses([latitude, longitude])
    response = str(response)
    response = ast.literal_eval(response)
    response = response["items"][0]["address"]["label"]

    return response

result = getLocationDetails(19.310472, 72.854042)
