# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)




## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: [https://ollo-testnet.grpc.kjnodes.com](https://ollo-testnet.grpc.kjnodes.com)

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

**live-peers** (22)
```bash
peers="536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,0d642afa8df369a5021609c43bb7765a332a615f@65.109.106.91:17656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,80c6ccc9523bd59a0420e76e8355f46fb61bf74f@65.109.93.58:33656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
