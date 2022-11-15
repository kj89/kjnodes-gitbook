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
peers="03c7d68a1433dde6db1acbbdf98712609843cc8f@161.97.187.189:36656,c2a993a5c8905ee1be929352654b6a49ecf0726a@195.3.222.163:26656,576e4e90b785fb16c129a0141b57342e51fd61b4@193.176.85.156:26656,e07945e91c6f9936e3dee73afd49d904be320c99@128.0.51.3:26656,abc62ded9142361bd9832282242a53611785ffcd@51.81.109.109:26656,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,e5970b2440e4083c7d74b51c8991ac9fd0f54dc0@162.55.132.48:15634,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
