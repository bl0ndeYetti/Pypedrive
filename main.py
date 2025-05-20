import os
from dotenv import load_dotenv
from pipedrive_client.client import PipedriveClient

def main():
    # Load environment variables
    load_dotenv()
    
    # Get credentials from environment variables
    api_token = os.getenv('PIPEDRIVE_API_KEY')
    company_domain = os.getenv('PIPEDRIVE_COMPANY_DOMAIN')
    
    if not api_token:
        raise ValueError("API Key Missing")
    
    if not company_domain:
        raise ValueError("Company domain missing")
    
    # Initialize Pipedrive client
    client = PipedriveClient(api_token=api_token, company_domain=company_domain)
    
    # Example usage (uncomment and modify as needed):
    deals = client.deals.get_details(123)
    #print(deals)

if __name__ == '__main__':
    main()

