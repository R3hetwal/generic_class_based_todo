from django.test import TestCase
from django.contrib.auth import get_user_model #We have Custom User Model

# Create your tests here.
class UserAccountTests(TestCase):

    def test_name_superuser(self):
        db = get_user_model()
        # User testing database and create the data
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'username', 'firstname', 'password'
        )
        self.assertEqual(super_user.email, 'testuser@super.com')#This is the correct data  that should match with data from super_user
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "username") #must be returned if user is created

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email = 'testuser@super.com', 
                user_name = 'username1', 
                first_name = 'firstname', 
                password = 'password', 
                is_superuser = False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email = 'testuser@super.com', 
                user_name = 'username1', 
                first_name = 'firstname', 
                password = 'password', 
                is_staff = False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email = '', 
                user_name = 'username1', 
                first_name = 'firstname', 
                password = 'password', 
                is_superuser = False
            )


    def test_name_user(self):
        db = get_user_model()
        # User testing database and create the data
        super_user = db.objects.create_user(
            'testuser@user.com', 'username', 'firstname', 'password'
        )
    
        self.assertEqual(super_user.email, 'testuser@user.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertFalse(super_user.is_superuser)
        self.assertFalse(super_user.is_staff)
        self.assertFalse(super_user.is_active) #user must be active to login to the system
        self.assertEqual(str(super_user), "username") #must be returned if user is created


        with self.assertRaises(ValueError):
            db.objects.create_user(
                email = '', 
                user_name = 'admin', 
                first_name = 'ad', 
                password = 'password', 
            )

