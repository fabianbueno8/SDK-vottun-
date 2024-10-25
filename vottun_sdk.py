
import requests

class VottunSDK:
    def __init__(self, api_key, app_id, base_url):
        self.api_key = api_key
        self.app_id = app_id
        self.base_url = base_url
        self.headers = {
            "x-application-vkn": self.app_id,
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def deploy_erc721_contract(self, contract_name, symbol, blockchain_network, gas_limit):
        url = f"{self.base_url}/erc721/deploy"
        payload = {
            "name": contract_name,
            "symbol": symbol,
            "blockchainNetwork": blockchain_network,
            "gasLimit": gas_limit
        }
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json() if response.status_code == 201 else (response.status_code, response.text)

    def mint_nft(self, contract_address, recipient_address, ipfs_uri, ipfs_hash, blockchain_network, royalty_percentage):
        url = f"{self.base_url}/vottun/mint"
        payload = {
            "contractAddress": contract_address,
            "recipientAddress": recipient_address,
            "ipfsUri": ipfs_uri,
            "ipfsHash": ipfs_hash,
            "blockchainNetwork": blockchain_network,
            "royaltyPercentage": royalty_percentage
        }
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json() if response.status_code == 200 else (response.status_code, response.text)

    def transfer_nft(self, contract_address, from_address, to_address, token_id, price, blockchain_network):
        url = f"{self.base_url}/vottun/transfer"
        payload = {
            "contractAddress": contract_address,
            "from": from_address,
            "to": to_address,
            "tokenId": token_id,
            "price": price,
            "blockchainNetwork": blockchain_network
        }
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json() if response.status_code == 200 else (response.status_code, response.text)
        
    def upload_file_to_ipfs(self, file_name, file_path):
        url = f"{self.base_url}/file/upload"
        files = {'file': open(file_path, 'rb')}
        payload = {'fileName': file_name}
        response = requests.post(url, headers=self.headers, files=files, data=payload)
        return response.json() if response.status_code == 201 else (response.status_code, response.text)
