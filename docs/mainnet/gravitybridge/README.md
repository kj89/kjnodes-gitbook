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

**live-peers** (8)
```bash
peers="d1f6c66610b6b03e86b13675c842cc1a5fbb593b@95.216.67.178:26656,22d909fa9213c13324e19f6ec85c9771f03171ac@51.210.223.98:26656,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,df243a4c65b436fb4c81bf71b83ce9de865fea5a@213.239.207.165:26656,8357279ecb5f1b80eda324762a1406868c89bb5a@172.105.103.88:26656,a8d25e5e9cae32ae50537e4c83673ad61d589517@65.108.107.100:26656,4e406a1dcfc02de104925e6b8718c6364e1e0864@45.14.194.229:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
