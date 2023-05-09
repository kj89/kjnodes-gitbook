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

**live-peers** (10)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12756,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,cf6854b4615508d264ad4404061b083aa70ce9c8@34.72.229.79:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.114:26656,506f9bca6ce2f29a2556427f90693a8ee1b100ff@178.128.238.183:26060,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,6ba72731d54ded6d012fa7b02ae46e0c214b1e07@5.75.230.116:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
