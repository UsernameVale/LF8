import unittest
import psutil
from server_monitoring import check_system, send_alert

class TestServerMonitoring(unittest.TestCase):

    def test_cpu_usage(self):
        """Testet, ob die CPU-Auslastung als Zahl zurückgegeben wird."""
        cpu_usage = psutil.cpu_percent(interval=1)
        self.assertIsInstance(cpu_usage, float)

    def test_memory_usage(self):
        """Testet, ob die RAM-Auslastung als Zahl zurückgegeben wird."""
        memory_usage = psutil.virtual_memory().percent
        self.assertIsInstance(memory_usage, float)

    def test_disk_usage(self):
        """Testet, ob die Festplattenauslastung als Zahl zurückgegeben wird."""
        disk_usage = psutil.disk_usage('/').percent
        self.assertIsInstance(disk_usage, float)

    def test_alert_function(self):
        """Testet, ob die Alarmfunktion ohne Fehler aufgerufen werden kann."""
        try:
            send_alert("Test-Alarm", "Dies ist eine Testnachricht")
            result = True
        except Exception as e:
            result = False
        self.assertTrue(result, "Die Alarmfunktion hat einen Fehler.")

if __name__ == "__main__":
    unittest.main()
