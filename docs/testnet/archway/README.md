# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-3 | **Latest Version Tag**: v0.6.0 | **Wasm**: ON

[Website](https://archway.io) | [Discord](https://discord.gg/archwayhq) | [Twitter](https://twitter.com/archwayhq)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/archway-testnet](https://explorer.kjnodes.com/archway-testnet)

## Public endpoints

* api: [https://archway-testnet.api.kjnodes.com](https://archway-testnet.api.kjnodes.com)
* rpc: [https://archway-testnet.rpc.kjnodes.com](https://archway-testnet.rpc.kjnodes.com)
* grpc: archway-testnet.grpc.kjnodes.com:15690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@archway-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@archway-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/archway-testnet/addrbook.json > $HOME/.archway/config/addrbook.json
```

**live-peers** (15)
```bash
peers="e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,f7a7c6bf673c201c55ecf0d249df43826293d9d4@176.9.28.41:26656,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,7f46c5c86639e04183cea341d62c59213cdc4542@185.230.138.49:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,280fe9d15d5399bdd549487246dac82bab0a3fe8@220.85.113.33:26656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,85c669e01f5fca4d1ef7636a9526296a0083bb1d@15.235.193.57:26656,c0e7e484e576f5aca635449a4ed41c2e7097103f@65.109.30.197:23656,50fff25c44a764e50e83e08da7727fb2aa345101@65.109.93.58:40656,447644c34095606449e8f7eb34eeea2d9b7f2216@65.109.225.25:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,147c1668031ee62a85bd7293a845fdcf4f7b1857@182.139.205.219:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
