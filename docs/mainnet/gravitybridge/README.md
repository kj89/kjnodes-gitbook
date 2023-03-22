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

**live-peers** (13)
```bash
peers="811817c6ddc112ed37f7cd71c6bbae186f1e8239@135.125.188.17:34095,c4666a5c897463492246983fdc78ab20f32dc0c0@50.21.167.179:26656,a460c9af789a48396a2f5ee62e3f7e79a6b84d4f@46.38.243.16:26656,8bc91ffabd860b6b54766ac3788d7c284e45b964@174.138.30.240:26656,b7a74520da474918a4a60a5ee542ddb40322d5dd@167.235.108.189:27010,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,74efecf52ba78626d4ba796fb6073fa9cb26b19e@65.108.11.250:26656,1cab2a9034532b5a83a6469537da9c296c2ea09d@65.108.73.25:46656,12500973a0561656f86ea12ce3bbf05a48714ad8@35.79.31.168:26656,07e2da0edb0facd81dab948a128330cc1250b24c@193.70.47.90:14256,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656,70ff1535443969705182c9473cc66773fbc12c09@15.235.13.145:26656,2acf8add94531707982f17b91192866ad02de504@154.12.227.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
