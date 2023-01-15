# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)


## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: https://ollo-testnet.grpc.kjnodes.com:443

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (23)
```bash
peers="861d8791ee3912589a825278b28170f8c523dab0@45.147.199.129:26656,519887d80be2c5c1725e4bb5210f6358090df5d4@64.227.75.6:26656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,45c6c9060c390a068cf1d6c1d9999af196b961ef@65.21.78.153:30656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,dfb2bba31436bc6cde54f475204ff53c9440804e@95.216.14.72:28656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,1d576b61c0c56a9b6ef6dabf336fd3cf04c017b1@95.217.223.85:15656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,c83d2b5015c446e08f80c9d3662f4098077d635b@85.190.254.14:32656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
