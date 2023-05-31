# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.7.0 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/bitcanna](https://explorer.kjnodes.com/bitcanna)

## Public endpoints

* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)
* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* grpc: bitcanna.grpc.kjnodes.com:14290

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:14256
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:14259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```bash
peers="a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,0cd929dc9fda0b0267b6f32c15146f5f5fe50403@65.108.230.113:21326,86e5fc5d80aed6a52bf89245bcc53c1b77641113@88.99.33.248:12656,ec4796daea06ecf0e51819b931fbcb3e1a99b137@144.91.101.49:26656,07c829cf936db34be61143fabb09541d05aea899@65.108.98.124:64206,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14256,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
