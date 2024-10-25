# Vottun Python SDK

Este SDK permite interactuar con las APIs de Vottun para realizar operaciones relacionadas con NFTs y contratos ERC721 en diversas blockchain.

### Inicialización

Primero, inicializa el SDK proporcionando tu API Key, Application ID y la URL base de las APIs de Vottun:

```python
VottunSDK

api_key = "tu_api_key"
app_id = "tu_app_id"
base_url = "https://api.vottun.com"

sdk = VottunSDK(api_key, app_id, base_url)
```

### Desplegar un contrato ERC721

Puedes desplegar un nuevo contrato ERC721 en la blockchain especificada:

```python
response = sdk.deploy_erc721_contract("MiNFT", "MNFT", 80001, 3000000)
print(response)
```

### Mint de NFT

Para acuñar (mint) un nuevo NFT:

```python
response = sdk.mint_nft("0xFde579C45Fa6CEA5f248fE1c0f58C8cCe7082DB7", "0x7D2ECffe9D8e92757BC96BdA1348945bf109df5A", 
                        "https://ipfsgw-pre.vottun.tech/ipfs/QmQcKr9kgSia7Ek3USr28YrTxoGWdbQQ6pTrjpk5x8BFMV", 
                        "QmQcKr9kgSia7Ek3USr28YrTxoGWdbQQ6pTrjpk5x8BFMV", 43113, 10)
print(response)
```

### Transferir NFT

Para transferir un NFT de una dirección a otra:

```python
response = sdk.transfer_nft("0x88B32cCB066623B3125E749302A0e64Ce117eecD", 
                            "0x532af0D1233270c8E85357eF4452C7e9d50038D9", 
                            "0x09Ad4223BB91461B1AD112F2Dc71C3548A638474", 
                            9, 25000000000000000, 80001)
print(response)
```

### Subir archivos a IPFS

Para subir un archivo a IPFS a través de Vottun:

```python
response = sdk.upload_file_to_ipfs("demo1", "/ruta/al/archivo")
print(response)
```

## Notas

- Asegúrate de tener una API Key válida y de haber configurado correctamente la autenticación.
- Esta es una implementación básica. Puedes expandirla según tus necesidades o agregar más e
