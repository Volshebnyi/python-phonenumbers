"""Auto-generated file, do not edit by hand. NF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NF = PhoneMetadata(id='NF', country_code=672, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[13]\\d{5}', possible_number_pattern='\\d{5,6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1(?:06|17|28|39)|3[012]\\d)\\d{3}', possible_number_pattern='\\d{5,6}', example_number='106609'),
    mobile=PhoneNumberDesc(national_number_pattern='38\\d{4}', possible_number_pattern='\\d{5,6}', example_number='381234'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='9(?:11|55|77)', possible_number_pattern='\\d{3}', example_number='911'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['1']),
        NumberFormat(pattern='(\\d)(\\d{5})', format=u'\\1 \\2', leading_digits_pattern=['3'])])
