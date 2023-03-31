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
peers="a9e9c67632880147aad2517c9ee19cac6d9d052e@193.17.92.212:26656,477d9806d76434ecba46502a5c850671b1aa888b@37.120.191.47:46656,9a8c4af7574a5d1fcd5e89f755348c7b6df3b4be@142.132.158.93:14256,56a8349703e8f5c97c452c7e45f5bcaac966ccbf@207.180.204.110:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,48e54221a2656616093469137ced63487f7bf456@146.56.50.55:26656,162d548d72d99f28478f85abb8926b52b8c9d362@65.109.88.107:36656,6770e29a9224810bcde6655b742d52b8a49d51e8@65.19.136.133:26656,db1e909b003e3d9d7565211db26295e84c4695a5@65.21.135.86:2000,e5362a93c6e7f686d72c8d6d98be2c7bceeb5cc3@49.12.23.149:27010,e38de921f46e22de0be8e4eba0b0338cbd065fc9@51.81.159.162:26656,16f40620f1b1942246015f35c40dd9fc84e51b01@66.94.124.27:26656,70ff1535443969705182c9473cc66773fbc12c09@15.235.13.145:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
