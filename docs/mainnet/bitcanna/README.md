# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.3 | **Wasm**: OFF

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
peers="dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14256,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,8a3d8b8a6608f19fbdb34d330c9c9dd44a756a38@88.198.52.150:26666,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,2c46e946a2375111b345f5bd2a8617c0e5438767@94.130.200.168:46656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,ec4796daea06ecf0e51819b931fbcb3e1a99b137@144.91.101.49:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
