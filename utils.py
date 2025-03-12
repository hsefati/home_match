from pydantic import BaseModel, Field, NonNegativeInt
from typing import List

class PropertyListing(BaseModel):
    """
    Represents a property listing with details about the real estate.
    
    Attributes:
    - location: The neighborhood or area where the property is situated.
    - price: The listed price of the property (must be non-negative).
    - num_bedrooms: The total number of bedrooms in the property.
    - num_bathrooms: The total number of bathrooms in the property.
    - square_footage: The total size of the property in square feet.
    - details: A brief description of the property.
    - area_overview: Information about the surrounding neighborhood.
    """
    location: str = Field(..., description="The area where the property is located")
    price: NonNegativeInt = Field(..., description="The listed price in USD")
    num_bedrooms: NonNegativeInt = Field(..., description="Number of bedrooms available")
    num_bathrooms: NonNegativeInt = Field(..., description="Number of bathrooms available")
    square_footage: NonNegativeInt = Field(..., description="Total area in square feet")
    details: str = Field(..., description="Description of the property")
    area_overview: str = Field(..., description="Overview of the neighborhood and its amenities")

class PropertyCollection(BaseModel):
    """
    A collection of property listings.
    
    Attributes:
    - properties: A list of available property listings.
    """
    properties: List[PropertyListing] = Field(..., description="A list of property listings")
