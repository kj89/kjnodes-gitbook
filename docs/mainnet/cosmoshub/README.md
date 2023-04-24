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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,e3f76b923d03fc99510b31049144e22d8f0f0587@65.108.193.249:2010,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,82aa1d7e83e7f675f6c2cb043e2b0ecfeb72d652@54.159.132.131:26656,7dd34d8d3880bc48eff3e47b941d06bd1941a962@93.115.25.106:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,2286eeee09fcf37e768dfffc0db8c821b9231b7b@204.16.244.78:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,f88e78f7448eeb8d0cdf465aed3308f52780f1f2@44.195.76.177:26656,b79e1d3a621bdafd3a8d9a49dff8f4737d0bedc9@52.203.105.100:26656,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,5b143d463427d9ad0b621f97c0b8933643e293da@35.212.90.144:26656,4ebf074e8b4a24438bd0bd503b62b4728dfb8eae@35.212.101.35:26656,a7f87b0df31316ba270f737e2cce6c100e1549d8@202.61.228.55:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,d484b416598b98d3cd7f4dfb6faa30d75ee9d545@188.214.129.233:26656,3334bb086be9ab0dba3a34331555624a7354a6ab@159.203.187.36:26090,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
