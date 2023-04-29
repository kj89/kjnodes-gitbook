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
peers="b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,6f473f7156b9e0a460f5ab9d5b8bba2412058974@93.159.134.156:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,213857e741833d17275ea559bb2d0342398cec99@35.245.206.45:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,e3f76b923d03fc99510b31049144e22d8f0f0587@65.108.193.249:2010,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,241b17dba97a2ed3c3747d12781fb86c9706e2d4@89.58.27.86:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,daa6d8314246ad65037a48ec2e2266eeea9d46f8@154.53.63.50:26656,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,1b5a5b6518d3cb30a0d49cbd74a45dd4cbab130d@18.138.176.63:26656,53b3651680ec3482d736808cbb3035940107f8ab@82.100.58.119:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656,62da9d5bc8768e84400941a1195f47bac90fcf97@35.210.106.206:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,3ce30fdd489fa87b6465141cc56b48e5a22fe8e1@154.53.41.185:10093,505f4467926cdad29932c44dc5ea7a5da6982f48@176.9.101.44:26656,61afb0f37c02031f285f6b27ead2a3e7a97cc28a@35.212.34.104:26656,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,7abab0475a506ed3b9ab2ad40948bfe53b797e13@128.199.128.15:26090,2b4b4e3b376af4becd60865cc71f81c7e148375c@83.125.137.151:26656,9c116194f25fd0d146019f171ef0f49904dcc586@167.86.98.230:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,9d7d9ba2b9bc1c805a24413fcfdc75010d52dd61@159.89.101.239:26090"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
