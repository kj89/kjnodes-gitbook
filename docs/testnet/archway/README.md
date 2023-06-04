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

**live-peers** (25)
```bash
peers="20355d8c6b7e8c77576982bfca148b5cbd1a538d@185.230.138.95:26656,7f46c5c86639e04183cea341d62c59213cdc4542@185.230.138.49:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,13dc844645671d5da8ee81ab969d19166c3df11d@65.109.90.169:15656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,280fe9d15d5399bdd549487246dac82bab0a3fe8@220.85.113.33:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,354a554c8ba12260c130cc1d5b706b10aced51ab@143.198.206.192:34656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,5e0d6bfea56f7da5a1bdf9e4d1ee95c672a9d957@185.144.99.13:26656,0cf5d2bcc49c1acddb6b7b2bc547543ec2fbe844@34.239.246.206:26656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,11aa4b7b17ac0a3372e98d4cbf83aacd6cfbbfdd@58.187.251.205:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,85c669e01f5fca4d1ef7636a9526296a0083bb1d@15.235.193.57:26656,5869fe239308895eed0cdfdfdf386c7642a36459@38.242.227.84:15656,e50d7fa6a50ac792e5df61ff621d9621e9fcc8aa@34.133.135.231:26656,e82e213c14f7a1396b7deb968e945de1bfda8952@178.160.195.71:26656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,bb5b725dfb5d2b667e8d0396b6ca5429af19ee4c@120.226.39.230:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
