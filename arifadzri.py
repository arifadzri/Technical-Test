import unittest
import mysql.connector

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.conn = mysql.connector.connect(user='user', password='password', host='localhost', database='database_name')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_price(self):
        # Tes harga yang tersimpan di table booking dengan harga yang seharusnya
        query = "SELECT price FROM booking WHERE booking_id = 'BK/000001'"
        self.cursor.execute(query)
        actual_price = self.cursor.fetchone()[0]
        expected_price = 1000000
        self.assertEqual(actual_price, expected_price, "Harga yang tersimpan di tabel booking tidak sesuai dengan harga yang seharusnya.")

    def test_double_booking(self):
        # Tes double booking pada waktu dan tanggal yang sama
        query = "SELECT COUNT(*) FROM booking WHERE venue_id = 15 AND date = '2022-12-10' AND ((start_time BETWEEN '09:00:00' AND '11:00:00') OR (end_time BETWEEN '09:00:00' AND '11:00:00'))"
        self.cursor.execute(query)
        actual_count = self.cursor.fetchone()[0]
        expected_count = 1
        self.assertEqual(actual_count, expected_count, "Terjadi double booking pada waktu dan tanggal yang sama.")

if __name__ == '__main__':
    unittest.main()
