import os
from dotenv import load_dotenv
from pipedrive_client.client import PipedriveV2Client

def main():
    # Load environment variables
    load_dotenv()
    
    # Get credentials from environment variables
    api_token = os.getenv('PD_API_TOKEN')
    company_domain = '' #'mycompany' from mycompany.pipedrive.com
    
    if not api_token or not company_domain:
        raise ValueError("Please set PD_API_TOKEN and PD_COMPANY_DOMAIN in your .env file")
    
    # Initialize Pipedrive client
    client = PipedriveV2Client(api_token=api_token, company_domain=company_domain)
    
    # Example usage (uncomment and modify as needed):
    deals = client.deals.get_details(123)
    #print(deals)

if __name__ == '__main__':
    main()
