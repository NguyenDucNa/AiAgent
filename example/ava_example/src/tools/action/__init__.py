
from example.ava_example.src.tools.action.misa_crm_add_opportunity import MisaCrmAddOpportunity
from example.ava_example.src.tools.action.tax_function import create_tax_declaration
from example.ava_example.src.tools.action.create_financial_report import CreateFinancialReport
from example.ava_example.src.tools.action.create_accounting_voucher import CreateAccountingVoucher
# from src.tools.action.misa_crm_search_knowledge import MisaCrmSearchKnowledge
from example.ava_example.src.tools.action.misa_crm_search_knowledge_v2 import MisaCrmSearchKnowledgeV2
from example.ava_example.src.tools.action.misa_crm_search_phonenumber import MisaCrmSearchPhoneNumber
from example.ava_example.src.tools.action.misa_crm_add_contact import MisaCrmAddContact
from example.ava_example.src.tools.action.misa_crm_search_mst import MisaCrmSearchMst
from example.ava_example.src.tools.action.misa_crm_add_customer import MisaCrmAddCustomer
from example.ava_example.src.tools.action.misa_crm_get_content_from_url import MisaCrmGetContentFromUrl
from example.ava_example.src.tools.action.misa_crm_process_opportunity_lead import MisaCrmProcessOpportunityLead
from example.ava_example.src.tools.action.misa_crm_action_success import MisaCrmActionSuccess
from example.ava_example.src.tools.action.misa_crm_get_product_info import MisaCrmGetProductInfo

action_tools = [
    create_tax_declaration,
    CreateFinancialReport,
    CreateAccountingVoucher,
    # MisaCrmSearchKnowledge,
    MisaCrmSearchPhoneNumber,
    # MisaCrmAddContact,
    MisaCrmSearchMst,
    MisaCrmAddCustomer,
    MisaCrmAddOpportunity,
    MisaCrmSearchKnowledgeV2,
    MisaCrmGetContentFromUrl,
    MisaCrmProcessOpportunityLead,
    MisaCrmActionSuccess,
    MisaCrmGetProductInfo,
]
