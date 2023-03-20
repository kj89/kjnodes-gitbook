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
peers="7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,845dc78ccd4e3509d0f00dd6151bcebc8dde0324@66.94.99.253:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,803fc66e3bd7b724921ef9c40636067f36e880c6@65.108.199.222:26356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
