# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: ollo-testnet.grpc.kjnodes.com:32090

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

**live-peers** (30)
```bash
peers="0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,a9123ae1e1b7f8438e7262efd50031aab600df41@154.12.225.160:32656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,80c6ccc9523bd59a0420e76e8355f46fb61bf74f@65.109.93.58:33656,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856,70ba32724461c7ed4ec8d6ddc8b5e0b1cfb9e237@54.219.57.63:26656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,6fb1ca4b01926c43fb28f5eadc4710d0e7df8624@176.126.87.165:26656,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,b731df187ce2b278b60bc3469e13c6bac278dcc9@167.235.139.212:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
