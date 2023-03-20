# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/gravitybridge](https://explorer.kjnodes.com/gravitybridge)

## Public endpoints

* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)
* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* grpc: gravitybridge.grpc.kjnodes.com:26090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (12)
```bash
peers="4d82b4d1851982b6eb81e67cb3b5bd040eda7cdc@136.244.29.116:26666,a2b2723dffd2dc3a8e5ea727f60c3eca3a07c6f5@80.64.208.80:26656,e38de921f46e22de0be8e4eba0b0338cbd065fc9@51.81.159.162:26656,91e4523f2fcf6c7a8314b583d2f9f92cf93f10d7@51.250.18.132:26656,16f40620f1b1942246015f35c40dd9fc84e51b01@66.94.124.27:26656,ca4270ebed73b4d0982450aac16fe08860410fac@142.132.248.138:26626,6446a62a3db95347be2d7ea02feb2c834c226848@142.132.133.189:26656,03fabb7a15f8209c8eb8f5770c25bbee78a1d82c@94.130.8.219:26656,22d909fa9213c13324e19f6ec85c9771f03171ac@51.210.223.98:26656,a460c9af789a48396a2f5ee62e3f7e79a6b84d4f@46.38.243.16:26656,56a8349703e8f5c97c452c7e45f5bcaac966ccbf@207.180.204.110:26656,b7a74520da474918a4a60a5ee542ddb40322d5dd@167.235.108.189:27010"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
