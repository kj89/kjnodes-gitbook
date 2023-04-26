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
peers="aa61bc0e8a42eda6ac1276c4279941714a4a38f4@88.99.70.38:26656,db7850e8e9bef0568904b7d5bcaec813e8e3d295@34.27.227.166:26656,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,51c49b57b371e3645de715e0034236a8bd61965e@35.221.229.109:26656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,62da9d5bc8768e84400941a1195f47bac90fcf97@35.210.106.206:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,d53ecee926a66a4a6b1858004f5f22f77faca036@3.69.52.20:26656,11de8a73123ce854241cfa9687921c544b83d5d9@141.94.100.228:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656,e3f76b923d03fc99510b31049144e22d8f0f0587@65.108.193.249:2010,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,89fb1dc652ced3b44f80e7427747548e93c61a86@52.77.248.139:26656,3ce30fdd489fa87b6465141cc56b48e5a22fe8e1@154.53.41.185:10093,64148c47e1424173e3dcf90ab90bf196c2971b15@88.218.224.118:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656,1733aef88702bd8326bea0e1dc403d3dbb6f5d8a@158.247.202.33:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,cfd785a4224c7940e9a10f6c1ab24c343e923bec@164.68.107.188:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.1:26656,cd372322e563832871672be23d8303508d4385a3@139.59.8.48:26090"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
