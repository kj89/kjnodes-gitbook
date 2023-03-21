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

**live-peers** (15)
```bash
peers="a460c9af789a48396a2f5ee62e3f7e79a6b84d4f@46.38.243.16:26656,ddf8f9ff250f760228c667d256d16ed4f1880c27@65.109.43.75:27010,a8d25e5e9cae32ae50537e4c83673ad61d589517@65.108.107.100:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,e5362a93c6e7f686d72c8d6d98be2c7bceeb5cc3@49.12.23.149:27010,774406f9e2c9c65e084effc8d823c470b82de6d0@146.19.24.186:26656,6446a62a3db95347be2d7ea02feb2c834c226848@142.132.133.189:26656,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,56a8349703e8f5c97c452c7e45f5bcaac966ccbf@207.180.204.110:26656,005263c9b18f6cbe5dd7805240535b1bcae195cb@51.195.145.104:26656,ca4270ebed73b4d0982450aac16fe08860410fac@142.132.248.138:26626,70ff1535443969705182c9473cc66773fbc12c09@15.235.13.145:26656,9a8c4af7574a5d1fcd5e89f755348c7b6df3b4be@142.132.158.93:14256,c4666a5c897463492246983fdc78ab20f32dc0c0@50.21.167.179:26656,1f43c723cb26092e20263905cbd71609d87a9c00@172.104.202.149:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
