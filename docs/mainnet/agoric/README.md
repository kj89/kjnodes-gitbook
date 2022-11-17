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
peers="e5970b2440e4083c7d74b51c8991ac9fd0f54dc0@162.55.132.48:15634,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,abc62ded9142361bd9832282242a53611785ffcd@51.81.109.109:26656,db14f5d2281c82b89ea32538eaa838cfcc0d9a7e@15.235.9.223:26656,766536f9ada683a9272c5305398ca7f82c9e7d43@35.215.60.158:26656,1dfd1a8be38d892fa485e1b417bcf5f225b3f638@185.210.219.66:26656,e759de7a872eff293ab1316a0745eb5fdd5614f3@88.217.142.187:26656,d7e0eedf5756b8c085104fb76c069ba3506f2183@80.64.208.64:26656,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
