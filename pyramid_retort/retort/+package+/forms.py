from wtforms import Form, TextField, validators

from wtforms import PasswordField


class LoginForm(Form):
    username = TextField('Username', [validators.required(), ])
    password = PasswordField('Password',
                             [validators.required()])


class RegistrationForm(LoginForm):
    password_confirm = PasswordField(
        "Confirm Password",
        [validators.required(),
         validators.EqualTo('password_confirm', message="Passwords must match")]
    )
    # reCaptcha fields for registration
    # recaptcha_challenge_field = TextField('recaptcha_challenge_field',
    #                                       [validators.required(), ])
    # recaptcha_response_field = TextField('recaptcha_response_field',
    #                                      [validators.required(), ])
