# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)


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

**live-peers** (23)
```bash
peers="b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,861d8791ee3912589a825278b28170f8c523dab0@45.147.199.129:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,0ce58fd448e62aa0c06c2603d8e047b9c7f9a3e5@38.242.158.251:26656,ef8863e006ba8eaea3aa8b780b01b82b401d7bd9@84.46.252.45:56656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,d915f25a07b79216e234e736f611b881d580f8b9@185.216.203.66:32656,1d576b61c0c56a9b6ef6dabf336fd3cf04c017b1@95.217.223.85:15656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
