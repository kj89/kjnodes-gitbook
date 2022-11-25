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

**live-peers** (10)
```
peers="71bd0265037393f31ee9947a8e32fa494e51b637@135.181.218.98:26656,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,bb257b3a0829910477a3845430b6b1f7eb2b4235@34.146.189.78:26656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,abc62ded9142361bd9832282242a53611785ffcd@51.81.109.109:26656,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,b37f20e94ab5164cfcc25c3ba5816ba5a272a22c@46.4.116.21:26656,d48697ba840d046b453846fc55d9432d1c537b56@95.217.117.83:26656,1dfd1a8be38d892fa485e1b417bcf5f225b3f638@185.210.219.66:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
