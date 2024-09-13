import unittest
import logging
from io import StringIO

from logger import Logger  # Assuming logger.py is in the same directory

class TestLogger(unittest.TestCase):
    
    def setUp(self):
        self.logger = Logger()
        self.log_output = StringIO()
        self.handler = logging.StreamHandler(self.log_output)
        formatter = logging.Formatter(Logger.BASIC_FORMAT)
        self.handler.setFormatter(formatter)
        self.logger.logger.addHandler(self.handler)

    def tearDown(self):
        self.logger.logger.removeHandler(self.handler)
        self.log_output.close()

    def test_info(self):
        self.logger.info("Testing info log")
        log_message = self.log_output.getvalue().strip()
        self.assertTrue(log_message.endswith("👉 Testing info log"))

    def test_warning(self):
        self.logger.warning("Testing warning log")
        log_message = self.log_output.getvalue().strip()
        self.assertTrue(log_message.endswith("😥 Testing warning log"))

    def test_error(self):
        self.logger.error("Testing error log")
        log_message = self.log_output.getvalue().strip()
        self.assertTrue(log_message.endswith("😡 Testing error log"))

    def test_debug(self):
        self.logger.debug("Testing debug log")
        log_message = self.log_output.getvalue().strip()
        self.assertTrue(log_message.endswith("👀 Testing debug log"))

    def test_critical(self):
        self.logger.critical("Testing critical log")
        log_message = self.log_output.getvalue().strip()
        self.assertTrue(log_message.endswith("😱 Testing critical log"))

    def test_exception(self):
        try:
            raise ValueError("Testing exception log")
        except ValueError:
            self.logger.exception("An error occurred")
        log_message = self.log_output.getvalue().strip()
        self.assertTrue(log_message.endswith("💥 An error occurred"))

if __name__ == "__main__":
    unittest.main()import unittest
import logging
from io import StringIO

from logger import Logger  # Adjust the import based on your project structure

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()
        self.log_stream = StringIO()
        self.logger.console_handler.stream = self.log_stream

    def test_info_logging(self):
        self.logger.info("Test info message")
        self.assertIn("👉 Test info message", self.log_stream.getvalue())

    def test_warning_logging(self):
        self.logger.warning("Test warning message")
        self.assertIn("😥 Test warning message", self.log_stream.getvalue())

    def test_error_logging(self):
        self.logger.error("Test error message")
        self.assertIn("😡 Test error message", self.log_stream.getvalue())

    def test_debug_logging(self):
        self.logger.debug("Test debug message")
        self.assertIn("👀 Test debug message", self.log_stream.getvalue())

    def test_critical_logging(self):
        self.logger.critical("Test critical message")
        self.assertIn("😱 Test critical message", self.log_stream.getvalue())

    def test_exception_logging(self):
        with self.assertRaises(Exception):
            raise Exception("Test exception")
        self.logger.exception("Caught an exception")
        self.assertIn("💥 Caught an exception", self.log_stream.getvalue())

if __name__ == '__main__':
    unittest.main()