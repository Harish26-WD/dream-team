from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Department, Designation

# class CompanyForm(FlaskForm):
#     """
#     Form for admin to add or edit a company
#     """
#     name = StringField('Name', validators=[DataRequired()])
#     description = StringField('Description', validators=[DataRequired()])
#     submit = SubmitField('Submit')

class DepartmentForm(FlaskForm):
	"""
	Form for admin to add or edit a department
	"""
	name = StringField('Name', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Submit')


class DesignationForm(FlaskForm):
    """
    Form for admin to add or edit a Designation
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    #company = QuerySelectField(query_factory=lambda: Company.query.all(),
    #                               get_label="name")
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    designation = QuerySelectField(query_factory=lambda: Designation.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')