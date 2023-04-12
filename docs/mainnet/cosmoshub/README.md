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
peers="e726816f42831689eab9378d5d577f1d06d25716@23.88.22.1:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,b0ac7f1485eedfc063af251fe12d93a68a22131d@65.108.137.38:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,9d048653fa4d98e6c0760ed0c54ad2d257ba46df@65.108.137.34:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,61afb0f37c02031f285f6b27ead2a3e7a97cc28a@35.212.34.104:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,7abab0475a506ed3b9ab2ad40948bfe53b797e13@128.199.128.15:26090,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,9c116194f25fd0d146019f171ef0f49904dcc586@167.86.98.230:26656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,460967e46cc013e5e3eb365c1a8d271b0662549f@35.208.242.182:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,9d7d9ba2b9bc1c805a24413fcfdc75010d52dd61@159.89.101.239:26090,4ddba29a7dfa740a4edeb5c620c963f67f951e1d@5.9.72.212:2000,a052e770d7cfa09b79f19c7ab3c6c932729a8cad@52.19.163.186:26656,eebc7a0257c91306b38fb42924b9292d6dd2951c@51.79.176.202:26656,d25bd1bea59f3a96bcb98b6da6f5cf874ac59179@54.236.120.119:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
