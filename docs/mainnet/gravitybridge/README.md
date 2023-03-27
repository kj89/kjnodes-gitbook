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

**live-peers** (14)
```bash
peers="572d417e11368f588d110efdeb7102a6a3c0752d@161.35.224.108:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,da401c011881747aa47b7348349edfc855794ba2@74.208.108.68:26656,288da01a1224eaeb931ce9a704e6ccd54fa59440@65.108.105.134:2000,961dc8a5e131e058c87c25f1d5c3b9395076e46a@65.108.106.131:26656,3eae7c785e7038b3c1376dc2fc8e6cff9d0ad709@65.108.121.110:14656,8fab97cbc7d11eddc56014eac8570232e596c18c@168.119.254.74:26656,9c3beda36b4e6d0a14fcb4e1a7823bb5495bcb10@159.69.58.176:26656,005263c9b18f6cbe5dd7805240535b1bcae195cb@51.195.145.104:26656,e5362a93c6e7f686d72c8d6d98be2c7bceeb5cc3@49.12.23.149:27010,a9e9c67632880147aad2517c9ee19cac6d9d052e@193.17.92.212:26656,c4666a5c897463492246983fdc78ab20f32dc0c0@50.21.167.179:26656,74efecf52ba78626d4ba796fb6073fa9cb26b19e@65.108.11.250:26656,8bc91ffabd860b6b54766ac3788d7c284e45b964@174.138.30.240:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
