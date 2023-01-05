<<<<<<< HEAD
import unittest
import otp_v1 as o

class TestOtp(unittest.TestCase):
    def test_email(self):
        self.assertIn("@",o.userEmail,"Invalid Email")
        self.assertIn(".com",o.userEmail, "Invalid Email")
    def test_otpLength(self):
        otp = o.generateOtp
        self.assertGreaterEqual(len(otp),6,"Length of otp should be greater or equal to 6")

if __name__ == '__main__':
   unittest.main()

=======
import unittest
import otp_v1 as o

class TestOtp(unittest.TestCase):
    def test_email(self):
        self.assertIn("@",o.userEmail,"Invalid Email")
        self.assertIn(".com",o.userEmail, "Invalid Email")
    def test_otpLength(self):
        otp = o.generateOtp
        self.assertGreaterEqual(len(otp),6,"Length of otp should be greater or equal to 6")

if __name__ == '__main__':
   unittest.main()

>>>>>>> 7605d657ce8a0aa41d869108fb2e0b39c7a3f8cc
