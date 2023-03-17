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

**live-peers** (11)
```bash
peers="4d82b4d1851982b6eb81e67cb3b5bd040eda7cdc@136.244.29.116:26666,4e406a1dcfc02de104925e6b8718c6364e1e0864@45.14.194.229:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,c4666a5c897463492246983fdc78ab20f32dc0c0@50.21.167.179:26656,ebec44e3e1558ade2487336f6d8d9d75954d3d8b@95.217.193.177:26656,ca9d9d0605f178fbba3bdf92e13719ab9dce0fc7@23.88.59.82:26656,56a8349703e8f5c97c452c7e45f5bcaac966ccbf@207.180.204.110:26656,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656,b7a74520da474918a4a60a5ee542ddb40322d5dd@167.235.108.189:27010,162e8994c0738fb5895e77b888718ea51d4c40d3@167.86.106.22:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
