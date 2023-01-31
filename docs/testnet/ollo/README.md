# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/ollo-testnet/None)


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

**live-peers** (24)
```bash
peers="dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,a9123ae1e1b7f8438e7262efd50031aab600df41@154.12.225.160:32656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,ef8863e006ba8eaea3aa8b780b01b82b401d7bd9@84.46.252.45:56656,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,771cfca799033e327511b25ae77784e02818d77f@65.108.101.4:23486,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,0ce58fd448e62aa0c06c2603d8e047b9c7f9a3e5@38.242.158.251:26656,1d576b61c0c56a9b6ef6dabf336fd3cf04c017b1@95.217.223.85:15656,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,5c3866af45b659bb2585f9209f95ed362079aa3b@38.242.149.134:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
