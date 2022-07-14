"""This module contains sub utilities used across the codebase."""

from apis.api_utils.error_logs import logging_error


def format_phone_no_to_plus234(phone_number):
    """Format Phone number to +234xxx"""
    try:
        # if phone number starts with Zero(0) and the length is 11, then replace Zero(0) with '+234'
        if phone_number.startswith('0') and len(phone_number) == 11:
            # setting replace() third arg (count) to 1 so only the first occurrence of '0' is replaced
            ph_no = phone_number.replace('0', '+234', 1)
            return ph_no

        # if phone number starts with '234' and the length is 13, then replace '234' with '+234'
        elif phone_number.startswith('234') and len(phone_number) == 13:
            # setting replace() third arg (count) to 1 so only the first occurrence of '234' is replaced
            ph_no = phone_number.replace('234', '+234', 1)
            return ph_no

        # if phone number starts with '+234' and the length is 14, then return the number.
        elif phone_number.startswith('+234') and len(phone_number) == 14:
            return phone_number

        # If any of the above conditions do not match return Invalid Phone Number
        else:
            return 'Invalid Phone number'
    except Exception as e:
        logging_error.error('format_phone_no_to_plus234@Error')
        logging_error.error(e)
        return None


def format_phone_no_to_234(phone_number):
    """Format Phone number to 234xxx"""
    try:
        # if phone number starts with Zero(0) and the length is 11, then replace Zero(0) with '234'
        if phone_number.startswith('0') and len(phone_number) == 11:
            # setting replace() third arg (count) to 1 so only the first occurrence of '0' is replaced
            ph_no = phone_number.replace('0', '234', 1)
            return ph_no

        # if phone number starts with '+234' and the length is 14, then replace '+234' with '234'
        elif phone_number.startswith('+234') and len(phone_number) == 14:
            # setting replace() third arg (count) to 1 so only the first occurrence of '+234' is replaced
            ph_no = phone_number.replace('+234', '234', 1)
            return ph_no

        # if phone number starts with '234' and the length is 13, then return the number.
        elif phone_number.startswith('234') and len(phone_number) == 13:
            return phone_number

        # If any of the above conditions do not match return Invalid Phone Number
        else:
            return 'Invalid Phone number'
    except Exception as e:
        logging_error.error('format_phone_no_to_234@Error')
        logging_error.error(e)
        return None
