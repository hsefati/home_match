from pydantic import BaseModel, Field
from typing import List

class PropertyQuestionnaireConfig(BaseModel):
    """Configuration settings for the property questionnaire"""
    
    # 
    questions: List[str] = Field(
        default=[
            "How big do you want your house to be?",
            "What are 3 most important things for you in choosing this property?",
            "Which amenities would you like?",
            "Which transportation options are important to you?",
            "How urban do you want your neighborhood to be?",
        ],
        description="List of questions for property preferences."
    )
    
    answers: List[str] = Field(
        default=[
            "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
            "A quiet neighborhood, good local schools, and convenient shopping options.",
            "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
            "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
            "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
        ],
        description="List of default answers to the property preference questions."
    )
    
    chat_bot_temp: float = Field(default=0.0, description="Temperature setting for the chatbot.")
    chat_bot_max_tokens: int = Field(default=4000, description="Maximum number of tokens for chatbot responses.")
    chat_bot_model: str = Field(default="gpt-3.5-turbo", description="Chatbot model in use.")
    
    # AI Prompt to create more real estate listings
    instruction: str = Field(
        default="Generate a CSV file with at least 20 real estate listings.",
        description="Instruction for AI to generate real estate listings."
    )
    
    # Example of a real estate description
    sample_listing: str = Field(
        default="""
        Neighborhood: Green Oaks
        Price: $800,000
        Bedrooms: 3
        Bathrooms: 2
        House Size: 2,000 sqft

        Description: Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.

        Neighborhood Description: Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze.
        """,
        description="Sample real estate listing for AI-generated listings."
    )