# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:13490

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:13456
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:13459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (30)
```bash
peers="fd4d63438f9e69da0220c7d97bc4cead5e12fcdd@195.201.63.87:26666,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656,7abab0475a506ed3b9ab2ad40948bfe53b797e13@128.199.128.15:26090,ec39fae6c161dea476d50bbaffa1ca0e7fbcb21f@65.21.200.7:1100,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,7dd34d8d3880bc48eff3e47b941d06bd1941a962@93.115.25.106:26656,6f473f7156b9e0a460f5ab9d5b8bba2412058974@93.159.134.156:36656,1b5a5b6518d3cb30a0d49cbd74a45dd4cbab130d@18.138.176.63:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,62da9d5bc8768e84400941a1195f47bac90fcf97@35.210.106.206:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,11de8a73123ce854241cfa9687921c544b83d5d9@141.94.100.228:26656,53b3651680ec3482d736808cbb3035940107f8ab@82.100.58.119:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,89757803f40da51678451735445ad40d5b15e059@169.155.168.135:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,72829b78b38408b03793ed389b9f16596b82c306@146.59.81.92:26656,505f4467926cdad29932c44dc5ea7a5da6982f48@176.9.101.44:26656,61afb0f37c02031f285f6b27ead2a3e7a97cc28a@35.212.34.104:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,51c49b57b371e3645de715e0034236a8bd61965e@35.221.229.109:26656,241b17dba97a2ed3c3747d12781fb86c9706e2d4@89.58.27.86:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
