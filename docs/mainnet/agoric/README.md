# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoC | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/agoric](https://explorer.kjnodes.com/agoric)

## Public endpoints

* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)
* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* grpc: agoric.grpc.kjnodes.com:12790

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@agoric.rpc.kjnodes.com:12756
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:12759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (11)
```bash
peers="d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,e5970b2440e4083c7d74b51c8991ac9fd0f54dc0@162.55.132.48:15634,16f2ad1b7f154d6f8751c0ab7453e24f32ee8db3@95.217.45.52:26656,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,cccbc2151821e498e03a3a3df9115618571262a7@35.215.1.238:26656,93edbbec5e945f5cf692c96bf8181afef9687869@138.201.63.38:26666,86ae5b4d883a0b035a3ec0e17b1f98a545e6ad5b@44.225.233.214:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,1cbe5f5c77610bb6568332e026a3b516edeb0121@65.21.234.47:21156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
