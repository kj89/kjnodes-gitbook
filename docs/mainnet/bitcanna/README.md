# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.2 | **Wasm**: OFF

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
* grpc: bitcanna.grpc.kjnodes.com:42090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (19)
```bash
peers="9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
