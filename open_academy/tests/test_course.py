from psycopg2.errors import CheckViolation
from psycopg2.errors import UniqueViolation

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


class TestOpenAcademyCourse(TransactionCase):
    def setUp(self):
        super().setUp()
        self.course = self.env['openacademy.course']

    def get_course_values(self, course_name, course_description,
                          course_responsible):
        course_id = self.course.create({
            'title': course_name,
            'description': course_description,
            'responsible_user_id': course_responsible,
        })
        return course_id

    @mute_logger('odoo.sql_db')
    def test_01_same_name_description(self):
        """Test to valid constraid when name is the same value than
        description.
        """
        with self.assertRaisesRegex(
            CheckViolation,
            'new row for relation "openacademy_course" violates'
            ' check constraint "openacademy_course_name_description_check"'
        ):
            self.get_course_values('101', '101', None)

    @mute_logger('odoo.sql_db')  
    def test_02_two_courses_same_name(self):
        """ Test to create two courses with same name
        to raise constraint of unique name. """

        self.get_course_values('test1', 'test_desciption', None)
        with self.assertRaisesRegex(
            UniqueViolation,
            'duplicate key value violates unique constraint'
            ' "openacademy_course_name_unique"'
        ):
            self.get_course_values('test1', 'test_desciption', None)

    def test_03_duplicate_course(self):
        """ Test to duplicate a course a and check that work fine! """
        course = self.env.ref('open_academy.odoo_course')
        course.copy()