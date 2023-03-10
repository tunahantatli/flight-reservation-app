from rest_framework import serializers
from .models import Flight, Reservation, Passenger


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


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True, required = False)
    flight = serializers.StringRelatedField()
    flight_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Reservation
        fields = ("id", "flight", "flight_id", "user", "passenger")

    def create(self, validated_data):
        passenger_data = validated_data.pop("passenger")
        validated_data["user_id"] = self.context["request"].user.id
        reservation = Reservation.objects.create(**validated_data)  # create reservation object
        
        # create passenger objects
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas) # is spacial for many2many field 
        
        reservation.save()
        return reservation
            
# serializer for Staff Users
class StaffSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(many=True, read_only=True)
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "edt",
            "reservation",
        )