from django.utils.text import slugify

def upload_institute_staff_image_to(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = "%s.%s" % (slugify(instance.institute), ext)

    return 'institute/staff_image/{}'.format(
        new_filename
    )

def upload_institute_logo_to(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = "%s.%s" % (slugify(instance.name), ext)

    return 'institute/logo/{}'.format(
        new_filename
    )


def upload_institute_cover_image_to(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = "%s.%s" % (slugify(instance.name), ext)

    return 'institute/cover_image/{}'.format(
        new_filename
    )