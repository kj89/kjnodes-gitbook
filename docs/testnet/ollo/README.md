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

**live-peers** (32)
```bash
peers="67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,2f5965450c9c831266959632fba2c1533b8f676d@38.242.248.2:26656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,0d642afa8df369a5021609c43bb7765a332a615f@65.109.106.91:17656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,7864a2e4b42e5af76a83a8b644b9172fa1e40fa5@52.8.174.235:26656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,595a8418f3f68a499a873148ec19a95b0f34390c@65.109.82.106:32656,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,e2d59891f1aed38fe8884c63e0bb00f8ddc41b6f@5.78.46.66:26656,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
