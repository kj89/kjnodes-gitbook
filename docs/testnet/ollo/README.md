# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (32)
```bash
peers="90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,b731df187ce2b278b60bc3469e13c6bac278dcc9@167.235.139.212:26656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,2f5965450c9c831266959632fba2c1533b8f676d@38.242.248.2:26656,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,46cd4ab1a4fd92ee0ab510d05dce3cd00e639a05@3.235.146.125:26656,ef2b392423003fe81c92ff8de2d08febc19b220e@142.93.36.7:26656,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,95ca646da3736cef5d6c6704f736bc49ff87ef6c@109.123.249.213:26656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
