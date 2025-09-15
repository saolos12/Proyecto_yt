from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_wtf.file import FileAllowed
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repetir Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este nombre de usuario ya está en uso. Por favor, elige otro.')

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class IdeaForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    format = StringField('Formato (Ej: Tutorial, Vlog)', validators=[DataRequired()])
    tags = StringField('Etiquetas (separadas por coma)')
    status = SelectField('Estado', choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Completada', 'Completada')])
    image = FileField('Imagen (opcional)', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo se permiten imágenes (JPG, PNG, JPEG)!')]) # Campo de imagen
    submit = SubmitField('Guardar Idea')