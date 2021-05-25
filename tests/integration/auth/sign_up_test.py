from flask.wrappers import Response
from tests.base_test import BaseTest, db
from website.models import User
from flask_login import current_user

class TestSignUp(BaseTest):

    # test signing up user successfully 
    def test_sign_up_post_success(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/sign-up',
                                    data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234', password2='pass1234'),
                                    follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created', response.data)
            # assert that user is logged in 
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            self.assertIn(b'Notes', response.data)
