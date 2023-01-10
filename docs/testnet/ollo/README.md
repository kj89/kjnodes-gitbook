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
peers="d915f25a07b79216e234e736f611b881d580f8b9@185.216.203.66:32656,3a178bcde0c4ebdcb933127e8440e49aafce894a@167.172.54.119:32656,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,95ca646da3736cef5d6c6704f736bc49ff87ef6c@109.123.249.213:26656,ef8863e006ba8eaea3aa8b780b01b82b401d7bd9@84.46.252.45:56656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,c83d2b5015c446e08f80c9d3662f4098077d635b@85.190.254.14:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,90ba3ab29147af2bc66a823d087ca49068d7974c@54.149.123.52:26656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,1d576b61c0c56a9b6ef6dabf336fd3cf04c017b1@95.217.223.85:15656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,5c3866af45b659bb2585f9209f95ed362079aa3b@38.242.149.134:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,287523060f2046e921dd329bd97110967798edca@194.247.12.102:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
