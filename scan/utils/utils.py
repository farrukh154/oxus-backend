from django.core.exceptions import ValidationError
from pypdf import PdfReader, PdfWriter
from django.utils.translation import gettext_lazy as _



def only_pdf(value):
    if isinstance(value, str):
        if not value.lower().endswith('.pdf'):
            raise ValidationError(_('Only PDF files.'))
    else:
        if not value.name.lower().endswith('.pdf'):
            raise ValidationError(_('Only PDF files.'))

def compress_pdf(file_path):
    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=10)

    with open(file_path, "wb") as f:
        writer.write(f)