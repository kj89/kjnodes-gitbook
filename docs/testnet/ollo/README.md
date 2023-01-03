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

**live-peers** (20)
```
peers="e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,3a178bcde0c4ebdcb933127e8440e49aafce894a@167.172.54.119:32656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,1d576b61c0c56a9b6ef6dabf336fd3cf04c017b1@95.217.223.85:15656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,6aa3e31cc85922be69779df9747d7a08326a44f2@65.108.121.240:28656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
