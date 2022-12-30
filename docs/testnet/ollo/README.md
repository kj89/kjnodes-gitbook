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
peers="b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,a30e26c23f88ab7e64bf8cc4d5ed091832295db6@95.217.144.107:18156,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,b76de75c13b2e80febbf574df981a2bfd28a7de1@65.108.124.172:28656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,6fb1ca4b01926c43fb28f5eadc4710d0e7df8624@176.126.87.165:26656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,1f06a05a88b812f9e8147379a2bb82c8bab37e42@84.46.252.55:26656,eaccf85a393de7254b9c2538bb09666c5706e302@146.190.51.92:10656,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,d915f25a07b79216e234e736f611b881d580f8b9@185.216.203.66:32656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
