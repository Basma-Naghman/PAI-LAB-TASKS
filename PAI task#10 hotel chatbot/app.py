from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

HOTEL_INFO = {
    "rooms": {
        "standard": {
            "price": 120,
            "description": "Comfortable 25m² room with queen bed, work desk, and city view",
            "capacity": "2 adults",
            "features": ["Free WiFi", "Smart TV", "Coffee maker", "Air conditioning"],
            "bathroom": "Private bathroom with shower"
        },
        "deluxe": {
            "price": 180,
            "description": "Spacious 35m² room with king bed, sitting area, and panoramic views",
            "capacity": "2 adults + 1 child",
            "features": ["Free WiFi", "Smart TV", "Mini-bar", "Air conditioning", "Bathrobes"],
            "bathroom": "Private bathroom with bathtub and shower"
        },
        "suite": {
            "price": 300,
            "description": "Luxurious 60m² suite with separate living room, dining area, and premium amenities",
            "capacity": "2 adults + 2 children",
            "features": ["Free WiFi", "Two Smart TVs", "Premium mini-bar", "Nespresso machine", 
                        "24/7 butler service", "Air conditioning"],
            "bathroom": "Spa-like bathroom with jacuzzi and premium toiletries"
        },
        "family": {
            "price": 220,
            "description": "Family-friendly 40m² room with two queen beds and child amenities",
            "capacity": "2 adults + 2 children",
            "features": ["Free WiFi", "Smart TV", "Board games", "Baby cot available"],
            "bathroom": "Private bathroom with shower"
        }
    },
    "amenities": {
        "general": ["24-hour front desk", "Concierge service", "Luggage storage", 
                   "Currency exchange", "Elevator", "Accessible facilities"],
        "wellness": ["Fitness center (24/7)", "Indoor swimming pool", "Spa & massage services", 
                    "Sauna", "Yoga classes"],
        "dining": ["Main restaurant (Breakfast 6-10:30AM)", "Lobby bar (12PM-12AM)", 
                 "Room service (24/7)", "Poolside snacks"],
        "business": ["Business center", "Meeting rooms", "Printing services", 
                    "High-speed WiFi throughout"]
    },
    "policies": {
        "check-in": "3:00 PM (Early check-in available upon request)",
        "check-out": "11:00 AM (Late check-out available for fee)",
        "cancellation": "Free cancellation up to 48 hours before arrival",
        "payment": "We accept all major credit cards and cash",
        "pets": "Small pets allowed (25kg max) with $50 cleaning fee"
    },
    "location": {
        "address": "123 Luxury Avenue, Downtown, Cityville 10001",
        "transport": {
            "airport": "15km from Cityville International (20-30 min by taxi)",
            "train": "5 min walk from Central Station",
            "subway": "Direct access via Blue Line (Downtown stop)"
        },
        "attractions": {
            "nearby": ["City Museum (0.5km)", "Central Park (1km)", "Shopping District (0.3km)"],
            "distance": ["Beach - 8km", "Golf Club - 5km", "Convention Center - 2km"]
        }
    },
    "dining_options": {
        "breakfast": {
            "time": "6:30AM - 10:30AM",
            "type": "Buffet",
            "price": "$25 per adult, $12 per child",
            "options": ["Continental", "American", "Asian selections"]
        },
        "room_service": {
            "available": "24 hours",
            "menu": ["Full dinner menu until 11PM", "Limited late-night menu"]
        }
    },
    "special_offers": [
        {
            "name": "Weekend Getaway",
            "details": "Stay 2 nights, get 3rd night free (Friday-Sunday)",
            "code": "WEEKEND23"
        },
        {
            "name": "Honeymoon Package",
            "details": "Champagne, late check-out, and spa credit",
            "code": "LOVE23"
        }
    ]
}
def process_query(query):
    query = query.lower()
    
    # Room information
    if "room" in query or "stay" in query:
        if "standard" in query:
            return f"Standard Room: ${HOTEL_INFO['rooms']['standard']['price']} per night. {HOTEL_INFO['rooms']['standard']['description']}"
        elif "deluxe" in query:
            return f"Deluxe Room: ${HOTEL_INFO['rooms']['deluxe']['price']} per night. {HOTEL_INFO['rooms']['deluxe']['description']}"
        elif "suite" in query:
            return f"Suite: ${HOTEL_INFO['rooms']['suite']['price']} per night. {HOTEL_INFO['rooms']['suite']['description']}"
        else:
            room_types = ", ".join(HOTEL_INFO['rooms'].keys())
            return f"We offer these room types: {room_types}. Would you like details on any specific type?"
    
    # Pricing
    elif "price" in query or "cost" in query:
        prices = [f"{room}: ${info['price']}" for room, info in HOTEL_INFO['rooms'].items()]
        return "Our room prices per night are: " + "; ".join(prices)
    
    # Amenities
    elif "amenit" in query or "facilit" in query:
        return "Our amenities include: " + ", ".join(HOTEL_INFO['amenities'])
    
    # Check-in/out
    elif "check-in" in query or "arrival" in query:
        return f"Check-in time is {HOTEL_INFO['check-in']}"
    elif "check-out" in query or "departure" in query:
        return f"Check-out time is {HOTEL_INFO['check-out']}"
    
    # Location
    elif "where" in query or "location" in query or "address" in query:
        return f"We're located at: {HOTEL_INFO['location']}"
    
    # Greetings
    elif any(word in query for word in ["hi", "hello", "hey"]):
        return random.choice(["Hello! How can I help you with your hotel stay?", 
                            "Welcome to Cityville Hotel! What would you like to know?"])
    
    # Default response
    else:
        return "I can help with room information, pricing, amenities, and more. What would you like to know?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    response = process_query(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)