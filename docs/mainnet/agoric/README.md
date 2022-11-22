# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

Website: [https://agoric.com](https://agoric.com)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@agoric.rpc.kjnodes.com:27656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:27659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (11)
```
peers="1cbe5f5c77610bb6568332e026a3b516edeb0121@65.21.234.47:21156,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,e759de7a872eff293ab1316a0745eb5fdd5614f3@88.217.142.187:26656,576e4e90b785fb16c129a0141b57342e51fd61b4@193.176.85.156:26656,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,1c9a5b1d34b9e6f184b2dcb18ed068cf0c282e50@51.79.98.163:26656,80e8d307c7b1e7027645a0054ba3e08addfa83b2@88.99.217.85:26656,c2a993a5c8905ee1be929352654b6a49ecf0726a@195.3.222.163:26656,3445f4b73fdc63a1bf78c638afb122f69cb0bd4a@157.90.208.234:26656,15f63de308337b66d8918ffaa74c6e956991bee9@138.201.120.161:28357,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
