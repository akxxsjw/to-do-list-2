import psycopg2
from psycopg2 import sql

db_params = {
    'dbname': 'hotel_booking_db',
    'user': 'postgres',  
    'password': '2107', 
    'host': 'localhost',
    'port': 5432
}

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    print("Подключение к базе данных успешно выполнено")

    def insert_data(query, data):
        try:
            cursor.execute(query, data)
            conn.commit()
            print("Данные успешно вставлены")
        except psycopg2.Error as e:
            print(f"Ошибка при вставке данных: {e}")
            conn.rollback()

    insert_query = """
        INSERT INTO Rooms (Name, Type, PricePerNight, Capacity, Description)
        VALUES (%s, %s, %s, %s, %s)
    """
    rooms_data = [
        ("Deluxe Room", "Deluxe", 150.00, 2, "Spacious room with a king-size bed and a beautiful view."),
        ("Standard Room", "Standard", 100.00, 2, "Comfortable room with a double bed."),
        ("Family Suite", "Suite", 250.00, 4, "Large suite with two bedrooms and a living area."),
        ("Single Room", "Single", 80.00, 1, "Cozy room perfect for solo travelers."),
        ("Presidential Suite", "Suite", 500.00, 5, "Luxurious suite with multiple rooms and top amenities.")
    ]
    for room in rooms_data:
        insert_data(insert_query, room)

    insert_query = """
        INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
        VALUES (%s, %s, %s, %s, %s)
    """
    clients_data = [
        ("John", "Doe", "john.doe@example.com", "+1234567890", "123 Main St, Anytown, USA"),
        ("Jane", "Smith", "jane.smith@example.com", "+0987654321", "456 Elm St, Othertown, USA"),
        ("Emily", "Johnson", "emily.johnson@example.com", "+1122334455", "789 Oak St, Sometown, USA"),
        ("Michael", "Brown", "michael.brown@example.com", "+6677889900", "101 Maple St, Anothertown, USA"),
        ("Laura", "Wilson", "laura.wilson@example.com", "+2233445566", "202 Birch St, Someothertown, USA")
    ]
    for client in clients_data:
        insert_data(insert_query, client)

    insert_query = """
        INSERT INTO Bookings (ClientID, RoomID, CheckInDate, CheckOutDate, TotalAmount)
        VALUES (%s, %s, %s, %s, %s)
    """
    bookings_data = [
        (1, 1, "2024-08-01", "2024-08-05", 600.00),
        (2, 2, "2024-08-10", "2024-08-15", 500.00),
        (3, 3, "2024-08-15", "2024-08-20", 1250.00),
        (4, 4, "2024-08-05", "2024-08-07", 160.00),
        (5, 5, "2024-08-20", "2024-08-25", 2500.00)
    ]
    for booking in bookings_data:
        insert_data(insert_query, booking)

    insert_query = """
        INSERT INTO Payments (BookingID, PaymentDate, Amount, PaymentMethod)
        VALUES (%s, %s, %s, %s)
    """
    payments_data = [
        (1, "2024-08-01", 600.00, "Credit Card"),
        (2, "2024-08-10", 500.00, "Debit Card"),
        (3, "2024-08-15", 1250.00, "Bank Transfer"),
        (4, "2024-08-05", 160.00, "Cash"),
        (5, "2024-08-20", 2500.00, "Credit Card")
    ]
    for payment in payments_data:
        insert_data(insert_query, payment)

    cursor.close()
    conn.close()
    print("Соединение закрыто")

except psycopg2.Error as e:
    print(f"Ошибка при подключении к базе данных: {e}")