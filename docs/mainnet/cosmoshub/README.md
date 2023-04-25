# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:34090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:34656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (30)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,fd4d63438f9e69da0220c7d97bc4cead5e12fcdd@195.201.63.87:26666,2286eeee09fcf37e768dfffc0db8c821b9231b7b@204.16.244.78:26656,222385f3ce7f55f9c01c23f2ee340ed9548b18fa@35.222.169.98:26656,c0e99d6797507c8ba3e97afda4400c9e9d986495@148.251.132.176:26656,e3f76b923d03fc99510b31049144e22d8f0f0587@65.108.193.249:2010,7dd34d8d3880bc48eff3e47b941d06bd1941a962@93.115.25.106:26656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,6a45e3655209dacddedf735a898ccfcae085abec@65.109.182.72:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,322efd4fdc72a189a2fc8b2b597927831df2bbed@128.0.51.9:26656,f6f5d71d0b9e29f2b86f47ce0d62b059b53009fc@74.118.143.238:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,11de8a73123ce854241cfa9687921c544b83d5d9@141.94.100.228:26656,61afb0f37c02031f285f6b27ead2a3e7a97cc28a@35.212.34.104:26656,803abd0b6b0478ab7f7e38dbda89902ca67f8778@65.21.90.137:11956,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,e2b3cba06a28ff811e72f23d0e025c9354ed680d@35.206.163.4:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,3c99aba53d77d9b86efb9a7a74037761360086e6@18.139.147.9:26656,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
