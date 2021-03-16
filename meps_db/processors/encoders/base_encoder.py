from datetime import date


class BaseEncoder:
    """ Base Encoder Class. Contains functions shared across all children encoder classes """

    @staticmethod
    def generate_date(year_str, month_str):
        """ Takes a year string and a month str. If both values are valid return a date object fixed on the first of
        the month, otherwise returns None """

        if month_str in {"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"} and year_str not in {
            "-015",
            "-15",
            "-009",
            "-09",
            "-9",
            "-008",
            "-08",
            "-8",
            "-007",
            "-07",
            "-7",
        }:

            return date(year=int(year_str), month=int(month_str), day=1)

    @staticmethod
    def order_histories(respondents):
        """ Takes a dictionary of respondents. Each respondent should have a list of events that contain a date field.
        For each respondent orders the events from earliest to latest. Forces missing dates to the end of the list. 
        Return the dictionary. """

        for resp_dict in respondents.values():
            resp_dict = sorted(resp_dict, key=lambda event: (event["date"] is None, event["date"]))

        return respondents
