# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (22)
```
peers="cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,1f06a05a88b812f9e8147379a2bb82c8bab37e42@84.46.252.55:26656,45c6c9060c390a068cf1d6c1d9999af196b961ef@65.21.78.153:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,23eb7907fc731a8492f74c3c3694d4c232ba3a21@139.162.10.122:26656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,377008a2fb0f98dfd15a4a38b9a751a5a3b56446@135.181.104.247:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,b731df187ce2b278b60bc3469e13c6bac278dcc9@167.235.139.212:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,90ba3ab29147af2bc66a823d087ca49068d7974c@54.149.123.52:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18156"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
