from enum import Enum


class DateType(Enum):
    TODAY =  "today"
    THIS_WEEK = "this_week"
    THIS_SESSION = "this_session"
    THIS_MONTH = "this_month"
    THIS_YEAR = "this_year"

class Gender(Enum):
    MALE =  "Nam"
    FEMALE = "Nữ"

class Honorific(Enum):
    MALE =  "Anh"
    FEMALE = "Chị"

class RecipientAddress(Enum):
    MALE = "anh"
    FEMALE = "chị"
    YOUNGER = "em"
    FRIEND = "bạn"

class NodeName(Enum):
    BIRTHDAY = "birthday"
    OPENAI = "openai"
    COHERE = "cohere"
    LLAMA3 = "llama3"

class AgentCode(Enum):
    TEXT_GENERATE = "avagentext"
    TRANSLATION = "avatranslation"
    DOC_SUMMARY = "avadocsummary"
    EXTRACT_FILE = "avaextractfile"