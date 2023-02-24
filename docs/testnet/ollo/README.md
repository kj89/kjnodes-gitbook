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
peers="47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,a99fc4e81770ca32d574cac2e8680dccc9b55f74@18.144.61.148:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,fffb9164b9091d2055b5469a456ca91288517856@178.208.86.48:16656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,ef8863e006ba8eaea3aa8b780b01b82b401d7bd9@84.46.252.45:56656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,1d576b61c0c56a9b6ef6dabf336fd3cf04c017b1@95.217.223.85:15656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
