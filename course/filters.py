from course.models import CourseReview
import django_filters 
from django_filters import OrderingFilter


class CourseReviewFilter(django_filters.FilterSet):

    o = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('courseDepartment', 'courseDepartment'),
            ('courseNumber', 'courseNumber'),
        ),

        # labels do not need to retain order
        field_labels={
            'courseDepartment': 'course department',
        }
    )

    class Meta:
        model = CourseReview
        fields = ['courseDepartment','courseNumber', 'reviewId','instructorId', 'courseReviewTagId', 'review', 'reviewDate' ]
