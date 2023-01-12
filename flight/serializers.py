from rest_framework import serializers
from .models import Flight, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "edt",
        )

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'