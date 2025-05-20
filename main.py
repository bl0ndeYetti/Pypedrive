import os
from dotenv import load_dotenv
from pipedrive_client.client import PipedriveV2Client

def main():
    # Load environment variables
    load_dotenv()
    
    # Get credentials from environment variables
    api_token = os.getenv('PIPEDRIVE_API_KEY')
    company_domain = os.getenv('PIPEDRIVE_COMPANY_DOMAIN')
    company_subdomain = os.getenv('PIPEDRIVE_COMPANY_SUBDOMAIN')
    
    if not api_token:
        raise ValueError("API Key Missing")
    
    if not company_domain and not company_subdomain:
        raise ValueError("Company Domain or Subdomain Missing. One is required.")
    
    # Initialize Pipedrive client
    client = PipedriveV2Client(api_token=api_token, company_domain=company_domain, company_subdomain=company_subdomain)
    
    # Example usage (uncomment and modify as needed):
    deals = client.deals.get_details(123)
    #print(deals)

if __name__ == '__main__':
    main()
