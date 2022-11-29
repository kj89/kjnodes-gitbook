# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (13)
```
peers="58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,f17140ac29380d434c1b5d2e33798d9f3bc6fd45@209.126.2.211:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,acd869ca67efdeae161974f5ce6a0010bf49ea1e@95.216.215.122:26656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,989c2419816cc187213cd604d09b088b4d64518c@195.3.222.189:26656,a234676afe7032f6b9933c0c64803a207b2affbe@38.242.208.212:40656,d49ed18a1c3ada861668d8ad391bbc66f4e41b4e@194.146.13.189:26656,cfd561edda42399f9a178f90d845063e756d6038@144.91.85.204:26656,4f40794ccb22ca1c7e33cd97b3460d497a2d0613@38.242.250.182:26656,deea630fc563decb676964e973c2c7314cb9dab4@65.21.147.148:26656,0d190196414307625a087a2d3cd02756fb4643a7@65.108.13.185:26767,c0fd97c27b0d96f2ae9dac5d31c6dff807bc8573@92.119.112.153:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
